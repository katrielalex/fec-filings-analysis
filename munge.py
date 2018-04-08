#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Katriel's FEC data munger

Author: Katriel Cohn-Gordon <me@katriel.co.uk>
Date: 2017
"""

import click
import logging
import matplotlib.pyplot as plt
import pandas as pd

log = logging.getLogger('fec')


@click.command()
@click.argument('company-contributions', type=click.File(), default='data/facebook_contributions.csv')
@click.argument('committees', type=click.File(), default='data/committees.csv')
def main(company_contributions, committees):
    """
    Munge some FEC data files
    """
    log.info(f'Reading {company_contributions.name} and {committees.name}...')
    df = pd.read_table(committees, sep=',')
    cid_to_party = df.set_index('committee_id').party

    log.info('Munging')
    contribs = pd.read_table(company_contributions, sep=',')
    contribs = contribs[[
        'committee_id',
        'committee_name',
        'contribution_receipt_amount',
    ]]
    contribs['party'] = contribs['committee_id'].map(cid_to_party)
    totals = contribs.groupby('committee_name')[
        'contribution_receipt_amount'
    ].sum().sort_values()
    log.debug(f'Got {len(totals)} grouped contributions')

    log.info('Plotting')
    contribs.groupby('party').sum().plot.pie(y='contribution_receipt_amount')
    plt.show()

    log.info('Bye!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
