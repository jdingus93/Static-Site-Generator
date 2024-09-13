import pytest
from markdown_blocks import extract_title

def test_extract_title_valid_header():
    markdown = "# This is a title\nSome content here"
    assert extract_title(markdown) == "This is a title"

def test_extract_title_no_header():
    markdown = "This is some content without a header"
    with pytest.raises(ValueError, match="No h1 header"):
        extract_title(markdown)

def test_extract_title_not_at_beginning():
    markdown = "Some content before the header\n# This is the title"
    with pytest.raises(ValueError, match="Title is not at beginning"):
        extract_title(markdown)


def test_extract_title_multiple_headers():
    markdown = "# This is the first title\n# This is the second title"
    with pytest.raises(ValueError, match="Multiple h1 headers found"):
        extract_title(markdown)

def test_extract_title_empty_string():
    markdown = ""
    with pytest.raises(ValueError, match="Empty string"):
        extract_title(markdown)

def test_extract_title_empty_title():
    markdown = "# "
    with pytest.raises(ValueError, match="Empty header"):
        extract_title(markdown)