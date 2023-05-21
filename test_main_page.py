from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
link1 = "http://selenium1py.pythonanywhere.com/"
link2 = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link1)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link1)
    page.open()
    page.should_be_login_link()


def test_guest_can_be_sure_its_login_page(browser):
    page = LoginPage(browser, link2)
    page.open()
    page.should_be_login_page()
