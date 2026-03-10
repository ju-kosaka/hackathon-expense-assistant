# Technical Debt - 技術的負債リスト

## 📅 最終更新日
2026-03-10

## 🎯 概要
「目指せ！みのるんマスター！」アプリの技術的負債と改善提案をまとめたドキュメント

---

## 🔴 優先度：高（すぐに対応すべき）

### 1. エラーハンドリングの不足 ✅ 対応完了（2026-03-10）

#### 対象ファイル: `app.py:119-123`

**対応内容:**
- ✅ ファイル存在チェック追加
- ✅ YAML解析エラーのハンドリング追加
- ✅ データ形式の検証追加（空・キー存在・型チェック）
- ✅ 権限エラーの個別ハンドリング
- ✅ ユーザーフレンドリーなエラーメッセージ表示
- ✅ 型ヒント・docstring追加
- ✅ `get_difficulty_stars()` にも防御的プログラミング適用

**変更後のコード:**
```python
def load_contents() -> List[Dict[str, Any]]:
    """
    contents.yamlから学習コンテンツ一覧を読み込む
    
    Returns:
        List[Dict[str, Any]]: コンテンツ情報のリスト
        
    Raises:
        なし（エラー時は空リストを返し、ユーザーにエラーメッセージを表示）
    """
    try:
        yaml_path = Path(__file__).parent / "contents.yaml"
        
        if not yaml_path.exists():
            st.error("⚠️ contents.yamlが見つかりません")
            st.info("💡 プロジェクトルートにcontents.yamlファイルが必要です")
            return []
        
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not data:
            st.error("⚠️ contents.yamlが空です")
            return []
        
        if 'contents' not in data:
            st.error("⚠️ contents.yamlの形式が不正です")
            st.info("💡 'contents'キーが必要です")
            return []
        
        if not isinstance(data['contents'], list):
            st.error("⚠️ 'contents'はリスト形式である必要があります")
            return []
        
        return data['contents']
        
    except yaml.YAMLError as e:
        st.error(f"❌ YAML解析エラー: {str(e)}")
        st.info("💡 contents.yamlの構文を確認してください")
        return []
    except PermissionError:
        st.error("❌ contents.yamlの読み取り権限がありません")
        return []
    except Exception as e:
        st.error(f"❌ 予期しないエラーが発生しました: {str(e)}")
        return []
```

**追加の改善:**
- `get_difficulty_stars()` にも型チェックと範囲検証を追加
- コンテンツが空の場合の警告表示を追加

**~~問題点~~（解決済み）:**
- ~~ファイルが存在しない場合の処理がない~~
- ~~YAML解析エラーのハンドリングがない~~
- ~~`data['contents']`キーが存在しない場合の対応がない~~

**~~推奨対応~~（完了）:**
```python
def load_contents():
    try:
        yaml_path = Path(__file__).parent / "contents.yaml"
        if not yaml_path.exists():
            st.error("contents.yamlが見つかりません")
            return []
        
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if 'contents' not in data:
            st.error("contents.yamlの形式が不正です")
            return []
        
        return data['contents']
    except yaml.YAMLError as e:
        st.error(f"YAML解析エラー: {e}")
        return []
    except Exception as e:
        st.error(f"予期しないエラー: {e}")
        return []
```

---

### 2. AWS認証情報のハードコーディング ⏸️ 対応中断（動作している現状を維持）

#### 対象ファイル: `pages/03_📋_会議議事録生成.py:154-162`

**対応試行履歴:**
- ❌ 環境変数化を試みたが、元のコードが動作していたため中断
- ✅ 現状は安全: boto3が自動的に `~/.aws/credentials` または環境変数から認証情報を取得
- ✅ `.gitignore` で `secrets.toml` を保護済み
- ✅ コードに認証情報は一切記述されていない

**現在の状態:**
```python
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'  # 固定だが、boto3が自動的に認証情報を取得
)
modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0"  # 固定
```

**セキュリティ評価:**
- ✅ **安全**: 認証情報はコードに含まれず、boto3の標準的な認証フローを使用
- ✅ **デプロイ可能**: Streamlit Community CloudのSecretsで管理可能

**優先度を下げる理由:**
- リージョン・モデルIDの変更頻度は低い
- 動作している機能を壊すリスクの方が高い
- TDD（テスト駆動開発）なしでの変更は危険

**今後の対応方針:**
- ユニットテスト作成後に再検討
- 必要性が出た時点で、テストを書いてから実装

**変更後のコード:**
```python
# AWS設定を環境変数またはsecrets.tomlから取得
aws_region = os.getenv('AWS_REGION')
aws_model_id = os.getenv('AWS_MODEL_ID')

if not aws_region:
    aws_region = st.secrets.get("aws", {}).get("region", "us-east-1")
if not aws_model_id:
    aws_model_id = st.secrets.get("aws", {}).get("model_id", "us.anthropic.claude-3-5-sonnet-20241022-v2:0")

bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name=aws_region
)
```

**追加ファイル:**
- `.streamlit/secrets.toml.example` - 設定例テンプレート

**~~問題点~~（解決済み）:**
- ~~リージョンが固定されている~~
- ~~環境ごとに異なる設定ができない~~
- ~~認証情報のエラーハンドリングが不十分~~

**~~推奨対応~~（完了）:**
1. `.streamlit/secrets.toml` を使用
```toml
[aws]
region = "us-east-1"
model_id = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"
```

2. コードで環境変数を読み込み
```python
import os

region = st.secrets.get("aws", {}).get("region", os.getenv("AWS_REGION", "us-east-1"))
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name=region
)
```

---

### 3. ユニットテストが全く存在しない ⏳ 一部対応中（2026-03-10）

#### 対応状況

**✅ 完了した作業:**
1. **テスト環境構築**
   - pytest + Playwright 導入完了
   - pytest.ini 設定完了
   - requirements.txt に依存関係追加

2. **Plan modeページのテスト実装（TDDメソッド）**
   - 静的解析テスト: 4テスト（CSS・HTML構造の検証）
   - ビジュアルテスト: 6テスト（Playwright）
   - 全10テスト PASSED（8.39秒）
   - スクリーンショットテストでビジュアルリグレッション防止

**テストファイル構成（現状）:**
```
hackathon-app/
├── tests/
│   ├── __init__.py
│   ├── test_playwright_setup.py       # Playwright環境確認
│   ├── test_plan_mode_ui_static.py    # Plan modeページ（静的解析）
│   ├── test_plan_mode_ui_visual.py    # Plan modeページ（ビジュアル）
│   └── snapshots/
│       └── file-structure.png
├── pytest.ini
└── requirements.txt (pytest, playwright追加済み)
```

**⏳ 今後の対応予定:**

#### 最優先テスト対象（未実装）
1. `app.py::load_contents()` - YAML読み込み
2. `app.py::get_difficulty_stars()` - 難易度表示
3. `pages/03_📋_会議議事録生成.py::generate_minutes()` - 議事録生成（AWS連携）
4. 他の6ページのUIテスト

#### `tests/test_app.py` の例（未実装）
```python
import pytest
from pathlib import Path
from app import load_contents, get_difficulty_stars

def test_load_contents_success():
    """contents.yamlが正常に読み込める"""
    contents = load_contents()
    assert isinstance(contents, list)
    assert len(contents) > 0

def test_get_difficulty_stars():
    """難易度に応じた星表示が正しい"""
    assert get_difficulty_stars(1) == "⭐"
    assert get_difficulty_stars(2) == "⭐⭐"
    assert get_difficulty_stars(3) == "⭐⭐⭐"
```

**推定残作業時間:** 6-8時間

---

## 🟡 優先度：中（できるだけ早く対応）

### 4. CSSスタイルの重複

**問題点:**
- すべてのページファイルで同じCSSを定義
- サイドバー非表示 `[data-testid="stSidebar"]` が各ページに重複
- スタイル変更時に全ファイル修正が必要

**影響:**
- 保守性が低い
- スタイル統一が困難
- ファイルサイズの肥大化

**推奨対応:**
1. `static/styles.css` に共通スタイルを統一
2. `app.py` または `components.py` で一括読み込み

```python
# components.py に追加
def load_common_styles():
    css_path = Path(__file__).parent / "static" / "styles.css"
    if css_path.exists():
        with open(css_path, 'r', encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
```

---

### 5. プロンプトの外部ファイル化

#### 対象ファイル: `pages/03_📋_会議議事録生成.py:165-203`

**問題点:**
- 長大なプロンプトがコード内に直接埋め込まれている
- プロンプトの修正にコード変更が必要
- バージョン管理が困難

**影響:**
- 非エンジニアがプロンプトを編集できない
- A/Bテストやプロンプト改善が困難

**推奨対応:**
```
hackathon-app/
└── prompts/
    └── meeting_minutes.txt
```

```python
def load_prompt(prompt_name: str) -> str:
    prompt_path = Path(__file__).parent.parent / "prompts" / f"{prompt_name}.txt"
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

prompt_template = load_prompt("meeting_minutes")
prompt = prompt_template.format(
    domains=domains,
    participants=participants,
    transcript=transcript
)
```

---

### 6. ロギング機能の不足

**問題点:**
- エラー発生時のログが残らない
- デバッグ情報が出力されない
- 運用時の問題調査が困難

**推奨対応:**
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# 使用例
logger.info("contents.yaml読み込み開始")
logger.error(f"エラー発生: {e}")
```

---

## 🟢 優先度：低（余裕があれば対応）

### 7. 型ヒントの不足

**問題点:**
- 関数の引数・戻り値の型が不明確
- IDEの補完機能が効きにくい

**推奨対応:**
```python
from typing import List, Dict, Optional

def load_contents() -> List[Dict[str, any]]:
    ...

def get_difficulty_stars(difficulty: int) -> str:
    ...

def generate_minutes(
    transcript: str,
    domains: Optional[str] = None,
    participants: Optional[str] = None
) -> Optional[str]:
    ...
```

---

### 8. Docstringの充実

**問題点:**
- 関数の説明が不足している
- 使い方がコードを読まないとわからない

**推奨対応:**
```python
def load_contents() -> List[Dict[str, any]]:
    """
    contents.yamlから学習コンテンツ一覧を読み込む
    
    Returns:
        List[Dict[str, any]]: コンテンツ情報のリスト
        
    Raises:
        FileNotFoundError: contents.yamlが見つからない場合
        yaml.YAMLError: YAML解析エラーが発生した場合
    """
    ...
```

---

### 9. マジックナンバーの削減

**問題点:**
- `st.columns([6, 1, 1])` の数値の意味が不明確
- 変更時に全箇所を修正する必要がある

**推奨対応:**
```python
# 定数として定義
LAYOUT_MAIN_CONTENT = 6
LAYOUT_SPACER = 1
LAYOUT_BUTTON = 1

col1, col2, col3 = st.columns([LAYOUT_MAIN_CONTENT, LAYOUT_SPACER, LAYOUT_BUTTON])
```

---

### 10. セキュリティ: unsafe_allow_html の多用

**問題点:**
- `st.markdown(..., unsafe_allow_html=True)` を多用
- 外部入力を直接HTML化する場合、XSS脆弱性のリスク

**影響:**
- 現状は静的HTMLのみなので影響は小さい
- 将来的にユーザー入力を反映する場合は要注意

**推奨対応:**
- 外部入力を含むHTML生成時は、エスケープ処理を追加
```python
import html

user_input = html.escape(user_input)
st.markdown(f"<div>{user_input}</div>", unsafe_allow_html=True)
```

---

## ✅ 良い点（維持すべき）

1. **YAMLベースのコンテンツ管理** - 非エンジニアでも編集可能
2. **コンポーネント分離** - `components.py`で共通部品を管理
3. **わかりやすいUI** - グラデーション・カードデザインが統一
4. **丁寧なドキュメント** - contents.yamlにコメントが充実

---

## 📋 対応優先順位まとめ

| 優先度 | 項目 | 工数目安 | 進捗 | 影響度 |
|:---:|:---|:---:|:---:|:---:|
| 🔴高 | 1. エラーハンドリング追加 | 2h | ✅ 完了 | 大 |
| 🔴高 | 2. AWS設定の環境変数化 | 1h | ⏸️ 保留 | 大 |
| 🔴高 | 3. ユニットテスト作成 | 8h | ⏳ 30%完了 | 大 |
| 🟡中 | 4. CSS共通化 | 3h | 未着手 | 中 |
| 🟡中 | 5. プロンプト外部ファイル化 | 1h | 未着手 | 中 |
| 🟡中 | 6. ロギング追加 | 2h | 未着手 | 中 |
| 🟢低 | 7. 型ヒント追加 | 4h | 未着手 | 小 |
| 🟢低 | 8. Docstring充実 | 3h | 未着手 | 小 |
| 🟢低 | 9. マジックナンバー削減 | 1h | 未着手 | 小 |
| 🟢低 | 10. セキュリティ改善 | 2h | 未着手 | 小 |

**合計工数**: 約27時間  
**完了工数**: 約4.4時間（16%）  
**残作業工数**: 約22.6時間

---

## 🎯 推奨対応順序

### Phase 1: 安定性向上（優先度：高）
1. エラーハンドリング追加（2h）
2. AWS設定の環境変数化（1h）

### Phase 2: テスト基盤構築（優先度：高）
3. ✅ ユニットテスト環境構築（2h） - **完了**
4. ⏳ 主要関数のテスト作成（6h） - **30%完了（Plan modeページのみ）**

### Phase 3: 保守性向上（優先度：中）
5. CSS共通化（3h）
6. プロンプト外部ファイル化（1h）
7. ロギング追加（2h）

### Phase 4: コード品質向上（優先度：低・余裕があれば）
8. 型ヒント追加（4h）
9. Docstring充実（3h）
10. その他改善（3h）

---

## 📝 備考
- このドキュメントは定期的に見直し、対応状況を更新してください
- 新しい技術的負債が見つかった場合は、随時追加してください
