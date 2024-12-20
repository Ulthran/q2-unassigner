# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat
from q2_unassigner._format import UnassignerStatsDirFmt
from unassigner.command import main as unassign_command


def unassign(
    seqs: DNAFASTAFormat,
    type_strain_fasta: str = None,
    db_dir: str = None,
    threshold: float = None,
    ref_mismatch_positions: str = None,
    num_cpus: int = None,
    soft_threshold: bool = None,
    verbose: bool = None,
) -> UnassignerStatsDirFmt:
    print("Starting unassigner...")
    unassigner_output = UnassignerStatsDirFmt()

    cmd = [str(seqs), "--output_dir", str(unassigner_output.path)]

    # Would love a more concise way to do this
    # but I can't think of any other method for
    # preserving the package's inbuilt defaults
    cmd += (
        ["--type_strain_fasta", type_strain_fasta] if type_strain_fasta else []
    )
    cmd += ["--db_dir", db_dir] if db_dir else []
    cmd += ["--threshold", str(threshold)] if threshold else []
    cmd += (
        ["--ref_mismatch_positions", ref_mismatch_positions]
        if ref_mismatch_positions
        else []
    )
    cmd += ["--num_cpus", str(num_cpus)] if num_cpus else []
    cmd += ["--soft_threshold"] if soft_threshold else []
    cmd += ["--verbose"] if verbose else []

    print(f"Running command: {str(cmd)}")
    unassign_command(cmd)
    print(f"Unassigner finished. Results in {str(unassigner_output.path)}")

    return unassigner_output
