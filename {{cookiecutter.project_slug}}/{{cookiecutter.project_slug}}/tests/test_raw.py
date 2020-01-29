#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple example of a test file using a function.
NOTE: All test file names must have one of the two forms.
- `test_<XYY>.py`
- '<XYZ>_test.py'

Docs: https://docs.pytest.org/en/latest/
      https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery
"""

import pytest
from {{cookiecutter.project_slug}}.steps import Raw


# This test just checks to see if the raw step instantiates and runs
def test_raw_run():
    raw = Raw(N=10)
    raw.run()
    assert len(raw.manifest == 10)
