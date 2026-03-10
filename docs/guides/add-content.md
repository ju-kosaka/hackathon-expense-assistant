# 📝 新しい学習コンテンツの追加ガイド

このファイルは、「目指せ！みのるんマスター！」に新しい学習コンテンツを追加する際の手順をまとめたものです。

**2つの方法があります:**
1. **自動生成スクリプト（推奨）**: `scripts/add_new_content.py` を使用
2. **手動作成**: このガイドに従って手動で作成

---

## 🤖 方法1: 自動生成スクリプトを使う（推奨）

### 1. 環境変数の設定（任意）

Claude APIを使ってブログ記事から自動生成したい場合は、環境変数を設定してください：

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

※ APIキーがない場合は、手動入力モードで使用できます。

### 2. スクリプトの実行

```bash
python scripts/add_new_content.py
```

### 3. 対話形式で情報を入力

スクリプトが以下の情報を順番に聞いてきます：

1. **ブログ記事のURL**（省略可）
   - URLを入力すると、Claude APIが記事を要約してチュートリアルを生成します
   - 省略した場合は、手動で学習内容を入力します

2. **タイトル** - 例: `プレゼン資料を爆速で作る`
3. **アイコン（絵文字）** - 例: `📊`
4. **説明文** - 例: `Marpを使ってMarkdownからスライドを生成する体験`
5. **所要時間** - 例: `20分`
6. **難易度（1-3）** - 1: ⭐（初級）, 2: ⭐⭐（中級）, 3: ⭐⭐⭐（上級）

### 4. スクリプトが自動実行する処理

1. ✅ 次のコンテンツIDを自動計算（例: 05）
2. ✅ Claude APIでチュートリアルページを生成
3. ✅ `pages/05_📊_プレゼン資料を爆速で作る.py` を作成
4. ✅ `render_top_button()` と `render_footer()` を自動追加
5. ✅ `contents.yaml` にメタデータを追加
6. ✅ TOPページから自動的にリンクされる（YAMLベースのため）

### 5. 動作確認とデプロイ

```bash
# ローカルで確認
streamlit run app.py

# Gitにコミット＆プッシュ
git add pages/XX_絵文字_タイトル.py contents.yaml
git commit -m "Add: 新しい学習コンテンツを追加"
git push
```

### トラブルシューティング

**APIキーが設定されていない**
```
⚠️  ANTHROPIC_API_KEY が設定されていません。
```
→ 手動入力モードで続行できます。学習内容の詳細を直接入力してください。

**YAMLファイルが見つからない**
```
❌ contents.yaml が見つかりません
```
→ スクリプトはプロジェクトのルートディレクトリで実行してください。

---

## ✍️ 方法2: 手動で作成する

自動生成スクリプトを使わず、手動でコンテンツを追加する手順です。

### ステップ1: contents.yamlにエントリを追加

`contents.yaml` に新しいコンテンツ情報を追加します。

```yaml
- id: "05"
  title: "新しいコンテンツのタイトル"
  description: "何を学べるかの説明（2-3行）"
  duration: "XX分"
  difficulty: 2  # 1: ⭐, 2: ⭐⭐, 3: ⭐⭐⭐
  page: "05_🎨_ページ名"
  icon: "🎨"
```

**ポイント:**
- `id`: ユニークなID（例: "05", "06"）
- `page`: ファイル名から `.py` を除いたもの（例: `05_🎨_ページ名` → `pages/05_🎨_ページ名.py`）
- `icon`: 絵文字を1つ選ぶ

---

### ステップ2: pages/配下に新しいファイルを作成

`pages/` フォルダに新しいPythonファイルを作成します。

**ファイル名の形式:**
```
XX_絵文字_ページ名.py
```

例:
- `05_🎨_デザイン実践.py`
- `06_🚀_デプロイ体験.py`

---

### ステップ3: ページの基本構造を実装

以下のテンプレートをコピーして、新しいページを作成します。

```python
import streamlit as st
from components import render_top_button, render_footer

st.set_page_config(
    page_title="ページタイトル",
    page_icon="🎨",
    layout="wide"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .main-header {
        background: linear-gradient(135deg, #A78BFA 0%, #4A90E2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("""
<div class="main-header">
    <h1>🎨 ページタイトル</h1>
    <p>サブタイトル</p>
</div>
""", unsafe_allow_html=True)

# ここにコンテンツを追加

render_footer()
```

**必須要素:**
1. `from components import render_top_button, render_footer` のimport
2. サイドバー非表示のCSS（`[data-testid="stSidebar"]`）
3. `render_top_button()` の呼び出し（ヘッダーの前）
4. `render_footer()` の呼び出し（ページの最後）

**ナビゲーション:**
- **右上**: `render_top_button()` - ページの途中でもすぐにTOPへ戻れる
- **フッター**: `render_footer()` - ページを読み終わった後にTOPへ戻れる

---

### ステップ4: ローカルで動作確認

```bash
streamlit run app.py
```

**確認項目:**
- [ ] トップページに新しいカードが表示される
- [ ] カードをクリックすると新しいページに遷移する
- [ ] 新しいページに「🏠 TOP」ボタンが表示される（右上）
- [ ] ページ下部にフッター（「🏠 TOPに戻る」ボタン付き）が表示される
- [ ] 右上のTOPボタンをクリックするとトップページに戻る
- [ ] フッターのTOPボタンをクリックするとトップページに戻る
- [ ] サイドバーが非表示になっている

---

### ステップ5: テストを書く（TDDメソッド - 重要！）

**⚠️ 重要な開発ルール:**
- **実装前にテストを書く**（Red → Green → Refactor）
- テストを書かずに実装してはいけない

#### テストの種類

1. **静的解析テスト** - CSSスタイル・HTML構造の検証
2. **ビジュアルテスト** - Playwrightで実際のブラウザでの見た目を検証

#### テストファイルの作成

**ファイル名の形式:**
```
tests/test_XX_page_name_static.py  # 静的解析テスト
tests/test_XX_page_name_visual.py  # ビジュアルテスト
```

例:
```
tests/test_05_design_practice_static.py
tests/test_05_design_practice_visual.py
```

#### 静的解析テストの例

```python
"""
デザイン実践ページの静的解析テスト
"""
import pytest
from pathlib import Path


@pytest.mark.static
def test_main_header_style_exists():
    """
    メインヘッダーのCSSスタイルが定義されているか
    """
    file_path = Path("pages/05_🎨_デザイン実践.py")
    content = file_path.read_text(encoding='utf-8')
    
    assert ".main-header" in content, \
        "CSSクラス .main-header が見つかりません"
    
    assert "background: linear-gradient" in content, \
        "グラデーション背景が設定されていません"


@pytest.mark.static
def test_render_functions_imported():
    """
    render_top_button と render_footer がimportされているか
    """
    file_path = Path("pages/05_🎨_デザイン実践.py")
    content = file_path.read_text(encoding='utf-8')
    
    assert "from components import render_top_button, render_footer" in content, \
        "render_top_button と render_footer がimportされていません"
    
    assert "render_top_button()" in content, \
        "render_top_button() が呼び出されていません"
    
    assert "render_footer()" in content, \
        "render_footer() が呼び出されていません"
```

#### ビジュアルテストの例

```python
"""
デザイン実践ページのビジュアルテスト（Playwright）
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_page_renders_successfully(page: Page):
    """
    ページが正常にレンダリングできるか
    """
    page.goto("http://localhost:8501/デザイン実践")
    
    # ページタイトルが表示されるまで待つ
    page.wait_for_selector("h1", timeout=15000)
    
    # ページタイトルが存在するか確認
    title = page.locator("h1")
    expect(title).to_be_visible()


@pytest.mark.ui
def test_top_button_navigation(page: Page):
    """
    TOPボタンが正しく動作するか
    """
    page.goto("http://localhost:8501/デザイン実践")
    
    # TOPボタンをクリック
    top_button = page.get_by_text("🏠 TOP")
    expect(top_button).to_be_visible(timeout=15000)
    top_button.click()
    
    # TOPページに遷移したか確認
    page.wait_for_url("http://localhost:8501", timeout=5000)
```

#### TDDサイクルの実践

1. **🔴 Red（失敗するテストを書く）**
   ```bash
   # 実装前にテストを実行（失敗することを確認）
   pytest tests/test_05_design_practice_static.py -v
   ```

2. **🟢 Green（テストを通す最小限の実装）**
   ```bash
   # ページを実装
   # 再度テストを実行（成功することを確認）
   pytest tests/test_05_design_practice_static.py -v
   ```

3. **🔵 Refactor（リファクタリング）**
   - コードの改善（テストが通ることを確認しながら）

#### テスト実行コマンド

```bash
# 静的解析テストのみ実行
pytest tests/ -m static -v

# ビジュアルテストのみ実行
pytest tests/ -m ui -v

# 全テスト実行
pytest tests/ -v

# 特定のファイルのみ実行
pytest tests/test_05_design_practice_static.py -v
```

---

### ステップ6: GitHubにpush

```bash
git add pages/XX_絵文字_ページ名.py contents.yaml tests/
git commit -m "Add new learning content: XXX with tests"
git push origin main
```

Streamlit Community Cloudが自動的に新しいバージョンをデプロイします（1-2分）。

---

## 🎨 デザインガイドライン

### カラーパレット

以下の色を基本として使用してください:

- **メインカラー**: `#4A90E2` (青)
- **サブカラー**: `#A78BFA` (紫)
- **アクセント**: `#56C288` (緑)
- **背景**: `#F8F9FA` (グレー)

### グラデーション例

```css
background: linear-gradient(135deg, #A78BFA 0%, #4A90E2 100%);
background: linear-gradient(135deg, #4A90E2 0%, #667eea 100%);
background: linear-gradient(90deg, #E3F2FD 0%, #F3E5F5 100%);
```

### ボックススタイル例

```css
.info-box {
    background-color: #F8F9FA;
    border-left: 4px solid #4A90E2;
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1rem 0;
}
```

---

## 📚 既存コンテンツの参考

### コンテンツ01: 経費精算
- **特徴**: CSVアップロード、データプレビュー
- **参考ポイント**: ファイルアップロードUI

### コンテンツ02: プチ仕様駆動開発
- **特徴**: フォーム入力、テンプレート提示
- **参考ポイント**: テキストエリア、ダウンロードボタン

### コンテンツ03: 会議議事録生成
- **特徴**: AWS Bedrock連携、複数区切り文字対応
- **参考ポイント**: Claude API統合、非同期処理

### コンテンツ04: プロマネ実践
- **特徴**: 5セクション構成、複雑なレイアウト
- **参考ポイント**: カラム分割、ダウンロード複数種類

---

## 🛠️ よくあるエラーと対処法

### エラー1: `ModuleNotFoundError: No module named 'components'`

**原因**: `from components import render_top_button` のimportが失敗

**対処法**: ファイルがプロジェクトルート（`app.py`と同じ階層）にあることを確認

### エラー2: TOPボタンをクリックしても遷移しない

**原因**: `st.switch_page("app.py")` のパスが間違っている

**対処法**: `components.py` の `st.switch_page("app.py")` を確認（相対パスではなく、`app.py`のみ）

### エラー3: サイドバーが表示される

**原因**: `[data-testid="stSidebar"]` のCSSが追加されていない

**対処法**: `st.markdown("""<style>...</style>""")` にサイドバー非表示CSSを追加

### エラー4: テストが失敗する（Red → Greenできない）

**原因**: 実装がテストの期待値と一致していない

**対処法**: 
1. テストのエラーメッセージを確認
2. ファイル内容を確認（CSSクラス名、import文、関数呼び出しなど）
3. `pytest tests/test_XX_*.py -v` で詳細なエラーを確認

### エラー5: Playwrightテストがタイムアウト

**原因**: Streamlitアプリが起動していない、または要素の読み込みが遅い

**対処法**:
```bash
# 別ターミナルでStreamlitアプリを起動
streamlit run app.py

# タイムアウトを延長
page.wait_for_selector("h1", timeout=15000)  # 15秒に延長
```

---

## ✅ チェックリスト

新しいコンテンツを追加する際は、以下をチェックしてください:

### 実装前
- [ ] `contents.yaml` にエントリを追加した
- [ ] テストファイルを作成した（`tests/test_XX_*_static.py`, `tests/test_XX_*_visual.py`）
- [ ] 🔴 Red: テストを実行して失敗することを確認した

### 実装中
- [ ] `pages/XX_絵文字_ページ名.py` を作成した
- [ ] `from components import render_top_button, render_footer` をimportした
- [ ] サイドバー非表示CSSを追加した
- [ ] `render_top_button()` を呼び出した（ヘッダーの前）
- [ ] `render_footer()` を呼び出した（ページの最後）

### 実装後
- [ ] 🟢 Green: テストを実行して成功することを確認した
- [ ] ローカルで動作確認した（トップ→ページ→トップの遷移）
- [ ] GitHubにpushした（ページ + テストファイル）
- [ ] 本番環境で動作確認した

---

## 📝 テンプレートファイルの場所

テンプレートファイルは以下を参照してください:

- **シンプルなページ**: `pages/02_📝_プチ仕様駆動開発体験.py`
- **Claude API連携**: `pages/03_📋_会議議事録生成.py`
- **複雑なレイアウト**: `pages/04_🎯_プロマネ実践.py`

---

## 🎓 メタ学習のポイント

このアプリ自体が「学習コンテンツの追加方法」を学ぶための教材になっています。

- **YAML**: `contents.yaml` を編集することで、YAMLの書き方を学べる
- **Streamlit**: 各ページのコードを読むことで、Streamlitの使い方を学べる
- **Git/GitHub**: プッシュ→自動デプロイの流れを体験できる

---

**更新履歴:**
- 2026-03-05: 初版作成
- 2026-03-10: TDDメソッド（twadaメソッド）とテスト手順を追加
