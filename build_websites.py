#!/usr/bin/env python3

import argparse
import jinja2
import logging
import os
import ruamel.yaml as yaml


log = logging.getLogger("fec_analysis")


def load(donations_path):
    with open(donations_path) as donations_yaml:
        donations = yaml.safe_load(donations_yaml)

    return donations


def render(donations, template_path):
    path, filename = os.path.split(template_path)
    template = jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename)

    for company, info in donations.items():
        log.info(f"rendering {len(info['donations'])} donations for {company}")
        template.stream(
            company=company,
            fec_url=info['url'],
            donations=info['donations'],
        ).dump(f"{company}.html")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("donations", help="yaml donations file")
    parser.add_argument("template", help="html template")
    args = parser.parse_args()

    donations = load(args.donations)
    render(donations, args.template)
