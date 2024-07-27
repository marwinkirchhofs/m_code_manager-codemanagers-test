#!/usr/bin/env python3

# PYTHON PROJECT_CREATE
#
# Create a python project from the template in this directory

import code_manager

LANG_IDENTIFIERS = ["test"]


class TestCodeManager(code_manager.CodeManager):

    def __init__(self):
        super().__init__("test")

    PLACEHOLDERS = {
    }
