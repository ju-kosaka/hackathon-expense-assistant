# 第3章: 技術的な学び

**開発を通じて得た6つの教訓**

---

## 📚 はじめに

このプロジェクトでは、開発プロセス全体を通じて多くの技術的な学びがありました。
特に、**本番環境での動作**、**フォルダ構成のルール化**、**外部API活用**など、
実践的な知見を`KNOWLEDGE.md`に記録してきました。

この章では、その中から特に重要な6つの教訓を抽出し、体系的にまとめます。

---

## 教訓1: 本番環境での動作を最優先にする 🚀

### 状況

**問題点:**
- ローカル環境でサイドバーに「🏠 TOP」と表示させるために、`app.py` → `🏠_TOP.py` にリネームした
- Streamlit Community Cloudでは、Main file pathの設定項目がなく、`app.py`を自動検出する仕様だった

**結果:**
```
デプロイエラー: 
The main module file does not exist: /mount/src/hackathon-expense-assistant/app.py
```

### 解決策

1. **`app.py`を復活させる**
   - 本番環境の制約を優先
   - ローカルでの見た目は妥協

2. **サイドバー非表示はCSSで対応**
   ```python
   st.markdown("""
   <style>
       [data-testid="stSidebar"] {
           display: none;
       }
   </style>
   """, unsafe_allow_html=True)
   ```

### 学んだこと

#### ✅ 本番優先の開発フロー

```
ローカル開発 → 本番デプロイ確認 → UI改善
```

**ポイント:**
- ローカルで動いても、本番で動かないと意味がない
- デプロイ環境の制約を事前に調査する
- 「完璧な設計」より「動くもの」が優先（特にハッカソンでは）

#### 📋 チェックリスト

- [ ] デプロイ環境のドキュメントを読む
- [ ] ローカルと本番の違いをリストアップ
- [ ] 本番環境で動作確認してからUI改善

### 適用場面

- **Streamlit Community Cloud**: `app.py`が必須
- **Vercel**: `vercel.json`で設定が必要
- **Heroku**: `Procfile`で起動コマンドを指定

---

## 教訓2: サイドバーを完全に非表示にする方法 🎨

### 状況

**問題点:**
- Streamlitのサイドバー（ページナビゲーション）が表示されている
- `.app`や絵文字付きのページ名が表示され、ユーザーにとって混乱の元

### 解決策

**CSS強制非表示:**
```python
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)
```

全ページ（`app.py` + `pages/`配下の全ファイル）に追加する。

### 学んだこと

#### ❌ `initial_sidebar_state="collapsed"`では不十分

- 小さいボタンが残ってしまう
- 完全に非表示にはならない

#### ✅ CSS `display: none;`が最適

- クリーンなUIになる
- ユーザーがサイドバーを開けない

#### ⚠️ トレードオフ

- ページ間の移動がボタンのみになる
- ユーザーが途中のページに直接アクセスした場合、トップに戻る手段が必要

**対策:**
- ヘッダーに「🏠 TOP」ボタンを常設（`components.py`で実装）
- フッターにもTOPボタンを配置

### コード例

**components.py:**
```python
def render_top_button():
    if st.button("🏠 TOP"):
        st.switch_page("app.py")
```

**各ページ:**
```python
from components import render_top_button
render_top_button()
```

---

## 教訓3: ファイル名変更はGitが自動認識する 🛠️

### 状況

`app.py` → `🏠_TOP.py`にリネームした際、Gitが自動的に`renamed`として認識した。

### 学んだこと

#### Git の賢い仕組み

```bash
git mv app.py 🏠_TOP.py
# または
mv app.py 🏠_TOP.py
git add -A
```

どちらでも、Gitは内容の類似性から「rename」と判断してくれる。

**出力例:**
```
renamed:    app.py -> 🏠_TOP.py
```

#### メリット

- 履歴が追跡できる
- 差分が見やすい
- レビュー時に変更内容が明確

### 適用場面

- ファイル名のリファクタリング
- フォルダ構成の変更
- 大規模なリネーム作業

---

## 教訓4: Qiita記事の取得方法 🌐

### 状況

**目的:**
Qiita記事（https://qiita.com/yoshiakih/items/18cd541d03720ab08958）からコンテンツを取得して、チュートリアルページを作成。

**試した方法:**

| 方法 | 結果 | 問題点 |
|------|------|--------|
| WebFetchツール | ❌ 失敗 | モデルエラー（400） |
| `curl`でHTML取得 | ⚠️ 成功 | HTMLタグが大量に含まれる |
| 手動抽出 | ✅ 採用 | 最終的にこれを選択 |

### より良い方法: Qiita API v2

#### API仕様

**エンドポイント:**
```
GET https://qiita.com/api/v2/items/{item_id}
```

**例:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     https://qiita.com/api/v2/items/18cd541d03720ab08958
```

#### レスポンス

```json
{
  "id": "18cd541d03720ab08958",
  "title": "Claude Code Plan modeの計画フォーマットをカスタマイズする",
  "body": "記事本文（Markdown形式）",
  "tags": [{"name": "ClaudeCode"}],
  "user": {"id": "yoshiakih"},
  "url": "https://qiita.com/yoshiakih/items/18cd541d03720ab08958"
}
```

**メリット:**
- ✅ JSON形式でクリーンなデータ
- ✅ Markdown形式で記事本文が取得できる
- ✅ HTMLパース不要

#### 実装例

```python
import requests

def fetch_qiita_article(article_id):
    """Qiita APIで記事を取得"""
    url = f"https://qiita.com/api/v2/items/{article_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'title': data['title'],
            'body': data['body'],  # Markdown形式
            'tags': [tag['name'] for tag in data['tags']],
            'url': data['url']
        }
    return None

# URLから記事IDを抽出
# https://qiita.com/yoshiakih/items/18cd541d03720ab08958
# → article_id = "18cd541d03720ab08958"
```

### 学んだこと

#### ✅ 専用APIを使う方が確実

- WebFetchの代替手段として
- Qiita APIは認証なしでも利用可能（制限あり）
- 無料枠: 認証なし60req/h、認証あり1000req/h

#### ⚠️ 注意点

- URLから記事IDを抽出する処理が必要
- API制限に注意
- エラーハンドリング（記事が存在しない、API制限など）

### 次回の改善案

1. **`add_new_content.py`に`fetch_qiita_article()`関数を追加**
2. **URLから記事IDを自動抽出する正規表現を実装**
3. **エラーハンドリング強化**

---

## 教訓5: Claude Code Hooks設定の仕組み 🔔

### 状況

Claude CodeのHooks機能（Notification、PostToolUse）を使った通知設定を学習コンテンツ化。
`~/.claude/settings.json`で通知音（Purr含む）をカスタマイズする手順を整理。

### settings.jsonの構造

```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "通知コマンド"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "ツール実行後のコマンド"
          }
        ]
      }
    ]
  }
}
```

### macOS通知の実装

```bash
osascript -e 'display notification "メッセージ" with title "タイトル" sound name "Purr"'
```

**要素:**
- `osascript`: macOSのAppleScriptを実行するCLIツール
- `display notification`: 通知センターに通知を表示
- `sound name`: 通知音の指定（Purr、Basso、Hero、Pingなど）

### ログファイルの活用

```bash
echo '[PostToolUse] '$(date) >> /tmp/claude_hooks.log && osascript -e '...'
```

**メリット:**
- `&&`: 前のコマンドが成功したら次を実行
- ログファイル（`/tmp/claude_hooks.log`）でHooksの動作確認ができる
- デバッグ時に役立つ

### 実際の設定例

```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo '[Notification] '$(date) >> /tmp/claude_hooks.log && osascript -e 'display notification \"Claude Code からの通知\" with title \"Claude Code\" sound name \"Purr\"'"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo '[PostToolUse] '$(date) >> /tmp/claude_hooks.log && osascript -e 'display notification \"ツールの実行が完了しました\" with title \"Claude Code\" sound name \"Purr\"'"
          }
        ]
      }
    ]
  }
}
```

### 学んだこと

#### ⚠️ 注意事項

- **macOS専用**: Windows/Linuxでは動作しない
- **JSON形式**: シンタックスエラーに注意（カンマ、クォート）
- **バックアップ推奨**: 既存の`settings.json`を上書きしないよう注意

#### 🎯 今後の拡張案

- Windows/Linux向けの通知設定の追加
- Hooksのその他の活用例（UserPromptSubmitなど）
- 通知音のプレビュー再生機能

---

## 教訓6: プロジェクトのフォルダ構成ルール 📂

### 状況

**問題点:**
- ファイルが増えてきて、ルートディレクトリが散らかっていた
- ドキュメント、スクリプト、本番ファイルが混在

**解決策:**
フォルダ構成を大規模リファクタリングし、ルールを`KNOWLEDGE.md`に記録。

### 新しいフォルダ構成

```
hackathon-app/
├── app.py                          # メインファイル（本番用、必須）
├── components.py                   # 共通コンポーネント（必須）
├── contents.yaml                   # コンテンツ管理（必須）
├── requirements.txt                # 依存パッケージ（必須）
├── README.md                       # プロジェクトREADME
├── folder-old.md                   # リファクタリング前の構成記録
│
├── pages/                          # Streamlitページ（必須）
│   ├── 01_🔧_VSCode設定.py
│   └── ...（全7コンテンツ）
│
├── docs/                           # ドキュメント集約
│   ├── specs/                      # 仕様書
│   │   ├── SPEC.md
│   │   ├── SPEC-setcharacter.md
│   │   └── SPEC-notification.md
│   │
│   ├── guides/                     # ガイド・手順書
│   │   └── add-content.md
│   │
│   └── project/                    # プロジェクト管理
│       ├── PLAN.md
│       ├── TODO.md
│       └── KNOWLEDGE.md
│
├── scripts/                        # 開発スクリプト
│   ├── add_new_content.py
│   └── 🏠_TOP.py
│
├── memo/                           # 開発メモ
│   └── streamlit_integration_consideration.md
│
└── static/                         # 静的ファイル
    └── sounds/                     # 音声ファイル（現在空）
```

### 今後のファイル作成ルール

#### ルール1: ルートディレクトリには必須ファイルのみ

**配置できるファイル:**
- `app.py` - メインエントリーポイント（Streamlit Community Cloud必須）
- `components.py` - 共通コンポーネント（全ページから参照）
- `contents.yaml` - コンテンツ管理（TOPページが参照）
- `requirements.txt` - 依存パッケージ（デプロイ時必須）
- `README.md` - プロジェクト説明
- `.gitignore`, `.python-version`など設定ファイル

**配置してはいけないファイル:**
- ドキュメント類（`.md`ファイル）
- 開発スクリプト（`.py`ファイル）
- メモやログ

#### ルール2: ドキュメントは`docs/`配下に分類

##### `docs/specs/` - 仕様書
- **命名規則**: `SPEC-<機能名>.md`
- **例**: `SPEC-notification.md`, `SPEC-setcharacter.md`
- **内容**: コンテンツの詳細仕様、学習目標、UI/UX設計、技術実装

##### `docs/guides/` - ガイド・手順書
- **命名規則**: `<動詞>-<対象>.md`
- **例**: `add-content.md`
- **内容**: 開発者向けの手順書、ガイドライン

##### `docs/project/` - プロジェクト管理
- **ファイル名**: 固定
  - `PLAN.md` - 開発計画
  - `TODO.md` - TODOリスト
  - `KNOWLEDGE.md` - 学んだ教訓・知見
- **内容**: プロジェクト全体の管理情報

#### ルール3: 開発スクリプトは`scripts/`配下

- **命名規則**: `<動詞>_<対象>.py`
- **例**: `add_new_content.py`
- **内容**: 開発を支援するスクリプト（本番環境では不使用）
- **特別なファイル**: `🏠_TOP.py` - ローカル開発用TOP

#### ルール4: メモは`memo/`配下

- **命名規則**: `<内容>_<タイプ>.md`
- **例**: `streamlit_integration_consideration.md`
- **内容**: 技術検討メモ、調査記録、保留事項

#### ルール5: 静的ファイルは`static/`配下

- **サブディレクトリ**: `sounds/`, `images/`など
- **例**: `static/sounds/notification.mp3`
- **内容**: 音声、画像、その他の静的リソース

### リファクタリングから学んだこと

#### ✅ 定期的な整理の重要性

- ファイルが増えてきたら、早めに整理する
- ルールを決めておくと、後から迷わない

#### ✅ バックアップの重要性

- `folder-old.md`を作成してから整理した
- 問題が起きても元に戻せる安心感

#### ✅ 依存関係の理解

- `components.py`, `contents.yaml`はルートに必須
- `pages/`はStreamlitの仕様でルートに必須
- ドキュメントは自由に移動できる

#### ✅ 段階的な整理

- いきなり全部移動せず、少しずつ確認しながら進める
- 各ステップで動作確認（Pythonファイルの構文チェック等）

---

## 🧠 まとめ: 6つの教訓の活かし方

### 開発プロセス

1. **本番環境を最優先**（教訓1）
   - デプロイ環境の制約を事前調査
   - ローカルで動いても本番で動かないと意味がない

2. **段階的なリファクタリング**（教訓6）
   - フォルダ構成のルール化
   - ファイルが増えたら早めに整理

### 技術的なテクニック

3. **Gitの活用**（教訓3）
   - ファイル名変更を自動認識
   - 履歴追跡の重要性

4. **外部API活用**（教訓4）
   - Qiita API v2でコンテンツ取得
   - Markdown形式の利点

5. **Hooks機能**（教訓5）
   - 通知のカスタマイズ
   - ログファイルでデバッグ

### UI/UX

6. **CSS活用**（教訓2）
   - サイドバー非表示
   - クリーンなUI設計

---

## 📚 参考リンク

- [Streamlit Community Cloud ドキュメント](https://docs.streamlit.io/streamlit-community-cloud)
- [Qiita API v2 ドキュメント](https://qiita.com/api/v2/docs)
- [Claude Code Hooks ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)
- [osascript マニュアル](https://ss64.com/osx/osascript.html)

---

**次の章**: [04_development-process.md](./04_development-process.md) - 開発プロセス
