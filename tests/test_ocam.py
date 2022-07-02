import pytest
from ocam.core import get_version

def test_get_version():
    assert get_version() == "0.0.1"
