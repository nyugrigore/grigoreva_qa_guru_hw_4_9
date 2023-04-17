import allure
from selene import browser, by, be


def test_github():
    with allure.step("Открываем главную странице GitHub"):
        browser.open("https://github.com/")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-input").click
        browser.element(".header-search-input").type("eroshenkoam/allure-example").press_enter()

    with allure.step("Открываем репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем tab Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с #76"):
        browser.element(by.partial_text("#76")).should(be.visible)
