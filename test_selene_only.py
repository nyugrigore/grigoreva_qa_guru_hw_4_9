from selene import browser, by, be


def test_github():
    browser.open("https://github.com/")
    browser.element(".header-search-input").click
    browser.element(".header-search-input").type("eroshenkoam/allure-example").press_enter()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#76")).should(be.visible)
