Feature: BestBuy End To End Workflow


  Scenario: [E2E_TC] Complete TV Purchase Workflow

    Given User launches BestBuy website

    When User opens Top Deals section

    And User opens TV & Home Theater section

    And User applies brand filters

    And User applies valid price filters

    And User adds first two products to cart

    And User navigates to cart page

    And User proceeds to checkout

    Then Checkout page should open successfully