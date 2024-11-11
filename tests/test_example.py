from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://hwm.puzzak.page/")
    print("Page Title:", page.title())
    browser.close()

with sync_playwright() as playwright:
    run(playwright)