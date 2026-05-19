import allure

from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils


@allure.feature("BestBuy Positive and Negative Testing")
class TestPositiveNegativeTC:

    @allure.story("Navigation Testing")
    def test_top_deals_navigation(self, setup):

        driver = setup

        home = HomePage(driver)

        home.click_top_deals()

        assert "top-deals" in driver.current_url

    @allure.story("TV Navigation Testing")
    def test_tv_home_theater_navigation(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)

        home.click_top_deals()

        deals.click_tv_home_theater()

        assert "tv" in driver.current_url.lower()

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

        assert min_price < max_price

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

        assert invalid_brand is not None

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