import os
import pytest
from pyfilemeta.metadata import get_file_metadata

@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "testfile.txt"
    file.write_text("This is a test file.")
    return str(file)

def test_get_file_metadata(sample_file):
    metadata = get_file_metadata(sample_file)
    assert metadata["file_name"] == "testfile.txt"
    assert metadata["size_bytes"] > 0
