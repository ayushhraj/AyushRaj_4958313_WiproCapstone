import allure

from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils
from utilities.logger import LogGenerator


@allure.feature("BestBuy Ecommerce Workflow")
@allure.story("Complete TV Purchase Flow")
class TestBestBuyWorkflow:

    logger = LogGenerator.loggen()

    @allure.title("Complete End-to-End BestBuy Workflow")
    @allure.description(
        "Validate TV filtering, cart and checkout workflow"
    )
    def test_complete_workflow(self, setup):

        driver = setup
        self.logger.info("==================================================")
        self.logger.info("END TO END TEST : BESTBUY COMPLETE WORKFLOW")
        self.logger.info("==================================================")

        assert (
                "bestbuy.com" in driver.current_url.lower()
        ), "User is not navigated to BestBuy website"
        self.logger.info("ASSERTION PASSED : BestBuy website loaded successfully")

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)
        cart = CartPage(driver)

        min_price, max_price = (
            ExcelUtils.get_price_data()
        )

        # ===== TOP DEALS =====
        self.logger.info("STEP 1 : Opening Top Deals Page")
        home.click_top_deals()
        assert "top-deals" in driver.current_url.lower()
        self.logger.info("ASSERTION PASSED : Top Deals page opened successfully")


        # ===== TV & HOME THEATER =====
        self.logger.info("STEP 2 : Opening TV & Home Theater Section")
        deals.click_tv_home_theater()
        assert "tv" in driver.current_url.lower()
        self.logger.info("ASSERTION PASSED : TV section opened successfully")


        # ===== BRAND FILTERS =====
        self.logger.info("STEP 3 : Applying Brand Filters")
        brands = ExcelUtils.get_brand_data()

        tv.apply_brand_filters(brands)

        for brand in brands:
            assert (
                    brand.lower() in driver.page_source.lower()
            )

            self.logger.info(
                f"ASSERTION PASSED : {brand} filter applied successfully"
            )

        # ===== PRICE FILTERS =====
        self.logger.info("STEP 4 : Applying Price Filter")
        tv.apply_price_filters(
            min_price,
            max_price,
            "valid_price_filter"
        )
        assert min_price < max_price
        assert ("0+to+250" in driver.current_url), "Price filter not applied correctly"
        self.logger.info("ASSERTION PASSED : Price filter applied successfully")

        # ===== ADD PRODUCTS =====
        self.logger.info("STEP 5 : Adding Products To Cart")
        tv.add_first_two_products()
        assert driver.find_element(
            *tv.go_to_cart
        ).is_displayed()
        self.logger.info("ASSERTION PASSED : Products added to cart successfully")

        # ===== GO TO CART =====
        self.logger.info("STEP 6 : Navigating To Cart")
        tv.click_go_to_cart()
        assert "cart" in driver.current_url.lower(), "User not redirected to cart"
        self.logger.info("ASSERTION PASSED : Cart page opened successfully")


        # ===== CHECKOUT =====
        self.logger.info("STEP 7 : Proceeding To Checkout")
        cart.click_checkout()
        assert (
                "checkout" in driver.current_url.lower()
                or "signin" in driver.current_url.lower()
                or "identity" in driver.current_url.lower()
        ), "Checkout page not opened"

        assert driver.find_element(
            *cart.email_input
        ).is_displayed()
        self.logger.info("ASSERTION PASSED : Checkout page opened successfully")

        self.logger.info("==================================================")
        self.logger.info("END TO END TEST CASE PASSED")
        self.logger.info("==================================================")