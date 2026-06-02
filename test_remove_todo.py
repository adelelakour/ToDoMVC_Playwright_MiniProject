from playwright.sync_api import Playwright, Page, Expect, expect
from urllib3.util import wait
import re


def test_remove_todo(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Do one Playwright project")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    todo = page.locator("li", has_text="Renew my driving license")
    todo.hover()
    todo.get_by_role("button").click()

    expect(page.locator("body")).not_to_contain_text("Renew my driving license")
    expect(page.locator("body")).to_contain_text("2 items left!")


