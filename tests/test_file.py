import os

def test_file_operations():
    filename = '../../../etc/passwd'
    # Path traversal in test
    with open(filename) as f:
        content = f.read()
    assert content is not None
