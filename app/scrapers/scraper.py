from abc import ABC, abstractmethod

from collections import namedtuple

TenantInfo = namedtuple('TenantInfo', ['address', 'email', 'phone_number'])


class Scraper(ABC):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @abstractmethod
    def process(self):
        """
        run a scraper which scrape the tenant information from a portal
        :return: TenantInfo namedtuple
        """
        pass

