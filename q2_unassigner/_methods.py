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
    type_strain_fasta: str = None,
    threshold: float = None,
    ref_mismatch_positions: str = None,
    num_cpus: int = None,
    soft_threshold: bool = None,
    verbose: bool = None,
) -> UnassignerStatsDirFmt:
    print("Starting unassigner...")
    unassigner_output = UnassignerStatsDirFmt()

    cmd = ["unassign", str(seqs), "--output_dir", str(unassigner_output.path)]

    # Would love a more concise way to do this
    # but I can't think of any other method for preserving the package's inbuilt defaults
    if type_strain_fasta:
        cmd.extend(["--type_strain_fasta", type_strain_fasta])
    if threshold:
        cmd.extend(["--threshold", str(threshold)])
    if ref_mismatch_positions:
        cmd.extend(["--ref_mismatch_positions", ref_mismatch_positions])
    if num_cpus:
        cmd.extend(["--num_cpus", str(num_cpus)])
    if soft_threshold:
        cmd.append("--soft_threshold")
    if verbose:
        cmd.append("--verbose")

    run_command(cmd)

    return unassigner_output
