# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin.testing import TestPluginBase
from q2_types.feature_data import DNAFASTAFormat

from q2_unassigner._methods import unassign
from unassigner.parse import parse_results


class UnassignTests(TestPluginBase):
    package = "q2_unassigner.tests"

    def test_unassign(self):
        # test that the unassign method runs without error
        # (for demonstration purposes)
        # seqs = transform(
        #    self.get_data_path('gg10.fasta'),
        #    from_type=DNAFASTAFormat,
        #    to_type=FeatureData[Sequence])
        seqs_fp = self.get_data_path("gg10.fasta")
        seqs = DNAFASTAFormat(seqs_fp, mode="r")
        observed = unassign(seqs)

        parsed_results = list(
            parse_results(open(observed.unassigner_output.path_maker(), "r"))
        )

        print("Parsed results: ", parsed_results)

        self.assertEqual(len(parsed_results), 20)
