import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.smoke
def test_trang_login_mo_duoc(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    login_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']"))
    )

    assert driver.title == "Swag Labs", f"Title sai, thực tế: {driver.title!r}"
    assert login_button.is_displayed(), "Nút Login phải hiển thị"

@pytest.mark.smoke
def test_input_userName_password(driver,base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver,10)

    username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#user-name")))
    password_input = wait.until( EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
    assert username_input.is_displayed(), "Ô username không hiển thị"
    assert password_input.is_displayed(), "Ô password không hiển thị"