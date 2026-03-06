# KNOWLEDGE.md - 学んだ教訓・知見

このファイルは、プロジェクトを通じて学んだ教訓や技術的な知見を記録します。

---

## 📅 2026-03-04

### 🚀 デプロイ・本番環境

#### **教訓1: 本番環境での動作を最優先にする**

**状況:**
- ローカル環境でサイドバーに "🏠 TOP" と表示させるために、`app.py` → `🏠_TOP.py` にリネームした
- Streamlit Community Cloudでは、Main file pathの設定項目がなく、`app.py` を自動検出する仕様だった
- 結果: デプロイエラー「The main module file does not exist: /mount/src/hackathon-expense-assistant/app.py」

**解決策:**
- `app.py` を復活させて、本番環境を優先
- サイドバーは `.app` のままで妥協（または、CSSで完全非表示にする）

**学んだこと:**
- **本番環境での動作を最優先にする**
- ローカルでの見た目の改善よりも、まず本番で動くことが重要
- Streamlit Community Cloudは設定の自由度が低いため、プラットフォームの制約に従う
- ハッカソンや期限のあるプロジェクトでは、「完璧な設計」よりも「動くもの」が優先

**今後の対応:**
- 新機能を追加する際は、まずローカルで動作確認
- その後、本番環境で問題が起きないかを確認してからデプロイ
- デプロイ前に、Streamlit Community Cloudの制約を事前に調査する

---

### 🎨 UI/UX

#### **教訓2: サイドバーを完全に非表示にする方法**

**状況:**
- Streamlitのサイドバー（ページナビゲーション）が表示されているが、学習アプリとして不要
- `.app` や絵文字付きのページ名が表示されるが、ユーザーにとって混乱の元

**解決策:**
- CSSで `[data-testid="stSidebar"]` を `display: none;` にする
- 全ページ（app.py + pages/配下の全ファイル）に以下を追加:

```python
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)
```

**学んだこと:**
- Streamlitの `initial_sidebar_state="collapsed"` では完全に非表示にならない（小さいボタンが残る）
- CSSで強制的に非表示にする方が、クリーンなUIになる
- ページ間の移動は、トップページの「学習を始める」ボタンで行う

**トレードオフ:**
- サイドバーを非表示にすると、ページ間の移動がボタンのみになる
- ユーザーが途中のページに直接アクセスした場合、トップに戻る手段がない（対応: ヘッダーにロゴリンクを追加する等）

---

### 🛠️ Git/GitHub

#### **教訓3: ファイル名変更はGitが自動認識する**

**状況:**
- `app.py` → `🏠_TOP.py` にリネームした際、Gitが `renamed` として認識した

**学んだこと:**
- Gitは内容が同じファイルを自動的に「rename」として認識する
- `git add -A` で削除と追加を一括でステージングすると、Gitが賢く判断してくれる

---

## 📅 2026-03-05

### 🌐 外部コンテンツの取得

#### **教訓4: Qiita記事の取得方法**

**状況:**
- Qiita記事 (https://qiita.com/yoshiakih/items/18cd541d03720ab08958) からコンテンツを取得してチュートリアルページを作成
- WebFetchツールがモデルエラー（400 The provided model identifier is invalid）で失敗
- 代替として`curl`でHTMLを取得したが、HTMLパース処理が必要だった

**試した方法:**
1. ❌ WebFetchツール → モデルエラーで失敗
2. ⚠️ `curl`でHTML取得 → 成功したが、HTMLタグが大量に含まれる
3. ✅ 記事タイトルと概要を手動で抽出 → 最終的にこれを採用

**より良い方法（次回に試す）:**

1. **Qiita API v2を使用**
   ```bash
   curl -H "Authorization: Bearer YOUR_TOKEN" \
        https://qiita.com/api/v2/items/18cd541d03720ab08958
   ```
   - JSON形式でクリーンなデータが取得できる
   - `title`, `body`, `tags` などが構造化されている
   - 無料枠: 認証なし60req/h、認証あり1000req/h

2. **Markdown形式で取得**
   - Qiita APIは記事本文を**Markdown形式**で返す
   - HTMLパース不要で、そのまま活用できる
   - `body`フィールドに記事の全文が含まれる

3. **レスポンス例**
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

**実装例（add_new_content.py用）:**
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

# URLからarticle_idを抽出
# https://qiita.com/yoshiakih/items/18cd541d03720ab08958
# → article_id = "18cd541d03720ab08958"
```

**学んだこと:**
- WebFetchの代替手段として、専用APIを使う方が確実
- Qiita APIは認証なしでも利用可能（制限あり）
- Markdown形式で取得できるため、コンテンツ生成に最適
- URLから記事IDを抽出する処理が必要

**次回の改善:**
- `add_new_content.py`に`fetch_qiita_article()`関数を追加
- URLから記事IDを自動抽出する正規表現を実装
- エラーハンドリング（記事が存在しない、API制限など）

**参考リンク:**
- [Qiita API v2 ドキュメント](https://qiita.com/api/v2/docs)
- [記事の取得エンドポイント](https://qiita.com/api/v2/docs#get-apiv2itemsitem_id)

---

## 🧠 次回に活かすこと

1. **デプロイ環境の制約を事前に確認する**
   - Streamlit Community Cloud、Vercel、Herokuなど、プラットフォームごとに制約が異なる
   - ローカルで動いても、本番で動かないことがある

2. **本番優先の開発フロー**
   - ローカル開発 → 本番デプロイ確認 → UI改善
   - 本番で動かないと意味がない

3. **UI/UX改善はトレードオフを理解して判断**
   - サイドバー非表示 = ナビゲーションの制約
   - 見た目の美しさと機能性のバランスを取る

4. **外部コンテンツ取得は専用APIを使う**
   - Qiita記事 → Qiita API v2
   - Zenn記事 → Zenn APIまたはRSS
   - Markdown形式で取得できるか確認
   - API制限とエラーハンドリングを忘れずに

---

## 📚 参考リンク

- [Streamlit Community Cloud ドキュメント](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit set_page_config リファレンス](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)
- [Qiita API v2 ドキュメント](https://qiita.com/api/v2/docs)

---

## 📅 2026-03-06

### 🔔 通知設定のコンテンツ化

#### **教訓5: Claude Code Hooks設定の仕組み**

**状況:**
- Claude CodeのHooks機能（Notification、PostToolUse）を使った通知設定を学習コンテンツ化
- `~/.claude/settings.json` で通知音（Purr含む）をカスタマイズする手順を整理

**実装したもの:**
1. **SPEC-notification.md**: 通知設定コンテンツの仕様書
2. **pages/07_🔔_通知設定.py**: Streamlitページ
3. **contents.yaml**: 新規コンテンツ（ID: 07）を追加

**学んだこと:**

##### 1. **settings.jsonの構造**
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

##### 2. **macOS通知の実装**
```bash
osascript -e 'display notification "メッセージ" with title "タイトル" sound name "Purr"'
```
- `osascript`: macOSのAppleScriptを実行するCLIツール
- `display notification`: 通知センターに通知を表示
- `sound name`: 通知音の指定（Purr、Basso、Hero、Pingなど）

##### 3. **ログファイルの活用**
```bash
echo '[PostToolUse] '$(date) >> /tmp/claude_hooks.log && osascript -e '...'
```
- `&&`: 前のコマンドが成功したら次を実行
- ログファイル（`/tmp/claude_hooks.log`）でHooksの動作確認ができる
- デバッグ時に役立つ

##### 4. **実際の設定例**
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

**注意事項:**
- macOS専用の機能（Windows/Linuxでは動作しない）
- 既存の`settings.json`を上書きしないよう、バックアップを推奨
- JSON形式のシンタックスエラーに注意（カンマ、クォート）

**今後の拡張案:**
- Windows/Linux向けの通知設定の追加
- Hooksのその他の活用例（UserPromptSubmitなど）
- 通知音のプレビュー再生機能

**参考リンク:**
- [Claude Code Hooks ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)
- [osascript マニュアル](https://ss64.com/osx/osascript.html)

---

**更新履歴:**
- 2026-03-04: 初版作成（デプロイ・UI・Git関連の教訓）
- 2026-03-05: Qiita記事取得方法を追加
- 2026-03-06: 通知設定コンテンツの追加と実装方法を記録
