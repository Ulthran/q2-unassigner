# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Bool, Float, Int, TextFileFormat
from qiime2.plugin.testing import TestPluginBase
from q2_types.feature_data import DNAFASTAFormat

from q2_unassigner._methods import unassign
from unassigner.parse import parse_results


class UnassignTests(TestPluginBase):
    package = "q2_unassigner.tests"

    def test_unassign(self):
        seqs_fp = self.get_data_path("gg10.fasta")
        seqs = DNAFASTAFormat(seqs_fp, mode="r")
        observed = unassign(seqs)

        parsed_results = list(
            parse_results(open(observed.unassigner_output.path_maker(), "r"))
        )

        print("Parsed results: ", parsed_results)

        # Maybe not the most thorough test but I'd like to leave testing
        # functionality to unassigner itself
        self.assertEqual(len(parsed_results), 20)

    def test_unassign_with_params(self):
        seqs_fp = self.get_data_path("gg10.fasta")
        seqs = DNAFASTAFormat(seqs_fp, mode="r")
        type_strain_fp = self.get_data_path("unassigner_species.fasta")
        ref_mismatch_fp = self.get_data_path("mismatch_db.txt")
        observed = unassign(
            seqs=seqs,
            type_strain_fasta=type_strain_fp,
            threshold=0.96,
            ref_mismatch_positions=ref_mismatch_fp,
            num_cpus=2,
            soft_threshold=True,
            verbose=True,
        )

        parsed_results = list(
            parse_results(open(observed.unassigner_output.path_maker(), "r"))
        )

        print("Parsed results: ", parsed_results)

        # Maybe not the most thorough test but I'd like to leave testing
        # functionality to unassigner itself
        self.assertGreater(len(parsed_results), 20)
