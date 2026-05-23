import allure

from behave import *

from pages.home_page import HomePage
from pages.top_deals_page import TopDealsPage
from pages.tv_products_page import TVProductsPage
from pages.cart_page import CartPage

from utilities.excel_utils import ExcelUtils
from utilities.logger import LogGenerator


logger = LogGenerator.loggen()


# ==========================================================
# LAUNCH WEBSITE
# ==========================================================
@given("User launches BestBuy website")
def step_launch(context):

    logger.info("STEP : INITIALIZING PAGE OBJECTS")

    context.home = HomePage(
        context.driver
    )

    context.deals = TopDealsPage(
        context.driver
    )

    context.tv = TVProductsPage(
        context.driver
    )

    context.cart = CartPage(
        context.driver
    )

    logger.info(
        "ALL PAGE OBJECTS INITIALIZED SUCCESSFULLY"
    )

    allure.attach(
        context.driver.get_screenshot_as_png(),
        name="HomePage_Loaded",
        attachment_type=allure.attachment_type.PNG
    )


# ==========================================================
# TOP DEALS
# ==========================================================
@when("User opens Top Deals section")
def step_top_deals(context):

    logger.info(
        "STEP : OPENING TOP DEALS SECTION"
    )

    context.home.click_top_deals()

    logger.info(
        "TOP DEALS PAGE OPENED SUCCESSFULLY"
    )


# ==========================================================
# TV SECTION
# ==========================================================
@when("User opens TV & Home Theater section")
def step_tv_section(context):

    logger.info(
        "STEP : OPENING TV SECTION"
    )

    context.deals.click_tv_home_theater()

    logger.info(
        "TV SECTION OPENED SUCCESSFULLY"
    )


# ==========================================================
# BRAND FILTERS
# ==========================================================
@when("User applies brand filters")
def step_brand_filters(context):

    logger.info(
        "STEP : APPLYING BRAND FILTERS"
    )

    brands = ExcelUtils.get_brand_data()

    context.tv.apply_brand_filters(
        brands
    )

    logger.info(
        "BRAND FILTERS APPLIED SUCCESSFULLY"
    )


# ==========================================================
# PRICE FILTERS
# ==========================================================
@when("User applies valid price filters")
def step_price_filters(context):

    logger.info(
        "STEP : APPLYING PRICE FILTERS"
    )

    min_price, max_price = (
        ExcelUtils.get_price_data()
    )

    context.tv.apply_price_filters(
        min_price,
        max_price,
        "valid_price_filter"
    )

    logger.info(
        "VALID PRICE FILTER APPLIED SUCCESSFULLY"
    )


# ==========================================================
# ADD PRODUCTS
# ==========================================================
@when("User adds first two products to cart")
def step_add_products(context):

    logger.info(
        "STEP : ADDING PRODUCTS TO CART"
    )

    context.tv.add_first_two_products()

    logger.info(
        "PRODUCTS ADDED TO CART SUCCESSFULLY"
    )


# ==========================================================
# GO TO CART
# ==========================================================
@when("User navigates to cart page")
def step_cart(context):

    logger.info(
        "STEP : NAVIGATING TO CART PAGE"
    )

    context.tv.click_go_to_cart()

    logger.info(
        "CART PAGE OPENED SUCCESSFULLY"
    )


# ==========================================================
# CHECKOUT
# ==========================================================
@when("User proceeds to checkout")
def step_checkout(context):

    logger.info(
        "STEP : PROCEEDING TO CHECKOUT"
    )

    context.cart.click_checkout()

    logger.info(
        "CHECKOUT PAGE OPENED SUCCESSFULLY"
    )


# ==========================================================
# FINAL VALIDATION
# ==========================================================
@then("Checkout page should open successfully")
def step_checkout_validation(context):

    logger.info(
        "ASSERTION : VALIDATING CHECKOUT PAGE"
    )

    assert (
        "checkout"
        in context.driver.current_url.lower()
        or
        "signin"
        in context.driver.current_url.lower()
        or
        "identity"
        in context.driver.current_url.lower()
    )

    logger.info(
        "ASSERTION PASSED : CHECKOUT PAGE VALIDATED"
    )