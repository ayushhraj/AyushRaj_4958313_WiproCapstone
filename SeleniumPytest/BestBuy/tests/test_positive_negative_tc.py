import allure

from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils


@allure.feature("BestBuy Positive and Negative Testing")
class TestPositiveNegativeTC:

    # ===== POSITIVE TEST CASE 1 =====
    # VALIDATE TOP DEALS NAVIGATION
    @allure.story("Navigation Testing")
    def test_top_deals_navigation(self, setup):

        driver = setup

        home = HomePage(driver)

        home.click_top_deals()

        assert "top-deals" in driver.current_url


    # ===== POSITIVE TEST CASE 2 =====
    # VALIDATE TV & HOME THEATER PAGE
    @allure.story("TV Navigation Testing")
    def test_tv_home_theater_navigation(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)

        home.click_top_deals()

        deals.click_tv_home_theater()

        assert "tv" in driver.current_url.lower()


    # ===== POSITIVE TEST CASE 3 =====
    # VALIDATE BRAND FILTERS
    @allure.story("Brand Filter Testing")
    def test_brand_filters(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_brand_filters()

        assert driver.find_element(
            *tv.samsung_checkbox
        ).is_displayed()

        assert (
            driver.find_element(
                *tv.lg_checkbox
            ).is_displayed()
        )

        assert (
            driver.find_element(
                *tv.sony_checkbox
            ).is_displayed()
        )


    # ===== POSITIVE TEST CASE 4 =====
    # VALIDATE PRICE FILTERS
    @allure.story("Price Filter Testing")
    def test_price_filters(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        min_price, max_price = (
            ExcelUtils.get_price_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_price_filters(
            min_price,
            max_price,
            "valid_price_filter"
        )

        assert (
                f"Price%7E{min_price}+to+{max_price}"
                in driver.current_url
        )

        assert min_price < max_price

    # ===== POSITIVE TEST CASE 5 =====
    # INCREASE PRODUCT QUANTITY IN THE CART PG
    import pytest
    @allure.feature("BestBuy Positive Test")
    @allure.story("Increase Product Quantity In Cart")
    #@pytest.mark.positive
    def test_increase_product_quantity(self, setup):
        driver = setup

        home = HomePage(driver)
        top_deals = TopDealsPage(driver)
        tv_page = TVProductsPage(driver)
        cart_page = CartPage(driver)

        home.click_top_deals()

        top_deals.click_tv_home_theater()

        tv_page.apply_brand_filters()

        tv_page.apply_price_filters(
            100,
            500,
            "valid_price_filter"
        )

        tv_page.add_first_two_products()

        tv_page.click_go_to_cart()

        updated_quantity = (
            cart_page.increase_product_quantity("2")
        )

        assert updated_quantity == "2", (
            f"Expected quantity 2 "
            f"but got {updated_quantity}"
        )
    ###############################################################################################


    # ===== NEGATIVE TEST CASE 1 =====
    # VALIDATE INVALID PRICE RANGE
    @allure.story("Invalid Price Validation")
    def test_invalid_price_filter(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        min_price, max_price = (
            ExcelUtils.get_invalid_price_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_price_filters(
            min_price,
            max_price,
            "invalid_price_filter"
        )

        assert min_price > max_price

        assert "currentprice_facet" in driver.current_url


    # ===== NEGATIVE TEST CASE 2 =====
    # VALIDATE INVALID BRAND SEARCH
    @allure.story("Invalid Brand Validation")
    def test_invalid_brand_filter(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        invalid_brand = (
            ExcelUtils.get_invalid_brand_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_invalid_brand_filter(
            invalid_brand
        )

        #assert invalid_brand is not None
        assert invalid_brand == "ABCXYZ"

        assert (
            driver.find_element(
                *tv.brand_search_box
            ).is_displayed()
        )


    # ===== NEGATIVE TEST CASE 3 =====
    # VALIDATE INVALID EMAIL DURING CHECKOUT
    @allure.story("Invalid Email Validation")
    def test_invalid_email_checkout(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)
        cart = CartPage(driver)

        invalid_email = (
            ExcelUtils.get_invalid_email_data()
        )

        min_price, max_price = (
            ExcelUtils.get_price_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_brand_filters()

        tv.apply_price_filters(
            min_price,
            max_price,
            "valid_price_filter"
        )

        tv.add_first_two_products()

        tv.click_go_to_cart()

        cart.click_checkout()

        cart.enter_invalid_email(
            invalid_email
        )

        assert "@" not in invalid_email

        assert (
            driver.find_element(
                *cart.email_input
            ).is_displayed()
        )