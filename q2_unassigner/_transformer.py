# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import collections

import pandas as pd
import numpy as np
import qiime2

from .plugin_setup import plugin
from ._format import UnassignerStatsFmt

_unassigner_stats_header = collections.OrderedDict([
    ('query_id', str),
    ('species', str),
    ('typestrain_id', str),
    ('region_mismatches', int),
    ('region_positions', int),
    ('probability_incompatible', float)])


def _stats_to_df(ff):
    df = pd.read_csv(str(ff), sep='\t', index_col=["query_id", "species"])
                    # Gets messed up by NAs for int/float values
                    #names=_unassigner_stats_header.keys(),
                    #dtype=_unassigner_stats_header)
    return df


@plugin.register_transformer
def _1(ff: UnassignerStatsFmt) -> qiime2.Metadata:
    return qiime2.Metadata(_stats_to_df(ff))


@plugin.register_transformer
def _2(ff: UnassignerStatsFmt) -> pd.DataFrame:
    return _stats_to_df(ff)