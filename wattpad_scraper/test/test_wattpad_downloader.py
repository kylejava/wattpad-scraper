import pytest
from wattpad_scraper import Wattpad

EXAMPLE_URL = "https://www.wattpad.com/story/48217861-ruins-harry-potter-1"

class TestWattpadDownloader:

  def test_book_exists(self):
    wattpad = Wattpad()
    book = wattpad.get_book_by_url(EXAMPLE_URL)
    assert book is not None

  def test_harry_in_tags(self):
    wattpad = Wattpad()
    book = wattpad.get_book_by_url(EXAMPLE_URL)
    assert "harry" in book.tags

  def test_find_correct_author(self):
    wattpad = Wattpad()
    book = wattpad.get_book_by_url(EXAMPLE_URL)
    assert book.author.name == "haIfblood"

  def test_get_num_of_votes(self):
      wattpad = Wattpad()
      book = wattpad.get_book_by_url(EXAMPLE_URL)
      assert book.votes == 184110

if __name__ == "__main__":
  pytest.main()
