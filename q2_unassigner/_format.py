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
    pass


class UnassignerStatsDirFmt(model.DirectoryFormat):
    unassigner_output = model.File(
        "unassigner_output.tsv", format=UnassignerStatsFmt
    )
