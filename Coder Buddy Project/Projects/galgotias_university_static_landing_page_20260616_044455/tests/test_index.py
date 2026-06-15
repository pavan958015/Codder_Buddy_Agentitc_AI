import pytest
from bs4 import BeautifulSoup

# Assuming index.html is in the root directory for testing purposes
HTML_FILE = "index.html"

def read_html(filepath):
    """Reads and returns the content of an HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail(f"HTML file not found at {filepath}. Please ensure index.html exists.")

def get_soup(html_content):
    """Returns a BeautifulSoup object from HTML content."""
    return BeautifulSoup(html_content, 'html.parser')

@pytest.fixture
def soup():
    """Fixture to provide a BeautifulSoup object for testing."""
    html_content = read_html(HTML_FILE)
    return get_soup(html_content)

def test_index_has_required_semantic_tags(soup):
    """Tests if the index.html contains essential semantic tags."""
    # Check for main structure elements
    assert soup.find('header', class_='site-header') is not None, "Missing <header> tag with class 'site-header'"
    assert soup.find('main', id='main-content') is not None, "Missing <main> tag with id 'main-content'"
    assert soup.find('footer', class_='site-footer') is not None, "Missing <footer> tag with class 'site-footer'"

def test_index_has_required_css_classes(soup):
    """Tests if the index.html contains required CSS classes."""
    # Check for specific structural classes
    assert soup.find('body', class_='container') is not None, "Body tag missing class 'container'"
    assert soup.find('nav', id='primary-nav') is not None, "Navigation tag missing ID 'primary-nav'"

def test_index_has_title(soup):
    """Tests if the HTML document has a <title> tag."""
    title = soup.find('title')
    assert title is not None, "HTML document is missing a <title> tag."
    # Optional: Check if the title is not empty
    assert len(title.string) > 0, "The <title> tag content is empty."

def test_index_structure_is_valid():
    """A basic check to ensure parsing doesn't fail unexpectedly."""
    try:
        soup = get_soup(read_html(HTML_FILE))
        # This test passes if the file can be parsed without raising an error.
        assert True
    except Exception as e:
        pytest.fail(f"Parsing index.html failed with error: {e}")