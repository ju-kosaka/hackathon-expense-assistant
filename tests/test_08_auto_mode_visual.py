"""
Auto Mode体験ページのビジュアルテスト（Playwright）

TDDメソッド: Red（失敗するテストを先に書く）
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_page_renders_successfully(page: Page):
    """
    ページが正常にレンダリングできるか
    """
    page.goto("http://localhost:8501/Auto_Mode体験")
    
    # ページタイトルが表示されるまで待つ
    title = page.locator("h1")
    expect(title).to_be_visible(timeout=15000)


@pytest.mark.ui
def test_main_header_has_gradient(page: Page):
    """
    メインヘッダーにグラデーション背景が適用されているか
    """
    page.goto("http://localhost:8501/Auto_Mode体験")
    
    # .main-header要素が存在するまで待つ
    main_header = page.locator(".main-header")
    expect(main_header).to_be_visible(timeout=15000)
    
    # 背景がグラデーションか確認（linear-gradientが含まれているか）
    background = main_header.evaluate("el => getComputedStyle(el).backgroundImage")
    assert "linear-gradient" in background or "gradient" in background, \
        f"グラデーション背景が適用されていません。実際: {background}"


@pytest.mark.ui
def test_top_button_exists_and_works(page: Page):
    """
    TOPボタンが存在し、クリックで遷移できるか
    """
    page.goto("http://localhost:8501/Auto_Mode体験")
    
    # TOPボタンが表示されるまで待つ（role="button"で特定）
    top_button = page.get_by_role("button", name="🏠 TOP")
    expect(top_button).to_be_visible(timeout=15000)
    
    # TOPボタンをクリック
    top_button.click()
    
    # TOPページに遷移したか確認
    page.wait_for_url("http://localhost:8501", timeout=5000)


@pytest.mark.ui
def test_footer_exists(page: Page):
    """
    フッターが存在するか
    """
    page.goto("http://localhost:8501/Auto_Mode体験")
    
    # ページ全体が読み込まれるまで少し待つ
    page.wait_for_timeout(3000)
    
    # フッターボタンを探す（ページの一番下までスクロール）
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)
    
    # フッターの「TOP」ボタンが存在するか確認
    footer_button = page.get_by_role("button").filter(has_text="TOP").last
    expect(footer_button).to_be_visible(timeout=15000)


@pytest.mark.ui
def test_sidebar_is_hidden(page: Page):
    """
    サイドバーが非表示になっているか
    """
    page.goto("http://localhost:8501/Auto_Mode体験")
    
    # ページが読み込まれるまで待つ
    page.wait_for_timeout(2000)
    
    # サイドバー要素が存在するか確認
    sidebar = page.locator('[data-testid="stSidebar"]')
    
    if sidebar.count() > 0:
        # サイドバーが存在する場合、display: noneになっているか確認
        is_visible = sidebar.is_visible()
        assert not is_visible, \
            "サイドバーが表示されています（display: noneになっていません）"


@pytest.mark.ui
@pytest.mark.slow
def test_page_screenshot(page: Page):
    """
    ページ全体のスクリーンショットを撮影（ビジュアルリグレッション用）
    """
    page.goto("http://localhost:8501/Auto_Mode体験")
    
    # ページ全体が読み込まれるまで待つ
    page.wait_for_selector("h1", timeout=15000)
    page.wait_for_timeout(2000)
    
    # スクリーンショットを保存
    page.screenshot(path="tests/snapshots/08_auto_mode_page.png", full_page=True)
    
    # ファイルが生成されたことを確認
    from pathlib import Path
    snapshot_path = Path("tests/snapshots/08_auto_mode_page.png")
    assert snapshot_path.exists(), \
        "スクリーンショットが保存されませんでした"
