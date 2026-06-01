from playwright.sync_api import Playwright, Page, Expect, expect
from urllib3.util import wait


def test_basics(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Apply for 3 QA Automation Jobs in Germany")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    #validate that Renew my driving license is there
    expect(page.locator("body")).to_contain_text("Renew my driving license")





    page.wait_for_timeout(3000)