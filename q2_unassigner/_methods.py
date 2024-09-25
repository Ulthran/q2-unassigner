# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import subprocess as sp
import tempfile
from q2_types.feature_data import FeatureData, Sequence
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
    seqs: FeatureData[Sequence]
) -> UnassignerStatsDirFmt:
    print("Starting unassigner...")
    #unassigner_dir = Path("./q2_unassigner/")
    #unassigner_dir.mkdir(exist_ok=True)
    #unassigner_input = unassigner_dir / "input.fasta"
    #unassigner_output = unassigner_dir / "unassigner_output.tsv"
    unassigner_output_dir = UnassignerStatsDirFmt()
    unassigner_output_dir.mkdir(parents=True, exist_ok=True)
    unassigner_input = tempfile.NamedTemporaryFile()

    with open(unassigner_input, "w") as f:
        for seq in seqs.view(Sequence):
            f.write(f">{seq.metadata['id']}\n{str(seq)}\n")

    cmd = ["unassign", str(unassigner_input), "--output_dir", str(unassigner_output_dir)]
    run_command(cmd)

    print("Unassigner output saved at:", unassigner_output_dir)
    return unassigner_output_dir
