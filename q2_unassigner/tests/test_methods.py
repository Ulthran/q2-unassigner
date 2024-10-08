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
from q2_types.feature_data import DNAFASTAFormat, FeatureData, Sequence

from q2_unassigner._methods import unassign
# TODO: Remove this once unassigner updates are pushed to conda/PyPi
from q2_unassigner._format import parse_results
#from unassigner.parse import parse_results


class UnassignTests(TestPluginBase):
    package = "q2_unassigner.tests"

    def test_unassign(self):
        # test that the unassign method runs without error
        # (for demonstration purposes)
        #seqs = transform(
        #    self.get_data_path('gg10.fasta'),
        #    from_type=DNAFASTAFormat,
        #    to_type=FeatureData[Sequence])
        seqs_fp = self.get_data_path("gg10.fasta")
        seqs = DNAFASTAFormat(seqs_fp, mode='r')
        print(str(seqs))
        observed = unassign(seqs)

        print(list(parse_results(open(str(observed), 'r'))))

        # no real output to check here, just check that the method runs without error