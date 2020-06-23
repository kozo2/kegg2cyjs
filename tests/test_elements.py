import pytest

from kegg2cyjs import *

def test_nodes():
    assert len(kegg2cyjs("eco00020")["nodes"]) ==10
