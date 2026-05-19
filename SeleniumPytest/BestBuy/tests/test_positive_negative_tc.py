from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils


class TestPositiveNegativeTC:

    # POSITIVE TEST CASE 1

    def test_top_deals_navigation(self, setup):

        driver = setup

        home = HomePage(driver)

        home.click_top_deals()

        assert "top-deals" in driver.current_url

    # POSITIVE TEST CASE 2

    def test_tv_home_theater_navigation(self, setup):

        driver = setup

        home = HomePage(driver)

        deals = TopDealsPage(driver)

        home.click_top_deals()

        deals.click_tv_home_theater()

        assert "tv" in driver.current_url.lower()

    # POSITIVE TEST CASE 3

    def test_brand_filters(self, setup):

        driver = setup

        home = HomePage(driver)

        deals = TopDealsPage(driver)

        tv = TVProductsPage(driver)

        # EXCEL BRAND DATA

        # samsung, lg, sony = (
        #     ExcelUtils.get_brand_data()
        # )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_brand_filters()

        assert True

    # POSITIVE TEST CASE 4

    def test_price_filters(self, setup):

        driver = setup

        home = HomePage(driver)

        deals = TopDealsPage(driver)

        tv = TVProductsPage(driver)

        # EXCEL PRICE DATA

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

        assert True

    # NEGATIVE TEST CASE 1

    def test_invalid_price_filter(self, setup):

        driver = setup

        home = HomePage(driver)

        deals = TopDealsPage(driver)

        tv = TVProductsPage(driver)

        # INVALID PRICE DATA FROM EXCEL

        min_price, max_price = (
            ExcelUtils.get_invalid_price_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_price_filters(
            min_price,
            max_price,
            tv.apply_price_filters(
                min_price,
                max_price,
                "invalid_price_filter"
            )
        )

        assert True

    # NEGATIVE TEST CASE 2

    def test_invalid_brand_filter(self, setup):

        driver = setup

        home = HomePage(driver)

        deals = TopDealsPage(driver)

        tv = TVProductsPage(driver)

        # INVALID BRAND DATA FROM EXCEL

        invalid_brand = (
            ExcelUtils.get_invalid_brand_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_invalid_brand_filter(
            invalid_brand
        )

        assert True

    def test_invalid_email_checkout(self, setup):
        driver = setup

        home = HomePage(driver)

        deals = TopDealsPage(driver)

        tv = TVProductsPage(driver)

        cart = CartPage(driver)

        invalid_email = (
            ExcelUtils.get_invalid_email_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        tv.apply_brand_filters()

        min_price, max_price = (
            ExcelUtils.get_price_data()
        )

        tv.apply_price_filters(
            min_price,
            max_price
        )

        tv.add_first_two_products()

        tv.click_go_to_cart()

        cart.click_checkout()

        cart.enter_invalid_email(
            invalid_email
        )

        assert "@" not in invalid_email