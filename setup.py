# ----------------------------------------------------------------------------
# Copyright (c) 2024, Charlie Bushman.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = "A template QIIME 2 plugin."

setup(
    name="q2-unassigner",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="Charlie Bushman",
    author_email="ctbushman@gmail.com",
    description=description,
    url="https://github.com/PennChopMicrobiomeProgram/unassigner",
    entry_points={
        "qiime2.plugins": [
            "q2_unassigner=" "q2_unassigner" ".plugin_setup:plugin"
        ]  # noqa: E501
    },
    package_data={
        "q2_unassigner": ["citations.bib"],
        "q2_unassigner.tests": ["data/*"],
    },
    zip_safe=False,
    install_requires=[
        "unassigner",
    ]
)
