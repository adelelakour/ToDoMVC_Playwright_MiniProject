from playwright.sync_api import Playwright, Page, Expect, expect
from urllib3.util import wait
import re


def test_completed_todos(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Do one Playwright project")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    #verify that completed todos show up under Completed tab
    renew_passport = page.locator("li").filter(has_text="Renew my passport")
    renew_passport.locator('input[type="checkbox"]').check()
    page.get_by_role("link", name="Completed").click()
    expect(page.locator("body")).to_contain_text("Renew my passport")


def test_active_todos(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Do one Playwright project")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    renew_passport = page.locator("li").filter(has_text="Renew my passport")
    renew_passport.locator('input[type="checkbox"]').check()
    page.get_by_role("link", name="Active").click()
    expect(page.locator("body")).to_contain_text("Renew my driving license")
    expect(page.locator("body")).to_contain_text("Do one Playwright project")

def test_toggle_all(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Do one Playwright project")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    renew_passport = page.locator("li").filter(has_text="Renew my passport")
    renew_passport.locator('input[type="checkbox"]').check()
    renew_license = page.locator("li").filter(has_text="Renew my driving license")
    renew_license.locator('input[type="checkbox"]').check()
    doProject = page.locator("li").filter(has_text="Do one Playwright project")
    doProject.locator('input[type="checkbox"]').check()

    page.get_by_role("link", name="Completed").click()
    expect(page.locator("body")).to_contain_text("Renew my passport")
    expect(page.locator("body")).to_contain_text("Renew my driving license")
    expect(page.locator("body")).to_contain_text("Do one Playwright project")

    #untick completed todos
    page.get_by_role("link", name="All").click()
    renew_passport = page.locator("li").filter(has_text="Renew my passport")
    renew_passport.locator('input[type="checkbox"]').uncheck()
    renew_license = page.locator("li").filter(has_text="Renew my driving license")
    renew_license.locator('input[type="checkbox"]').uncheck()
    doProject = page.locator("li").filter(has_text="Do one Playwright project")
    doProject.locator('input[type="checkbox"]').uncheck()

    expect(page.locator("body")).to_contain_text("Renew my passport")
    expect(page.locator("body")).to_contain_text("Renew my driving license")
    expect(page.locator("body")).to_contain_text("Do one Playwright project")

    page.wait_for_timeout(6000)
