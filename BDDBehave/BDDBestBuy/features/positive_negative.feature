Feature: BestBuy Positive and Negative Test Cases


  # ==========================================================
  # POSITIVE TEST CASES
  # ==========================================================

  Scenario: [POS_TC_01] Validate Top Deals Navigation

    Given User launches BestBuy website
    When User opens Top Deals section
    Then Top Deals page should open successfully


  Scenario: [POS_TC_02] Validate TV Navigation

    Given User launches BestBuy website
    When User opens Top Deals section
    And User opens TV & Home Theater section
    Then TV section should open successfully


  Scenario: [POS_TC_03] Validate Brand Filters

    Given User launches BestBuy website
    When User opens Top Deals section
    And User opens TV & Home Theater section
    And User applies brand filters
    Then Brand filters should apply successfully


  Scenario: [POS_TC_04] Validate Price Filters

    Given User launches BestBuy website
    When User opens Top Deals section
    And User opens TV & Home Theater section
    And User applies valid price filters
    Then Price filters should apply successfully


  Scenario: [POS_TC_05] Validate Product Quantity Update

    Given User launches BestBuy website
    When User opens Top Deals section
    And User opens TV & Home Theater section
    And User applies brand filters
    And User applies valid price filters
    And User adds first two products to cart
    And User navigates to cart page
    And User increases product quantity
    Then Product quantity should update successfully


  # ==========================================================
  # NEGATIVE TEST CASES
  # ==========================================================

  Scenario: [NEG_TC_01] Validate Invalid Price Filter

    Given User launches BestBuy website
    When User opens Top Deals section
    And User opens TV & Home Theater section
    And User applies invalid price filters
    Then Invalid price validation should display


  Scenario: [NEG_TC_02] Validate Invalid Brand Filter

    Given User launches BestBuy website
    When User opens Top Deals section
    And User opens TV & Home Theater section
    And User applies invalid brand filter
    Then Invalid brand validation should display


  Scenario: [NEG_TC_03] Validate Invalid Email Checkout

    Given User launches BestBuy website
    When User opens Top Deals section
    And User opens TV & Home Theater section
    And User applies brand filters
    And User applies valid price filters
    And User adds first two products to cart
    And User navigates to cart page
    And User proceeds to checkout
    And User enters invalid email
    Then Invalid email validation should display