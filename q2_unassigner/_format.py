# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2.plugin.model as model
from qiime2.plugin import ValidationError
#from unassigner.parse import parse_results


# TODO: Remove these once unassigner updates are pushed to conda/PyPi
def cast_num_or_na(val, cast_func):
    if val == "NA":
        return None
    return cast_func(val)


def parse_results(f):
    float_fields = ["probability_incompatible"]
    int_fields = ["region_mismatches", "region_positions"]
    header_line = next(f)
    header_line = header_line.rstrip()
    fields = header_line.split("\t")
    for line in f:
        line = line.rstrip()
        vals = line.split("\t")
        res = dict(zip(fields, vals))
        for field, val in res.items():
            if field in float_fields:
                res[field] = cast_num_or_na(val, float)
            elif field in int_fields:
                res[field] = cast_num_or_na(val, int)
        yield res


class UnassignerStatsFmt(model.TextFileFormat):

    def _check_records(self):
        with open(str(self)) as f:
            try:
                list(parse_results(f))
            except Exception as e:
                raise ValidationError(str(e))

    def _validate_(self):
        self._check_records()


UnassignerStatsDirFmt = model.SingleFileDirectoryFormat(
    'UnassignerStatsDirFmt', 'unassigner_output.tsv', UnassignerStatsFmt)