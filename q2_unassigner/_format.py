# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2.plugin.model as model
from qiime2.plugin import ValidationError
from unassigner.parse import parse_results


class UnassignerStatsFmt(model.TextFileFormat):

    def _check_records(self):
        with open(str(self)) as f:
            try:
                list(parse_results(f))
            except Exception as e:
                raise ValidationError(str(e))

    def _validate_(self):
        self._check_records()


# UnassignerStatsDirFmt = model.SingleFileDirectoryFormat(
#    'UnassignerStatsDirFmt', 'unassigner_output.tsv', UnassignerStatsFmt)
class UnassignerStatsDirFmt(model.DirectoryFormat):
    unassigner_output = model.File(
        "unassigner_output.tsv", format=UnassignerStatsFmt
    )

    def _validate_(self):
        self.unassigner_output.validate()
