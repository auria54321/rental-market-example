from playwright.sync_api import sync_playwright
from scrapers.scraper import TenantInfo, Scraper

CLICK_PAY_BASE_URL = 'https://www.clickpay.com'


class ClickPayScraper(Scraper):

    def process(self):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(CLICK_PAY_BASE_URL)
            page.locator('.login.btn_login').click()
            page.wait_for_timeout(1000)
            page.locator('input[name="h_txt_Username"]').type(self.username)
            page.locator('input[name="h_txt_Password"]').type(self.password)
            page.locator('button[name="submitbtn"]').click()
            page.wait_for_timeout(2000)
            address = page.locator('.pn_unit_block_addr.header-sm.address').text_content()
            page.goto(f'{CLICK_PAY_BASE_URL}/app#UserProfile')
            page.wait_for_timeout(1000)
            email = page.locator('input[aria-label="Email"]').input_value()
            phone_number = page.locator('input[aria-label="Mobile Phone"]').input_value()
            browser.close()
            return TenantInfo(address=address, email=email, phone_number=phone_number)
