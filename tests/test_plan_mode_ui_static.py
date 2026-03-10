"""
Plan modeカスタマイズページの静的解析テスト
今回の修正: ファイル配置場所のUIデザイン改善（黒背景）

TDDメソッド: Red（失敗するテストを先に書く）
"""
import pytest
from pathlib import Path


@pytest.mark.static
def test_file_structure_css_style_exists():
    """
    .file-structure CSSクラスが定義されているか
    
    期待する動作:
    - background-color: #1e1e1e （黒背景）
    - color: #d4d4d4 （明るいグレーのテキスト）
    - font-family: 'Courier New' （等幅フォント）
    - border: 1px solid #3c3c3c （ダークグレーのボーダー）
    """
    file_path = Path("pages/05_📋_Plan modeカスタマイズ.py")
    content = file_path.read_text(encoding='utf-8')
    
    # CSSクラス .file-structure が存在するか
    assert ".file-structure" in content, \
        "CSSクラス .file-structure が見つかりません"
    
    # 黒背景が設定されているか
    assert "background-color: #1e1e1e" in content, \
        "黒背景（#1e1e1e）が設定されていません"
    
    # テキストカラーが設定されているか
    assert "color: #d4d4d4" in content, \
        "テキストカラー（#d4d4d4）が設定されていません"
    
    # 等幅フォントが設定されているか
    assert "font-family: 'Courier New'" in content, \
        "等幅フォント（Courier New）が設定されていません"
    
    # ボーダーが設定されているか
    assert "border: 1px solid #3c3c3c" in content, \
        "ボーダー（#3c3c3c）が設定されていません"


@pytest.mark.static
def test_file_structure_html_applied():
    """
    ファイル配置場所のHTMLに .file-structure クラスが適用されているか
    
    期待する動作:
    - <div class="file-structure"> が存在する
    - "プロジェクトルート/" の説明が含まれている
    - ".claude/" ディレクトリの説明が含まれている
    """
    file_path = Path("pages/05_📋_Plan modeカスタマイズ.py")
    content = file_path.read_text(encoding='utf-8')
    
    # HTMLに .file-structure クラスが適用されているか
    assert '<div class="file-structure">' in content, \
        "HTMLに .file-structure クラスが適用されていません"
    
    # ファイル構造の説明が含まれているか
    assert "プロジェクトルート/" in content, \
        "ファイル構造の説明（プロジェクトルート/）が見つかりません"
    
    assert ".claude/" in content, \
        ".claude/ ディレクトリの説明が見つかりません"
    
    assert "plan_output_style.md" in content, \
        "plan_output_style.md の説明が見つかりません"


@pytest.mark.static
def test_old_step_box_not_used_for_file_structure():
    """
    ファイル配置場所に古い .step-box が使われていないか
    （リグレッション防止テスト）
    
    期待する動作:
    - "📁 ファイル配置場所" の後に .step-box が使われていない
    - 代わりに .file-structure が使われている
    """
    file_path = Path("pages/05_📋_Plan modeカスタマイズ.py")
    content = file_path.read_text(encoding='utf-8')
    
    lines = content.split('\n')
    
    # "📁 ファイル配置場所" を探す
    file_structure_section_found = False
    for i, line in enumerate(lines):
        if "📁 ファイル配置場所" in line:
            file_structure_section_found = True
            
            # 次の10行以内に .step-box がないことを確認
            next_lines = '\n'.join(lines[i:i+10])
            
            assert '<div class="step-box">' not in next_lines, \
                "ファイル配置場所に古い .step-box が使われています（修正前のコードに戻っています）"
            
            # 代わりに .file-structure が使われていることを確認
            assert '<div class="file-structure">' in next_lines, \
                "ファイル配置場所に .file-structure が使われていません"
            
            break
    
    assert file_structure_section_found, \
        "「📁 ファイル配置場所」のセクションが見つかりません"


@pytest.mark.static
def test_file_structure_heading_is_separate():
    """
    ファイル配置場所の見出しが .file-structure の外に出ているか
    
    期待する動作:
    - "#### 📁 ファイル配置場所" が st.markdown() で独立している
    - .file-structure div の中に <h4> が含まれていない
    """
    file_path = Path("pages/05_📋_Plan modeカスタマイズ.py")
    content = file_path.read_text(encoding='utf-8')
    
    # "#### 📁 ファイル配置場所" が st.markdown() で独立しているか
    assert 'st.markdown("#### 📁 ファイル配置場所")' in content, \
        "見出しが st.markdown() で独立していません"
    
    # .file-structure div の中に <h4> が含まれていないか確認
    lines = content.split('\n')
    inside_file_structure = False
    
    for line in lines:
        if '<div class="file-structure">' in line:
            inside_file_structure = True
        elif '</div>' in line and inside_file_structure:
            inside_file_structure = False
        elif inside_file_structure and '<h4>' in line:
            pytest.fail(".file-structure div の中に <h4> が含まれています（見出しが独立していません）")
