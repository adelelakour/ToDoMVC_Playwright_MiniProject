from playwright.sync_api import Playwright, Page, Expect, expect
from urllib3.util import wait


def test_add_single_todo(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.locator("body")).to_contain_text("Renew my passport")
    expect(page.locator("body")).to_contain_text("1 item left!")

def test_multiple_todos(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Do a playwright mini-project")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.locator("body")).to_contain_text("Renew my passport")
    expect(page.locator("body")).to_contain_text("Renew my driving license")
    expect(page.locator("body")).to_contain_text("Do a playwright mini-project")
    expect(page.locator("body")).to_contain_text("3 items left!")

def test_empty_todo(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.locator("body")).not_to_contain_text("Active")

def test_white_space_todo(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill(" ")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.locator("body")).not_to_contain_text("Active")

def test_duplicated_todos(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.locator("body")).to_contain_text("2 items left!")

