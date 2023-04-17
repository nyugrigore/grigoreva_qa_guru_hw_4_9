import allure
from selene import browser, by, be
from allure_commons.types import Severity


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Issues")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com/", name="Testing")
def test_with_decorators():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    open_repository("eroshenkoam/allure-example")
    search_for_issue()
    open_issue("76")


@allure.step("Открываем главную странице GitHub")
def open_main_page():
    browser.open("https://github.com/")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-input").click
    browser.element(".header-search-input").type(repo).press_enter()


@allure.step("Открываем репозиторий {repo}")
def open_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем tab Issues")
def search_for_issue():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue #{issue}")
def open_issue(issue):
    browser.element(by.partial_text(f"#{issue}")).should(be.visible)
