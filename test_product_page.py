from pages.product_page import ProductPage
import pytest
import time


# @pytest.mark.parametrize('promo_offer', [pytest.param(i,
# marks=pytest.mark.xfail(i == "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                         reason="bug"))
#                                          for i in range(1)])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket_button()
#     page.should_be_search_field()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     time.sleep(10)
#     page.find_text_has_been_added_to_basket()
#
#
# @pytest.mark.xfail(reason="test has to fail")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail(reason="test has to fail")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.success_message_disappeared()
#
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
