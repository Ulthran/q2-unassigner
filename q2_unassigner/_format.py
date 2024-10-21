# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2.plugin.model as model
from qiime2.plugin import ValidationError
from q2_types.feature_data import DNAFASTAFormat
from unassigner.parse import parse_results


class UnassignerStatsFmt(model.TextFileFormat):
    def _check_records(self):
        with open(str(self)) as f:
            try:
                list(parse_results(f))
            except Exception as e:
                raise ValidationError(str(e))

    def _validate_(self, level: str = "max"):
        self._check_records()


class UnassignerQueryHitsFmt(model.TextFileFormat):
    def _validate_(self, level: str = "max"):
        pass


class UnassignerStatsDirFmt(model.DirectoryFormat):
    unassigner_output = model.File(
        "unassigner_output.tsv", format=UnassignerStatsFmt
    )
    extended_output = model.File(
        "algorithm_output.tsv", format=UnassignerStatsFmt
    )
    query_hits = model.File(
        "unassigner_query_hits.txt", format=UnassignerQueryHitsFmt
    )
    query = model.File("unassigner_query.fasta", format=DNAFASTAFormat)

    def _validate_(self, level: str = "max"):
        pass
