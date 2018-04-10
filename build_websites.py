#!/usr/bin/env python3

import argparse
import jinja2
import logging
import os
import ruamel.yaml as yaml

from logos import custom_logos

log = logging.getLogger('fec_analysis')


def load(donations_path):
    with open(donations_path) as donations_yaml:
        donations = yaml.safe_load(donations_yaml)

    return donations


def render(donations):
    loader = jinja2.FileSystemLoader('./')
    environment = jinja2.Environment(loader=loader)

    company_logos = {c: f"<i class='fab fa-{c}'></i>" for c in donations}
    company_logos.update({c: l for c, l in custom_logos.items() if c in company_logos})

    log.info('rendering index.html')
    environment.get_template('index.jinja2').stream(logos=company_logos).dump('index.html')

    log.info('rendering company pages')
    company_page = environment.get_template('company_page.jinja2')
    for company, info in donations.items():
        log.info(f'rendering {len(info["donations"])} donations for {company}')
        company_page.stream(
            company=company,
            logo=company_logos[company],
            fec_url=info['url'],
            donations=info['donations'],
        ).dump(f'{company}.html')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('donations', help='yaml donations file')
    args = parser.parse_args()

    donations = load(args.donations)
    render(donations)
