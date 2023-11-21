from enum import Enum
import logging

from scrapers.click_pay import ClickPayScraper
from scrapers.scraper import TenantInfo, Scraper
from models.tenant import Tenant


class TenantPortalEnum(Enum):
    CLICK_PAY = 'click_pay'


def get_scraper(tenant_portal: str, username: str, password: str) -> Scraper:
    if tenant_portal == TenantPortalEnum.CLICK_PAY.value:
        return ClickPayScraper(username=username, password=password)


def process(tenant_portal: str, username: str, password: str):
    scraper = get_scraper(tenant_portal=tenant_portal, username=username, password=password)
    logging.info(f'Initiate scraper: {scraper.__class__.__name__}, start scraping')
    tenant: TenantInfo = scraper.process()
    logging.info(f'TenantInfo: address: {tenant.address}, email: {tenant.email}, phone_number: {tenant.phone_number}')
    tenant_entity = Tenant(address=tenant.address, company=tenant_portal, email=tenant.email,
                           phone_number=tenant.phone_number)
    Tenant.add_tenant(tenant_entity)
