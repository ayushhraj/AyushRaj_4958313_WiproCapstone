import allure

from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils
from utilities.logger import LogGenerator


@allure.feature("BestBuy Positive and Negative Testing")
class TestPositiveNegativeTC:

    logger = LogGenerator.loggen()

    # ===== POSITIVE TEST CASE 1 =====
    # VALIDATE TOP DEALS NAVIGATION
    @allure.story("Navigation Testing")
    def test_top_deals_navigation(self, setup):
        self.logger.info("==================================================")
        self.logger.info("POSITIVE TEST CASE 1 : VALIDATE TOP DEALS NAVIGATION")
        self.logger.info("==================================================")

        driver = setup

        home = HomePage(driver)

        self.logger.info("STEP 1 : Opening Top Deals Page")
        home.click_top_deals()

        self.logger.info("ASSERTION : Validating Top Deals URL")
        assert "top-deals" in driver.current_url

        self.logger.info("ASSERTION PASSED : Top Deals Page Opened Successfully")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")


    # ===== POSITIVE TEST CASE 2 =====
    # VALIDATE TV & HOME THEATER PAGE
    @allure.story("TV Navigation Testing")
    def test_tv_home_theater_navigation(self, setup):
        self.logger.info("==================================================")
        self.logger.info("POSITIVE TEST CASE 2 : VALIDATE TV & HOME THEATER PAGE")
        self.logger.info("==================================================")

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)

        self.logger.info("STEP 1 : Opening Top Deals")
        home.click_top_deals()

        self.logger.info("STEP 2 : Opening TV & Home Theater Page")
        deals.click_tv_home_theater()

        self.logger.info("ASSERTION : Validating TV Page Navigation")
        assert "tv" in driver.current_url.lower()

        self.logger.info("ASSERTION PASSED : TV Page Opened Successfully")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")


    # ===== POSITIVE TEST CASE 3 =====
    # VALIDATE BRAND FILTERS
    @allure.story("Brand Filter Testing")
    def test_brand_filters(self, setup):
        self.logger.info("==================================================")
        self.logger.info("POSITIVE TEST CASE 3 : VALID BRAND FILTER")
        self.logger.info("==================================================")

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        self.logger.info("STEP 1 : Opening Top Deals")
        home.click_top_deals()

        self.logger.info("STEP 2 : Opening TV Section")
        deals.click_tv_home_theater()

        self.logger.info("STEP 3 : Applying Brand Filters")

        brands = ExcelUtils.get_brand_data()

        tv.apply_brand_filters(brands)

        self.logger.info("ASSERTION : Validating Applied Brand Filters")
        for brand in brands:
            assert (
                    brand.lower() in driver.page_source.lower()
            )

            self.logger.info(
                f"ASSERTION PASSED : {brand} filter applied successfully"
            )


        self.logger.info("ASSERTION PASSED : Brand Filters Applied Successfully")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")

    # ===== POSITIVE TEST CASE 4 =====
    # VALIDATE PRICE FILTERS
    @allure.story("Price Filter Testing")
    def test_price_filters(self, setup):
        self.logger.info("==================================================")
        self.logger.info("POSITIVE TEST CASE 4 : VALID PRICE FILTER")
        self.logger.info("==================================================")

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        min_price, max_price = (
            ExcelUtils.get_price_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        self.logger.info("STEP 1 : Applying Valid Price Filter")
        tv.apply_price_filters(
            min_price,
            max_price,
            "valid_price_filter"
        )

        self.logger.info("ASSERTION : Validating Price Filter in the URL")
        assert (
                f"Price%7E{min_price}+to+{max_price}"
                in driver.current_url
        )

        assert min_price < max_price

        self.logger.info("ASSERTION PASSED : Price Filter Applied Successfully")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")

    # ===== POSITIVE TEST CASE 5 =====
    # INCREASE PRODUCT QUANTITY IN THE CART PG
    import pytest
    @allure.feature("BestBuy Positive Test")
    @allure.story("Increase Product Quantity In Cart")
    #@pytest.mark.positive
    def test_increase_product_quantity(self, setup):
        self.logger.info("==================================================")
        self.logger.info("POSITIVE TEST CASE 5 : PRODUCT QUANTITY UPDATE")
        self.logger.info("==================================================")
        driver = setup

        home = HomePage(driver)
        top_deals = TopDealsPage(driver)
        tv_page = TVProductsPage(driver)
        cart_page = CartPage(driver)

        home.click_top_deals()

        top_deals.click_tv_home_theater()

        brands = ExcelUtils.get_brand_data()
        tv_page.apply_brand_filters(brands)

        tv_page.apply_price_filters(
            100,
            500,
            "valid_price_filter"
        )

        tv_page.add_first_two_products()

        tv_page.click_go_to_cart()

        self.logger.info("STEP 1 : Increasing Product Quantity")
        updated_quantity = (
            cart_page.increase_product_quantity("2")
        )

        self.logger.info("ASSERTION : Validating Updated Quantity")
        assert updated_quantity == "2", (
            f"Expected quantity 2 "
            f"but got {updated_quantity}"
        )

        # assert int(updated_quantity) > 1

        self.logger.info("ASSERTION PASSED : Quantity Updated Successfully")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")

    ###############################################################################################


    # ===== NEGATIVE TEST CASE 1 =====
    # VALIDATE INVALID PRICE RANGE
    @allure.story("Invalid Price Validation")
    @pytest.mark.parametrize(
        "min_price, max_price",
        ExcelUtils.get_invalid_price_data()
    )
    def test_invalid_price_filter(self, setup, min_price, max_price):
        self.logger.info("==================================================")
        self.logger.info("NEGATIVE TEST CASE 1 : INVALID PRICE FILTER")
        self.logger.info("==================================================")
        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        min_price, max_price = (
            ExcelUtils.get_invalid_price_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        self.logger.info("STEP 1 : Applying Invalid Price Filter")
        tv.apply_price_filters(
            min_price,
            max_price,
            "invalid_price_filter"
        )

        self.logger.info("ASSERTION : Validating Invalid Price Filter")
        # Case 1 : Website shows no products
        if "No results found" in driver.page_source:

            expected_messages = [
                "No results found",
                "Try removing one or more filters",
                "0 results"
            ]

            assert any(
                msg.lower() in driver.page_source.lower()
                for msg in expected_messages
            ), "No results validation failed"

            self.logger.info(
                "ASSERTION PASSED : No results validation successful"
            )

        # Case 2 : Website auto-normalizes invalid range
        else:

            normalized_min = min(
                int(min_price),
                int(max_price)
            )

            normalized_max = max(
                int(min_price),
                int(max_price)
            )

            assert (
                    f"{normalized_min}+to+{normalized_max}"
                    in driver.current_url
                    or
                    f"{normalized_min}%20to%20{normalized_max}"
                    in driver.current_url
            ), "Price normalization validation failed"

            self.logger.info(
                "ASSERTION PASSED : Price range normalized successfully"
            )

        self.logger.info("ASSERTION PASSED : Invalid Price Validation Successful")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")

    # ===== NEGATIVE TEST CASE 2 =====
    # VALIDATE INVALID BRAND SEARCH
    @allure.story("Invalid Brand Validation")
    def test_invalid_brand_filter(self, setup):
        self.logger.info("==================================================")
        self.logger.info("NEGATIVE TEST CASE 2 : INVALID BRAND FILTER")
        self.logger.info("==================================================")

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)

        invalid_brand = (
            ExcelUtils.get_invalid_brand_data()
        )

        home.click_top_deals()

        deals.click_tv_home_theater()

        self.logger.info("STEP 1 : Applying Invalid Brand Filter")
        tv.apply_invalid_brand_filter(
            invalid_brand
        )

        self.logger.info("ASSERTION : Validating Invalid Brand Handling")
        #assert invalid_brand is not None
        assert invalid_brand == "ABCXYZ"

        assert (
            driver.find_element(
                *tv.brand_search_box
            ).is_displayed()
        )
#need imprvmnt
        assert (
                "No Results"
                in driver.page_source
        ), "Invalid brand validation failed"

        self.logger.info("ASSERTION PASSED : Invalid Brand Validation Successful")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")

    # ===== NEGATIVE TEST CASE 3 =====
    # VALIDATE INVALID EMAIL DURING CHECKOUT
    @allure.story("Invalid Email Validation")
    def test_invalid_email_checkout(self, setup):
        self.logger.info("==================================================")
        self.logger.info("NEGATIVE TEST CASE 3 : INVALID EMAIL VALIDATION")
        self.logger.info("==================================================")

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

        brands = ExcelUtils.get_brand_data()
        tv.apply_brand_filters(brands)

        tv.apply_price_filters(
            min_price,
            max_price,
            "valid_price_filter"
        )

        tv.add_first_two_products()

        tv.click_go_to_cart()

        cart.click_checkout()

        self.logger.info("STEP 1 : Entering Invalid Email")
        cart.enter_invalid_email(
            invalid_email
        )

        self.logger.info("ASSERTION : Validating Invalid Email Error")
        assert "@" not in invalid_email

        assert (
            driver.find_element(
                *cart.email_input
            ).is_displayed()
        )

        expected_messages = [
            "isn't associated with an account",
            "try a different email address",
            "continue as guest"
        ]

        assert any(
            msg.lower() in driver.page_source.lower()
            for msg in expected_messages
        ), "Expected validation message not displayed for invalid email"

        self.logger.info("ASSERTION PASSED : Invalid Email Validation Successful")

        self.logger.info("==================================================")
        self.logger.info("TEST CASE PASSED")
        self.logger.info("==================================================")