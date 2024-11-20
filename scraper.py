import csv
from pathlib import Path

from playwright.sync_api import sync_playwright

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
            task_slug = f'{str(j).rjust(2, "0")}-{title.replace("'", "").replace(" ", "-").lower()}'

            task_dir = category_dir / task_slug
            task_dir.mkdir(exist_ok=True)

            (task_dir / "solution.py").touch(exist_ok=True)

            writer.writerow(
                {
                    "path": f"{category_slug}/{task_slug}",
                    "cses_id": _id,
                    "status": "unsolved",
                }
            )

browser.close()
playwright.stop()
