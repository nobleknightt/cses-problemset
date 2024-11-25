import csv
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()

page.goto("https://cses.fi/problemset/")

h2_elements = page.query_selector_all("h2")
categories = [h2.inner_text() for h2 in h2_elements[1:]]

tasks_dir = Path(__file__).parent / "tasks"
tasks_dir.mkdir(exist_ok=True)

with open("tasks.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["path", "cses_id", "status"])
    writer.writeheader()

    for i, category in enumerate(categories, start=1):
        category_slug = f'{str(i).rjust(2, "0")}-{category.replace(" ", "-").lower()}'

        category_dir = tasks_dir / category_slug
        category_dir.mkdir(exist_ok=True)

        a_elements = page.query_selector_all(f'h2:has-text("{category}") + ul a')
        ids = [
            a.get_attribute("href").removeprefix("/problemset/task/")
            for a in a_elements
        ]
        titles = [a.inner_text() for a in a_elements]

        for j, (_id, title) in enumerate(zip(ids, titles), start=1):
            task_slug = f'{str(j).rjust(2, "0")}-{title.replace("ü", "u").replace("'", "").replace(" ", "-").lower()}'

            task_dir = category_dir / task_slug
            task_dir.mkdir(exist_ok=True)

            task_file = task_dir / "task.md"
            task_file.touch(exist_ok=True)

            with task_file.open("w") as f:
                f.write(f"# {title.replace("ü", "u")} \n\n")

            solution_file = task_dir / "solution.py"
            solution_file.touch(exist_ok=True)

            with solution_file.open("w") as f:
                f.write(f"# {title.replace("ü", "u").lower()} \n\n")

            writer.writerow(
                {
                    "path": f"{category_slug}/{task_slug}",
                    "cses_id": _id,
                    "status": "unsolved",
                }
            )

task_base_url = "https://cses.fi/problemset/task"
tasks_csv = Path(__file__).parent / "tasks.csv"

with tasks_csv.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        page.goto(f"{task_base_url}/{row['cses_id']}")

        with (Path(__file__).parent / "tasks" / row["path"] / "task.md").open(
            "a", encoding="utf-8"
        ) as tasks_md:
            try:
                page.locator(".md").evaluate(
                    """
                    (node) => {
                        const mrowElements = document.querySelectorAll('mrow');
                        mrowElements.forEach((element) => {
                            element.remove();
                        });
                        const katexElements = document.querySelectorAll('.katex-html');
                        katexElements.forEach((element) => {
                            element.remove();
                        });
                        const images = document.querySelectorAll('img[src^="/file"]');
                        images.forEach((image, i) => {
                            const imgUrl = image.getAttribute('src');
                            const imageName = imgUrl.split('/').pop();
                            const span = document.createElement('span');
                            span.textContent = '\\n![](./images/' + imageName + '.png)\\n';
                            image.insertAdjacentElement('afterend', span);
                        });
                        const h1Elements = document.querySelectorAll('h1');
                        h1Elements.forEach((element) => {
                            element.textContent = '## ' + element.textContent;
                        });
                        const annotationElements = document.querySelectorAll('annotation');
                        annotationElements.forEach((element) => {
                            element.textContent = '```' + element.textContent + '```';
                        });
                        const listItemElements = node.querySelectorAll('li');
                        listItemElements.forEach((element) => {
                            element.innerHTML = '- ' + element.innerHTML;
                        });
                        const headings = document.querySelectorAll('h1:not([id^="example"])');
                        headings.forEach((element) => {
                            let nextElement = element.nextElementSibling;
                            console.log(nextElement, nextElement.id, nextElement.id === "example")
                            if (nextElement && nextElement.tagName === 'P') {
                                nextElement.textContent = '- ' + nextElement.textContent;
                            }
                        });
                        const preElements = document.querySelectorAll('pre');
                        preElements.forEach((element) => {
                            element.textContent = '```\\n' + element.textContent.trim() + '\\n```\\n';
                        });
                        return node.innerText
                    }
                    """
                )

                images = [
                    image.get_attribute("src")
                    for image in page.locator("img").all()
                    if image.get_attribute("src").startswith("/file")
                ]

                if images:
                    images_dir = (
                        Path(__file__).parent / "tasks" / row["path"] / "images"
                    )
                    images_dir.mkdir(exist_ok=True)
                    for image_url in images:
                        response = requests.get(f"https://cses.fi{image_url}")
                        image_file = images_dir / f'{image_url.split("/")[-1]}.png'
                        with image_file.open("wb") as f:
                            f.write(response.content)

                examples_dir = (
                    Path(__file__).parent / "tasks" / row["path"] / "examples"
                )
                examples_dir.mkdir(exist_ok=True)

                for i, pre in enumerate(page.locator('h1[id^="example"] ~ pre').all()):
                    example_dir = examples_dir / str(i // 2 + 1).rjust(2, "0")
                    example_dir.mkdir(exist_ok=True)
                    if i % 2 == 0:
                        with (example_dir / "in").open("w") as f:
                            f.write(
                                pre.text_content()
                                .strip()
                                .removeprefix("```")
                                .removesuffix("```")
                                .strip()
                            )
                            f.write("\n")
                    else:
                        with (example_dir / "out").open("w") as f:
                            f.write(
                                pre.text_content()
                                .strip()
                                .removeprefix("```")
                                .removesuffix("```")
                                .strip()
                            )
                            f.write("\n")

                tasks_md.write(page.locator(".md").text_content())

            except Exception as e:
                print(row, e)

page.goto("https://cses.fi/problemset/")
page.get_by_text("Login").click()
page.fill('input[type="text"]', os.environ["CSES_USERNAME"])
page.fill('input[type="password"]', os.environ["CSES_PASSWORD"])
page.click('input[type="submit"]')

tests_base_url = "https://cses.fi/problemset/tests"
tasks_csv = Path(__file__).parent / "tasks.csv"

with tasks_csv.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            page.goto(f"{tests_base_url}/{row['cses_id']}")
            with page.expect_download() as download:
                page.click('input[value="Download"]')
            download.value.save_as(
                Path(__file__).parent / "tasks" / row["path"] / "tests.zip"
            )

        except Exception as e:
            print(row, e)

browser.close()
playwright.stop()
