from playwright.sync_api import Page
import pytest
import random
from decouple import config

@pytest.mark.order(1)
def test_segundo(page: Page):
    pass