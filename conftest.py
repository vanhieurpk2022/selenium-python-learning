"""Fixture dùng chung cho toàn bộ dự án (Selenium + pytest)."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.saucedemo.com/"


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        "--headless", action="store_true", default=False,
        help="Chạy Chrome ở chế độ headless (không hiện cửa sổ)",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
def driver(request):
    """Khởi tạo Chrome, trả về cho test, rồi đóng sau khi test xong."""
    options = Options()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver, base_url):
    """Mở sẵn trang login của Swag Labs, trả về driver."""
    driver.get(base_url)
    return driver
