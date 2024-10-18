# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_unassigner._format import UnassignerStatsDirFmt, UnassignerStatsFmt
from q2_unassigner._type import UnassignerStats
from qiime2.plugin import Bool, Citations, Float, Int, Plugin, Range, Str
from q2_types.feature_data import FeatureData, Sequence
from q2_unassigner import __version__
from q2_unassigner._methods import unassign

citations = Citations.load("citations.bib", package="q2_unassigner")

plugin = Plugin(
    name="unassigner",
    version=__version__,
    website="https://github.com/PennChopMicrobiomeProgram/unassigner",
    package="q2_unassigner",
    description=(
        "Evaluate consistency with named bacterial species ",
        "for short 16S rRNA marker gene sequences",
    ),
    short_description="Run unassigner with QIIME2",
    citations=[citations["Tanes2024Unassigner"]],
)

plugin.register_semantic_types(UnassignerStats)
plugin.register_formats(UnassignerStatsFmt, UnassignerStatsDirFmt)
plugin.register_artifact_class(
    UnassignerStats,
    UnassignerStatsDirFmt,
    description="Unassigner stats output.",
)

plugin.methods.register_function(
    function=unassign,
    inputs={"seqs": FeatureData[Sequence]},
    parameters={
        "type_strain_fasta": Str,
        "threshold": Float
        % Range(0, 1, inclusive_start=True, inclusive_end=True),
        "ref_mismatch_positions": Str,
        "num_cpus": Int % Range(1, None),
        "soft_threshold": Bool,
        "verbose": Bool,
    },
    outputs=[("unassigned", UnassignerStats)],
    input_descriptions={"seqs": "The sequences to unassign."},
    parameter_descriptions={
        "type_strain_fasta": (
            "Type strain sequences FASTA file. "
            "If the default file is not found, sequences are downloaded "
            "and re-formatted automatically."
        ),
        "threshold": (
            "Sequence identity threshold for ruling out species-level "
            "compatibility. Default value is 0.975 for the standard "
            "algorithm and 0.991 for the soft threshold algorithm."
        ),
        "ref_mismatch_positions": (
            "File of mismatch positions in reference database. The file may "
            "be compressed in gzip format."
        ),
        "num_cpus": (
            "Number of CPUs to use during sequence aligment (default: "
            "use all the CPUs)"
        ),
        "soft_threshold": "Use soft threshold algorithm.",
        "verbose": "Print verbose output.",
    },
    output_descriptions={
        "unassigned": "The unassigned sequences information."
    },
    name="Unassign sequences",
    description="Run unassigner on input sequences.",
    citations=[],
)
