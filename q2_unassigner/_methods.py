# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import skbio
import subprocess as sp
import tempfile
from pathlib import Path
from q2_types.feature_data import DNAFASTAFormat, FeatureData, Sequence
from q2_unassigner._format import UnassignerStatsDirFmt, UnassignerStatsFmt
from q2_unassigner._type import UnassignerStats


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
    seqs: DNAFASTAFormat,
) -> UnassignerStatsFmt:
    print("Starting unassigner...")
    unassigner_output = UnassignerStatsFmt()

    cmd = ["unassign", str(seqs), "--output_dir", str(Path(str(unassigner_output)).parents[0])]
    run_command(cmd)

    print("Unassigner output saved at:", unassigner_output)
    return unassigner_output
