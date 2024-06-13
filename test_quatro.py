from playwright.sync_api import Page
import pytest
import random
from decouple import config

@pytest.mark.order(4)
def test_ee(page: Page):
    pass