"""
Playwright環境の動作確認テスト
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_playwright_can_open_browser(page: Page):
    """
    Playwrightがブラウザを起動できるか確認
    """
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")


@pytest.mark.ui
def test_local_streamlit_is_running(page: Page):
    """
    ローカルのStreamlitアプリにアクセスできるか確認
    """
    page.goto("http://localhost:8501")
    
    # ページタイトルが存在することを確認
    expect(page).to_have_title("目指せ！みのるんマスター！")
