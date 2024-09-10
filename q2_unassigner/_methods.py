# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import subprocess as sp
from pathlib import Path
from q2_types.feature_data import FeatureData, Sequence
from q2_types.feature_table import FeatureTable, Frequency


def run_command(cmd):
    print(
        "Running external command line application. This may print "
        "messages to stdout and/or stderr."
    )
    print(
        "The command being run is below. This command cannot "
        "be manually re-run as it will depend on temporary files that "
        "no longer exist."
    )
    print("\nCommand:", end=" ")
    print(" ".join(cmd), end="\n\n")
    sp.run(cmd, check=True)


def unassign(
    seqs: FeatureData[Sequence], output_fp: Path = "./q2_unassigner/"
) -> FeatureTable[Frequency]:
    cmd = ["unassign", str(seqs), "--output_dir", str(output_fp)]
    run_command(cmd)

    # Convert outputs to QIIME2 compatible formats

    return FeatureTable[Frequency]()
