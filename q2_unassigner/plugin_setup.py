# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Citations, Plugin
from q2_types.feature_data import DNAFastaFormat
from q2_types.feature_table import FeatureTable, Frequency
from q2_unassigner import __version__
from q2_unassigner._methods import unassign

citations = Citations.load("citations.bib", package="q2_unassigner")

plugin = Plugin(
    name="unassigner",
    version=__version__,
    website="https://github.com/PennChopMicrobiomeProgram/unassigner",
    package="q2_unassigner",
    description="Evaluate consistency with named bacterial species for short 16S rRNA marker gene sequences",
    short_description="Unassigner",
    citations=[citations['Tanes2024Unassigner']]
)

plugin.methods.register_function(
    function=unassign,
    inputs={'seqs': FeatureTable[Frequency]},
    parameters={'output_fp': str},
    outputs=[('unassigned', FeatureTable[Frequency])],
    input_descriptions={'seqs': 'The sequences to unassign.'},
    parameter_descriptions={'output_fp': 'The output directory.'},
    output_descriptions={'unassigned': 'The unasigned sequences.'},
    name='Unassign sequences',
    description=("Run unassigner on input sequences."),
    citations=[]
)
