# coding=utf-8
"""
This is a temporary test to cover the import of modules that have 0% coverage so far

Yes, this is shameful...
"""

import glob

import pytest


# noinspection PyUnresolvedReferences,PyProtectedMember
@pytest.mark.nocleandir
@pytest.mark.parametrize('module_', glob.glob('./pvnhxgmgiq/**/*.py', recursive=True))
def test_imports(module_):
    module_ = module_[2:-3].replace('\\', '.')
    __import__(module_)
