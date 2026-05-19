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