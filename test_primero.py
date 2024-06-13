from playwright.sync_api import Page
import pytest
import random
from decouple import config

@pytest.mark.order(2)
def test_foo(page: Page):
    assert True

