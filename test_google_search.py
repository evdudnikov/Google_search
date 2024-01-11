import pytest
from selene import browser, be, have


@pytest.fixture
def config_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield
    browser.quit()

def test_selene(config_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative_search(config_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('shlkjhslkjfkslgdsksodjfoisjdoifjs').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу shlkjhslkjfkslgdsksodjfoisjdoifjs ничего не найдено.'))