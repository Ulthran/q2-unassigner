# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pandas as pd
import pandas.testing as pdt

from qiime2.plugin.testing import TestPluginBase
from qiime2.plugin.util import transform
from q2_types.feature_data import FeatureData, Sequence
from q2_types.feature_table import FastaFormat

from q2_unassigner._methods import unassign


class UnassignTests(TestPluginBase):
    package = "q2_unassigner.tests"

    def test_unassign(self):
        # test that the unassign method runs without error
        # (for demonstration purposes)
        seqs = transform(
            self.get_data_path("gg10.fasta"),
            from_type=FastaFormat,
            to_type=FeatureData[Sequence],
        )
        observed = unassign(seqs)

        # no real output to check here, just check that the method runs without error

class DuplicateTableTests(TestPluginBase):
    package = "q2_unassigner.tests"

    def test_simple1(self):
        in_table = pd.DataFrame(
            [[1, 2, 3, 4, 5], [9, 10, 11, 12, 13]],
            columns=["abc", "def", "jkl", "mno", "pqr"],
            index=["sample-1", "sample-2"],
        )
        observed = duplicate_table(in_table)

        expected = in_table

        pdt.assert_frame_equal(observed, expected)

    def test_simple2(self):
        # test table duplication with table loaded from file this time
        # (for demonstration purposes)
        in_table = transform(
            self.get_data_path("table-1.biom"),
            from_type=BIOMV100Format,
            to_type=pd.DataFrame,
        )
        observed = duplicate_table(in_table)

        expected = in_table

        pdt.assert_frame_equal(observed, expected)
