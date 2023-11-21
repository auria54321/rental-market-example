import argparse


def parse_input():
    parser = argparse.ArgumentParser(description='retrieve data from portal into database')
    parser.add_argument('tenant_portal',
                        help='Curretnly support only "click_pay"')

    parser.add_argument('username',
                        help='Curretnly support only "click_pay"')

    parser.add_argument('password',
                        help='Curretnly support only "click_pay"')

    args = parser.parse_args()
    return args
