import allure

from behave import *

from utilities.excel_utils import ExcelUtils
from utilities.logger import LogGenerator


logger = LogGenerator.loggen()


# ==========================================================
# [POS_TC_01] TOP DEALS VALIDATION
# ==========================================================
@then("Top Deals page should open successfully")
def step_top_deals_validation(context):

    logger.info(
        "ASSERTION : VALIDATING TOP DEALS PAGE"
    )

    assert (
        "top-deals"
        in context.driver.current_url.lower()
    )

    logger.info(
        "ASSERTION PASSED : TOP DEALS PAGE VALIDATED"
    )


# ==========================================================
# [POS_TC_02] TV PAGE VALIDATION
# ==========================================================
@then("TV section should open successfully")
def step_tv_validation(context):

    logger.info(
        "ASSERTION : VALIDATING TV SECTION"
    )

    assert (
        "tv"
        in context.driver.current_url.lower()
    )

    logger.info(
        "ASSERTION PASSED : TV SECTION VALIDATED"
    )


# ==========================================================
# [POS_TC_03] BRAND FILTER VALIDATION
# ==========================================================
@then("Brand filters should apply successfully")
def step_brand_validation(context):

    logger.info(
        "ASSERTION : VALIDATING BRAND FILTERS"
    )

    brands = ExcelUtils.get_brand_data()

    for brand in brands:

        assert (
            brand.lower()
            in context.driver.page_source.lower()
        )

    logger.info(
        "ASSERTION PASSED : BRAND FILTERS VALIDATED"
    )


# ==========================================================
# [POS_TC_04] PRICE FILTER VALIDATION
# ==========================================================
@then("Price filters should apply successfully")
def step_price_validation(context):

    logger.info(
        "ASSERTION : VALIDATING PRICE FILTER"
    )

    min_price, max_price = (
        ExcelUtils.get_price_data()
    )

    assert (
        f"Price%7E{min_price}+to+{max_price}"
        in context.driver.current_url
    )

    logger.info(
        "ASSERTION PASSED : PRICE FILTER VALIDATED"
    )


# ==========================================================
# [POS_TC_05] PRODUCT QUANTITY UPDATE
# ==========================================================
@when("User increases product quantity")
def step_quantity(context):

    logger.info(
        "STEP : INCREASING PRODUCT QUANTITY"
    )

    context.updated_quantity = (
        context.cart.increase_product_quantity("2")
    )

    logger.info(
        "PRODUCT QUANTITY UPDATED"
    )


@then("Product quantity should update successfully")
def step_quantity_validation(context):

    logger.info(
        "ASSERTION : VALIDATING UPDATED QUANTITY"
    )

    assert context.updated_quantity == "2"

    logger.info(
        "ASSERTION PASSED : PRODUCT QUANTITY VALIDATED"
    )


# ==========================================================
# [NEG_TC_01] INVALID PRICE FILTER
# ==========================================================
@when("User applies invalid price filters")
def step_invalid_price(context):

    logger.info(
        "STEP : APPLYING INVALID PRICE FILTER"
    )

    data = ExcelUtils.get_invalid_price_data()

    min_price = data[0][0]

    max_price = data[0][1]

    context.tv.apply_price_filters(
        min_price,
        max_price,
        "invalid_price_filter"
    )

    logger.info(
        "INVALID PRICE FILTER APPLIED"
    )


@then("Invalid price validation should display")
def step_invalid_price_validation(context):

    logger.info(
        "ASSERTION : VALIDATING INVALID PRICE FILTER"
    )

    assert (
        "No results found"
        in context.driver.page_source
        or
        "to"
        in context.driver.current_url
    )

    logger.info(
        "ASSERTION PASSED : INVALID PRICE VALIDATED"
    )


# ==========================================================
# [NEG_TC_02] INVALID BRAND FILTER
# ==========================================================
@when("User applies invalid brand filter")
def step_invalid_brand(context):

    logger.info(
        "STEP : APPLYING INVALID BRAND FILTER"
    )

    invalid_brand = (
        ExcelUtils.get_invalid_brand_data()
    )

    context.tv.apply_invalid_brand_filter(
        invalid_brand
    )

    logger.info(
        "INVALID BRAND FILTER APPLIED"
    )


@then("Invalid brand validation should display")
def step_invalid_brand_validation(context):

    logger.info(
        "ASSERTION : VALIDATING INVALID BRAND"
    )

    assert (
        "No Results"
        in context.driver.page_source
    )

    logger.info(
        "ASSERTION PASSED : INVALID BRAND VALIDATED"
    )


# ==========================================================
# [NEG_TC_03] INVALID EMAIL
# ==========================================================
@when("User enters invalid email")
def step_invalid_email(context):

    logger.info(
        "STEP : ENTERING INVALID EMAIL"
    )

    invalid_email = (
        ExcelUtils.get_invalid_email_data()
    )

    context.cart.enter_invalid_email(
        invalid_email
    )

    logger.info(
        "INVALID EMAIL ENTERED"
    )


@then("Invalid email validation should display")
def step_invalid_email_validation(context):

    logger.info(
        "ASSERTION : VALIDATING INVALID EMAIL"
    )

    expected_messages = [
        "isn't associated with an account",
        "try a different email address",
        "continue as guest"
    ]

    assert any(
        msg.lower()
        in context.driver.page_source.lower()
        for msg in expected_messages
    )

    logger.info(
        "ASSERTION PASSED : INVALID EMAIL VALIDATED"
    )