from playwright.sync_api import Page, expect
import time

url = "https://automationexercise.com/"
product_name = "Men Tshirt"
tshirt_count = 2
quantity = "4"

def test_product_search(page:Page):
    # Navigate to website
    page.goto(url)
    # Verify the home page is visible
    expect(page).to_have_title("Automation Exercise")
    expect(page.get_by_alt_text("Website for automation practice")).to_be_visible()
    # Click on "Products" button
    page.locator("a", has_text="Products").click()
    # Verify ALL PRODUCTS page loaded successfully
    expect(page).to_have_title("Automation Exercise - All Products")
    expect(page.locator("h2", has_text="All Products")).to_be_visible()
    # Enter product name
    page.locator("#search_product").fill(product_name)
    page.locator("#submit_search").click()
    # Verify "Searched Products" is visible
    expect(page.locator("h2", has_text="Searched Products")).to_be_visible()
    # Verify all the products related to search is visible
    product_count = page.locator("p", has_text=product_name).count()
    assert product_count == tshirt_count, f"Expected {tshirt_count}, but found {product_count}"


def test_cart(page:Page):
    # Navigate to website
    page.goto(url)
    # Verify the home page is visible
    expect(page).to_have_title("Automation Exercise")
    expect(page.get_by_alt_text("Website for automation practice")).to_be_visible()
    # Click "View Product" of the first product
    page.locator("a", has_text="View Product").nth(0).click()
    # Verify product detail page is opened
    expect(page).to_have_title("Automation Exercise - Product Details")
    expect(page.locator("button", has_text="Add to cart")).to_be_visible()
    # Increase the quantity to 4
    page.locator("#quantity").clear()
    page.locator("#quantity").fill(quantity)
    # Click "Add to cart" button
    page.locator("button", has_text="Add to cart").click()
    # Click "View Cart" link
    page.locator("a", has_text="View Cart").click()
    # Get the quantity count
    quantity_count = page.locator(".cart_quantity button").text_content()
    assert quantity_count == quantity, f"Expected {quantity}, but found {quantity_count}"
