import pytest

from kegg2cyjs import *

def test_elements():
    elements = kegg2cyjs("eco00020")
    assert len(elements["nodes"]) == 70
    assert len(elements["edges"]) == 66
