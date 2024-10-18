# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import subprocess as sp
from q2_types.feature_data import DNAFASTAFormat
from q2_unassigner._format import UnassignerStatsDirFmt


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
) -> UnassignerStatsDirFmt:
    print("Starting unassigner...")
    unassigner_output = UnassignerStatsDirFmt()

    cmd = ["unassign", str(seqs), "--output_dir", str(unassigner_output.path)]
    run_command(cmd)

    return unassigner_output
