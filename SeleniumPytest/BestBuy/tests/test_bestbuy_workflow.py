from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils


class TestBestBuyWorkflow:

    def test_complete_workflow(self, setup):

        driver = setup

        # PAGE OBJECTS
        home = HomePage(driver)

        deals = TopDealsPage(driver)

        tv = TVProductsPage(driver)

        cart = CartPage(driver)

        # EXCEL DATA
        # samsung, lg, sony = (
        #     ExcelUtils.get_brand_data()
        # )

        min_price, max_price = (
            ExcelUtils.get_price_data()
        )

        # TEST FLOW
        home.click_top_deals()

        deals.click_tv_home_theater()

        # BRAND FILTERS
        tv.apply_brand_filters()

        # PRICE FILTERS
        tv.apply_price_filters(
            min_price,
            max_price
        )

        # ADD PRODUCTS
        tv.add_first_two_products()

        # CART
        tv.click_go_to_cart()

        # CHECKOUT
        cart.click_checkout()