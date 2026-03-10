"""
Auto Mode体験ページの静的解析テスト

TDDメソッド: Red（失敗するテストを先に書く）
"""
import pytest
from pathlib import Path


@pytest.mark.static
def test_page_file_exists():
    """
    ページファイルが存在するか
    """
    file_path = Path("pages/08_🤖_Auto Mode体験.py")
    assert file_path.exists(), \
        "ページファイル 08_🤖_Auto Mode体験.py が見つかりません"


@pytest.mark.static
def test_render_functions_imported():
    """
    render_top_button と render_footer がimportされているか
    """
    file_path = Path("pages/08_🤖_Auto Mode体験.py")
    content = file_path.read_text(encoding='utf-8')
    
    assert "from components import render_top_button, render_footer" in content, \
        "render_top_button と render_footer がimportされていません"
    
    assert "render_top_button()" in content, \
        "render_top_button() が呼び出されていません"
    
    assert "render_footer()" in content, \
        "render_footer() が呼び出されていません"


@pytest.mark.static
def test_main_header_style_exists():
    """
    メインヘッダーのCSSスタイルが定義されているか
    """
    file_path = Path("pages/08_🤖_Auto Mode体験.py")
    content = file_path.read_text(encoding='utf-8')
    
    assert ".main-header" in content, \
        "CSSクラス .main-header が見つかりません"
    
    assert "background: linear-gradient" in content, \
        "グラデーション背景が設定されていません"


@pytest.mark.static
def test_sidebar_hidden():
    """
    サイドバー非表示のCSSが設定されているか
    """
    file_path = Path("pages/08_🤖_Auto Mode体験.py")
    content = file_path.read_text(encoding='utf-8')
    
    assert '[data-testid="stSidebar"]' in content, \
        "サイドバー非表示のCSSが設定されていません"
    
    assert "display: none" in content, \
        "サイドバーを非表示にする display: none が見つかりません"


@pytest.mark.static
def test_page_config_set():
    """
    st.set_page_config が設定されているか
    """
    file_path = Path("pages/08_🤖_Auto Mode体験.py")
    content = file_path.read_text(encoding='utf-8')
    
    assert "st.set_page_config(" in content, \
        "st.set_page_config() が設定されていません"
    
    assert 'page_title=' in content, \
        "page_title が設定されていません"
    
    assert 'page_icon=' in content, \
        "page_icon が設定されていません"


@pytest.mark.static
def test_content_about_auto_mode():
    """
    Auto Modeに関する説明が含まれているか
    """
    file_path = Path("pages/08_🤖_Auto Mode体験.py")
    content = file_path.read_text(encoding='utf-8')
    
    # Auto Mode関連のキーワードがあるか確認
    keywords = ["auto", "Auto", "オート", "自動", "承認"]
    
    found_keywords = [kw for kw in keywords if kw in content]
    
    assert len(found_keywords) > 0, \
        f"Auto Modeに関するキーワードが見つかりません。検索したキーワード: {keywords}"
