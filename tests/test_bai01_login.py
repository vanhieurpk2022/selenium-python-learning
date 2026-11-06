import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ===== EXAMPLE (giảng viên làm sẵn) =====
@pytest.mark.login
def test_login_thanh_cong_standard_user(login_page):
    driver = login_page
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()

    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']"))
    )
    items = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")

    assert title.text == "Products", f"Tiêu đề sai: {title.text!r}"
    assert len(items) == 6, f"Mong đợi 6 sản phẩm, thực tế {len(items)}"


# ===== BÀI TẬP (học viên tự làm) =====
# TODO Bài 1.1: locked_out_user
# TODO Bài 1.2: sai mật khẩu
# TODO Bài 1.3: bỏ trống username
# TODO Bài 1.4: bỏ trống password
# TODO Bài 1.5: parametrize 4 user hợp lệ
# TODO Bài 1.6 (nâng cao): logout
# TODO Bài 1.7 (nâng cao): vào inventory khi chưa login
