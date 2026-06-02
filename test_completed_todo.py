import re

from playwright.sync_api import Playwright, Page, Expect, expect
from urllib3.util import wait

def test_completed_todo(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    task = page.locator("li").filter(has_text="Renew my passport")
    task.locator('input[type="checkbox"]').check()
    expect(task).to_have_class(re.compile("completed"))
    page.wait_for_timeout(2000)

