import allure

from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils


@allure.feature("BestBuy Ecommerce Workflow")
@allure.story("Complete TV Purchase Flow")
class TestBestBuyWorkflow:

    @allure.title("Complete End-to-End BestBuy Workflow")
    @allure.description(
        "Validate TV filtering, cart and checkout workflow"
    )
    def test_complete_workflow(self, setup):

        driver = setup

        home = HomePage(driver)
        deals = TopDealsPage(driver)
        tv = TVProductsPage(driver)
        cart = CartPage(driver)

        min_price, max_price = (
            ExcelUtils.get_price_data()
        )

        # ===== TOP DEALS =====
        home.click_top_deals()
        assert "top-deals" in driver.current_url.lower()


        # ===== TV & HOME THEATER =====
        deals.click_tv_home_theater()
        assert "tv" in driver.current_url.lower()


        # ===== BRAND FILTERS =====
        tv.apply_brand_filters()
        assert driver.find_element(
            *tv.samsung_checkbox
        ).is_displayed()


        # ===== PRICE FILTERS =====
        tv.apply_price_filters(
            min_price,
            max_price,
            "valid_price_filter"
        )
        assert min_price < max_price


        # ===== ADD PRODUCTS =====
        tv.add_first_two_products()
        assert driver.find_element(
            *tv.go_to_cart
        ).is_displayed()


        # ===== GO TO CART =====
        tv.click_go_to_cart()
        assert "cart" in driver.current_url.lower()


        # ===== CHECKOUT =====
        cart.click_checkout()
        assert driver.find_element(
            *cart.email_input
        ).is_displayed()