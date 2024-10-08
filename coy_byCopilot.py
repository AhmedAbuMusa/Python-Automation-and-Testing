from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

# Initialize the WebDriver (Edge in this case)
driver = webdriver.Edge()

# Navigate to the target webpage
driver.get("https://www.selenium.dev/")

# Example 1: Interacting with the navigation menu
try:
    # Wait for the navigation menu to become visible
    nav_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.main-nav"))
    )

    # Click on the "Docs" link
    docs_link = nav_menu.find_element(By.LINK_TEXT, "Docs")
    docs_link.click()

    # Wait for the "Docs" page to load
    WebDriverWait(driver, 10).until(
        EC.url_contains("https://www.selenium.dev/documentation/")
    )

    # Assert that the URL contains "documentation"
    assert "documentation" in driver.current_url

except Exception as e:
    print(f"Error interacting with navigation menu: {e}")

# Example 2: Interacting with the search bar
try:
    # Wait for the search bar to become visible
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#search-input"))
    )

    # Enter a search term
    search_bar.send_keys("Selenium WebDriver")

    # Submit the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.search-results"))
    )

    # Assert that the search results page is loaded
    assert "Search Results" in driver.title

except Exception as e:
    print(f"Error interacting with search bar: {e}")

# Example 3: Interacting with a blog post
try:
    # Wait for a blog post title to become visible
    blog_post_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.post-title a"))
    )

    # Click on the blog post title
    blog_post_title.click()

    # Wait for the blog post page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "article.post"))
    )

    # Assert that the blog post page is loaded
    assert "Blog" in driver.title

except Exception as e:
    print(f"Error interacting with blog post: {e}")

# Add assertions to verify expected outcomes after each interaction

# Close the browser window
driver.quit()
