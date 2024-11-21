#!/usr/bin/env python

import argparse
import csv
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()

page.goto("https://cses.fi/problemset/")
page.get_by_text("Login").click()
page.fill('input[type="text"]', os.environ["CSES_USERNAME"])
page.fill('input[type="password"]', os.environ["CSES_PASSWORD"])
page.click('input[type="submit"]')

task_submit_base_url = "https://cses.fi/problemset/submit"

tasks_csv = Path(__file__).parent / "tasks.csv"
current_task = None

with tasks_csv.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "unsolved":
            current_task = row
            break


def test():
    task_dir = Path(__file__).parent / "tasks" / current_task["path"]
    print(
        "\n",
        "\033[33m",
        " ".join(
            word.title() for word in current_task["path"].split("/")[1].split("-")[1:]
        ),
        "\033[0m",
        "\n",
    )
    for example_dir in (task_dir / "examples").iterdir():
        with (example_dir / "in").open("r") as f_in, (example_dir / "out").open(
            "r"
        ) as f_out:
            result = None
            try:
                expected_output = f_out.read().strip()

                result = subprocess.run(
                    [sys.executable, task_dir / "solution.py"],
                    input=f_in.read(),
                    capture_output=True,
                    text=True,
                    timeout=2,
                )

                if result.returncode != 0:
                    print(
                        " " * 2,
                        "\033[31m",
                        f"[{example_dir.name}]",
                        "RUNTIME ERROR",
                        "\033[0m",
                    )
                    print(
                        " " * 6,
                        "\n".join(
                            " " * 6 + line for line in result.stderr.splitlines()
                        ),
                        "\n",
                    )
                else:
                    output = result.stdout.strip()

                    if output == expected_output:
                        print(
                            "\033[32m",
                            " " * 2,
                            f"[{example_dir.name}]",
                            "ACCEPTED",
                            "\033[0m",
                        )
                    else:
                        print(
                            " " * 2,
                            "\033[31m",
                            f"[{example_dir.name}]",
                            "WRONG ANSWER",
                            "\033[0m",
                        )
                        print(" " * 6, repr(output))
                        print(" " * 6, repr(expected_output), "\n")

            except subprocess.TimeoutExpired:
                print(
                    " " * 2,
                    "\033[31m",
                    f"[{example_dir.name}]",
                    "TIME LIMIT EXCEEDED",
                    "\033[0m",
                )

    print()


def submit():
    task_submit_url = f"{task_submit_base_url}/{current_task['cses_id']}/"
    task_dir = Path(__file__).parent / "tasks" / current_task["path"]

    page.goto(task_submit_url)
    with page.expect_file_chooser() as fc_info:
        page.click('input[type="file"]')

    file_chooser = fc_info.value
    file_chooser.set_files(task_dir / "solution.py")
    page.click('input[type="submit"]')

    page.wait_for_selector(
        'td:has-text("result")', timeout=10000
    )  # wait for 10 seconds

    print(
        "\n",
        "\033[33m",
        " ".join(
            word.title() for word in current_task["path"].split("/")[1].split("-")[1:]
        ),
        "\033[0m",
        end="",
    )
    verdict = page.locator("td:has-text('result') + td").text_content()
    if verdict == "ACCEPTED":
        print("\033[32m", f"[{verdict}]", "\033[0m", "\n")
    else:
        print("\033[31m", f"[{verdict}]", "\033[0m", "\n")


def next_():
    rows = []
    with tasks_csv.open("r") as f:
        reader = csv.DictReader(f)
        rows = [
            {**row, "status": "solved"} if row["path"] == current_task["path"] else row
            for row in reader
        ]
    print(len(rows))
    with tasks_csv.open("w") as f:
        print(len(rows))
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser("cses")
    subparsers = parser.add_subparsers(dest="command")

    test_parser = subparsers.add_parser("test")
    test_parser.set_defaults(func=test)

    submit_parser = subparsers.add_parser("submit")
    submit_parser.set_defaults(func=submit)

    submit_parser = subparsers.add_parser("next")
    submit_parser.set_defaults(func=next_)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func()


if __name__ == "__main__":
    main()
