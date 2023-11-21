import logging

from utils.parse_util import parse_input
from controllers.portal import process, TenantPortalEnum
from models.database import create_tables

logging.basicConfig(level=logging.DEBUG)


def main():
    create_tables()
    args = parse_input()
    if args.tenant_portal != TenantPortalEnum.CLICK_PAY.value:
        logging.error('Invalid tenant portal, available values: "click_pay"')
        return
    logging.info(f'Retrieving data from {args.tenant_portal}, username: {args.username}')
    process(tenant_portal=args.tenant_portal, username=args.username, password=args.password)
    logging.info(f'Finished process successfully')


if __name__ == '__main__':
    main()
