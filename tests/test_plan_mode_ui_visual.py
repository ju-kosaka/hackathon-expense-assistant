"""
Plan modeカスタマイズページのビジュアルテスト（Playwright）
今回の修正: ファイル配置場所のUIデザイン改善（黒背景）

TDDメソッド: Red（失敗するテストを先に書く）
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_file_structure_section_has_black_background(page: Page):
    """
    ファイル配置場所のセクションが黒背景で表示されているか
    
    期待する動作:
    - .file-structure 要素が存在する
    - 背景色が #1e1e1e（黒）である
    - テキスト色が #d4d4d4（明るいグレー）である
    """
    page.goto("http://localhost:8501/Plan_modeカスタマイズ")
    
    # .file-structure 要素が表示されるまで待つ
    file_structure = page.locator(".file-structure")
    expect(file_structure).to_be_visible(timeout=15000)
    
    # 背景色が黒（#1e1e1e = rgb(30, 30, 30)）か確認
    bg_color = file_structure.evaluate("el => getComputedStyle(el).backgroundColor")
    assert bg_color == "rgb(30, 30, 30)", \
        f"背景色が正しくありません。期待: rgb(30, 30, 30), 実際: {bg_color}"
    
    # テキスト色が明るいグレー（#d4d4d4 = rgb(212, 212, 212)）か確認
    text_color = file_structure.evaluate("el => getComputedStyle(el).color")
    assert text_color == "rgb(212, 212, 212)", \
        f"テキスト色が正しくありません。期待: rgb(212, 212, 212), 実際: {text_color}"


@pytest.mark.ui
def test_file_structure_uses_monospace_font(page: Page):
    """
    ファイル配置場所が等幅フォントで表示されているか
    
    期待する動作:
    - font-family に 'Courier New' が含まれている
    """
    page.goto("http://localhost:8501/Plan_modeカスタマイズ")
    
    # .file-structure 要素を取得
    file_structure = page.locator(".file-structure")
    expect(file_structure).to_be_visible(timeout=15000)
    
    # フォントファミリーに 'Courier New' が含まれているか確認
    font_family = file_structure.evaluate("el => getComputedStyle(el).fontFamily")
    assert "Courier New" in font_family, \
        f"等幅フォント（Courier New）が設定されていません。実際: {font_family}"


@pytest.mark.ui
def test_file_structure_has_border(page: Page):
    """
    ファイル配置場所にボーダーが表示されているか
    
    期待する動作:
    - border が 1px solid #3c3c3c である
    """
    page.goto("http://localhost:8501/Plan_modeカスタマイズ")
    
    # .file-structure 要素を取得
    file_structure = page.locator(".file-structure")
    expect(file_structure).to_be_visible(timeout=15000)
    
    # ボーダースタイルを確認
    border_width = file_structure.evaluate("el => getComputedStyle(el).borderWidth")
    border_style = file_structure.evaluate("el => getComputedStyle(el).borderStyle")
    border_color = file_structure.evaluate("el => getComputedStyle(el).borderColor")
    
    assert border_width == "1px", \
        f"ボーダー幅が正しくありません。期待: 1px, 実際: {border_width}"
    
    assert border_style == "solid", \
        f"ボーダースタイルが正しくありません。期待: solid, 実際: {border_style}"
    
    # #3c3c3c = rgb(60, 60, 60)
    assert border_color == "rgb(60, 60, 60)", \
        f"ボーダー色が正しくありません。期待: rgb(60, 60, 60), 実際: {border_color}"


@pytest.mark.ui
def test_file_structure_content_is_visible(page: Page):
    """
    ファイル配置場所の内容が正しく表示されているか
    
    期待する動作:
    - "プロジェクトルート/" のテキストが表示されている
    - ".claude/" のテキストが表示されている
    - "plan_output_style.md" のテキストが表示されている
    """
    page.goto("http://localhost:8501/Plan_modeカスタマイズ")
    
    # .file-structure 要素を取得
    file_structure = page.locator(".file-structure")
    expect(file_structure).to_be_visible(timeout=15000)
    
    # 内容を確認
    content = file_structure.inner_text()
    
    assert "プロジェクトルート/" in content, \
        "「プロジェクトルート/」のテキストが見つかりません"
    
    assert ".claude/" in content, \
        "「.claude/」のテキストが見つかりません"
    
    assert "plan_output_style.md" in content, \
        "「plan_output_style.md」のテキストが見つかりません"


@pytest.mark.ui
def test_file_structure_heading_is_separate(page: Page):
    """
    ファイル配置場所の見出しが .file-structure の外に出ているか
    （黒背景の中に見出しが含まれていないことを確認）
    
    期待する動作:
    - "📁 ファイル配置場所" が .file-structure の外にある
    """
    page.goto("http://localhost:8501/Plan_modeカスタマイズ")
    
    # .file-structure 要素を待つ
    file_structure = page.locator(".file-structure")
    expect(file_structure).to_be_visible(timeout=15000)
    
    # .file-structure 要素の内容を取得
    content = file_structure.inner_text()
    
    # 見出しが含まれていないことを確認
    assert "📁 ファイル配置場所" not in content, \
        "見出しが .file-structure の中に含まれています（独立していません）"


@pytest.mark.ui
@pytest.mark.slow
def test_file_structure_visual_regression(page: Page):
    """
    ファイル配置場所のビジュアルリグレッションテスト
    （スクリーンショットを撮って、見た目の変化を検出）
    
    期待する動作:
    - .file-structure 要素のスクリーンショットを保存
    """
    page.goto("http://localhost:8501/Plan_modeカスタマイズ")
    
    # .file-structure 要素のスクリーンショットを撮る
    file_structure = page.locator(".file-structure")
    expect(file_structure).to_be_visible(timeout=15000)
    
    # スクリーンショットを保存
    file_structure.screenshot(path="tests/snapshots/file-structure.png")
    
    # ファイルが生成されたことを確認
    from pathlib import Path
    snapshot_path = Path("tests/snapshots/file-structure.png")
    assert snapshot_path.exists(), \
        "スクリーンショットが保存されませんでした"
