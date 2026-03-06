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

## 📅 2026-03-06（続き）

### 📂 フォルダ構成のルール（リファクタリング）

#### **教訓6: プロジェクトのフォルダ構成ルール**

**状況:**
- ファイルが増えてきて、ルートディレクトリが散らかっていた
- ドキュメント、スクリプト、本番ファイルが混在
- 整理してスッキリさせた

**実施したリファクタリング:**

##### 新しいフォルダ構成
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
│   ├── 01_💰_経費精算.py
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

##### 削除したファイル
1. `docs/guides/README_ADD_CONTENT.md` → `add-content.md` にマージして削除
2. `static/sounds/notification.mp3` → 未使用のため削除

---

### 📋 今後のファイル作成ルール

#### **ルール1: ルートディレクトリには必須ファイルのみ**

**配置できるファイル:**
- `app.py` - メインエントリーポイント（Streamlit Community Cloud必須）
- `components.py` - 共通コンポーネント（全ページから参照）
- `contents.yaml` - コンテンツ管理（TOPページが参照）
- `requirements.txt` - 依存パッケージ（デプロイ時必須）
- `README.md` - プロジェクト説明
- `.gitignore`, `.python-version` など設定ファイル

**配置してはいけないファイル:**
- ドキュメント類（`.md`ファイル）
- 開発スクリプト（`.py`ファイル）
- メモやログ

---

#### **ルール2: ドキュメントは`docs/`配下に分類**

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

---

#### **ルール3: 開発スクリプトは`scripts/`配下**

- **命名規則**: `<動詞>_<対象>.py`
- **例**: `add_new_content.py`
- **内容**: 開発を支援するスクリプト（本番環境では不使用）
- **特別なファイル**: `🏠_TOP.py` - ローカル開発用TOP

---

#### **ルール4: メモは`memo/`配下**

- **命名規則**: `<内容>_<タイプ>.md`
- **例**: `streamlit_integration_consideration.md`
- **内容**: 技術検討メモ、調査記録、保留事項

---

#### **ルール5: 静的ファイルは`static/`配下**

- **サブディレクトリ**: `sounds/`, `images/` など
- **例**: `static/sounds/notification.mp3`
- **内容**: 音声、画像、その他の静的リソース

---

### ⚠️ 新規ファイル作成時の注意

**必ず守ること:**
1. **ルートディレクトリには配置しない** - 必ず適切なサブディレクトリに配置
2. **ルールに迷ったら確認する** - ユーザーに確認してから作成
3. **命名規則に従う** - 各ディレクトリの命名規則を守る
4. **重複を避ける** - 既存ファイルとの重複がないか確認

**確認が必要なケース:**
- ルートディレクトリに新しい`.md`ファイルを作りたい場合
- 新しいサブディレクトリを作りたい場合
- 既存のルールに当てはまらないファイルを作りたい場合
- ファイルの配置先に迷った場合

**例外:**
- `folder-old.md` - リファクタリング記録（一時的）
- 設定ファイル（`.gitignore`, `.streamlit/` など）

---

### 📝 リファクタリングから学んだこと

1. **定期的な整理の重要性**
   - ファイルが増えてきたら、早めに整理する
   - ルールを決めておくと、後から迷わない

2. **バックアップの重要性**
   - `folder-old.md` を作成してから整理した
   - 問題が起きても元に戻せる安心感

3. **依存関係の理解**
   - `components.py`, `contents.yaml` はルートに必須
   - `pages/` はStreamlitの仕様でルートに必須
   - ドキュメントは自由に移動できる

4. **段階的な整理**
   - いきなり全部移動せず、少しずつ確認しながら進める
   - 各ステップで動作確認（Pythonファイルの構文チェック等）

---

### 📱 OGP最適化

#### **教訓7: Open Graph Protocol (OGP) の最適化**

**状況:**
- Streamlitアプリのシェア時に、"TOP - 目指せ！みのるんマスター！" という不要な接頭辞が表示されていた
- READMEが経費精算アプリの説明になっていて、現在の学習アプリと内容が乖離していた

**実施した改善:**

##### 1. **OGPタイトルの最適化**
```python
st.set_page_config(
    page_title="目指せ！みのるんマスター！",
)
```
- ✅ 変更前: `"TOP - 目指せ！みのるんマスター！"`
- ✅ 変更後: `"目指せ！みのるんマスター！"`
- 理由: 不要な接頭辞を削除してシンプルに

##### 2. **README.mdの全面刷新**
- タイトル: 経費精算アシスタント → **目指せ！みのるんマスター！**
- 説明文: "AIを使ってみたいけど、難しいと思っていてなかなか使えないあなたに。"
- 内容: 7つの学習コンテンツの詳細を追加
- 特徴: 段階的学習、実践的ユースケース、メタ学習要素を明記

##### 3. **フッターの整理**
```python
<p>Powered by Claude Code</p>
```
- ✅ 変更前: `"Powered by Claude AI | Hackathon MVP"`
- ✅ 変更後: `"Powered by Claude Code"`
- 理由: ハッカソン完了後のクリーンな表示

**学んだこと:**
- OGPはSNSシェア時の第一印象を決める重要な要素
- `st.set_page_config(page_title=...)` がOGPタイトルになる
- README.mdはプロジェクトの顔であり、常に最新の状態に保つべき
- 開発フェーズ（MVP/ベータ/製品版）に応じてメッセージを更新する

**参考リンク:**
- [Open Graph Protocol 公式サイト](https://ogp.me/)
- [Streamlit set_page_config ドキュメント](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)

---

### 🛡️ YAML編集リスクとユーザー保護

#### **教訓8: 設定ファイル編集のリスク管理**

**状況:**
- 当初、`app.py` にYAMLファイルの編集を推奨する案内があった
- YAML構文エラーが発生すると、アプリ全体が起動しなくなるリスクがあった
- 非エンジニアユーザーにとって、YAMLの編集はハードルが高い

**実施した対策:**

##### 1. **YAML編集案内の削除**
**削除した箇所:**
- `app.py` (lines 154-163): hint-boxとGitHubリンク
- `scripts/🏠_TOP.py`: 同様の案内

**残した箇所:**
- `docs/guides/add-content.md`: 開発者向けガイド
- `docs/hackathon-report/`: ハッカソン報告資料
- 理由: 開発者は構文エラーに対応できるため

##### 2. **README.mdのメッセージ変更**
```markdown
✅ 変更前: YAMLベースのコンテンツ管理で、自分でコンテンツを追加できる
✅ 変更後: YAMLベースのコンテンツ管理で、データ管理の仕組みを理解できます
```
- ユーザーに編集を促さず、学習要素として位置づけ

**YAMLのリスク:**
```yaml
contents:
  - id: 01
    title: タイトル
    icon: 🎓
    difficulty: 1  # ← カンマを入れるとエラー、

contents:
  - id: 01
    title: "タイトル  # ← 閉じクォートがないとエラー
```

**学んだこと:**
1. **設定ファイルの編集はハイリスク**
   - YAML構文エラー → アプリ全体が起動不可
   - 非エンジニアには構文の理解が難しい
2. **ユーザー保護の重要性**
   - 「できる」ことを全て案内するのではなく、リスクも考慮
   - 開発者向けドキュメントとユーザー向けUIは分離
3. **メッセージングの工夫**
   - 「編集できる」→「仕組みを理解できる」
   - ユーザーの学習意欲を保ちつつ、リスクを回避

**今後の方針:**
- 非エンジニアユーザーには編集を推奨しない
- 開発者には `docs/guides/` でサポート
- コンテンツ追加の要望は、Issue/PRで受け付ける

---

### 💬 エレベーターピッチとメッセージング

#### **教訓9: プロダクトの価値を30秒で伝える技術**

**状況:**
- TOPページのキャッチコピーが抽象的だった: "AI活用の実践スキルを体験を通じて学ぼう"
- プロダクトの価値とターゲットが明確でなかった

**実施した改善:**

##### 1. **エレベーターピッチの作成**
アジャイルサムurai『インセプションデッキ』のフォーマットを使用:

```
【AIツールを使ってみたいけど、難しそうで一歩を踏み出せない非エンジニア】向けの
【Claude Code活用の体験型学習アプリ】である【目指せ！みのるんマスター！】は、
【実際に手を動かしながら、段階的にAI活用スキルを習得】ができ、
【ブログ記事を読むだけの学習】とは違って、
【7つのインタラクティブなコンテンツで、VSCode設定からプロマネ実践まで体験できる】が備わっている。
```

**5つの要素:**
1. **ターゲット**: AIツールを使ってみたいけど、難しそうで一歩を踏み出せない非エンジニア
2. **カテゴリ**: Claude Code活用の体験型学習アプリ
3. **プロダクト名**: 目指せ！みのるんマスター！
4. **主な利点**: 実際に手を動かしながら、段階的にAI活用スキルを習得
5. **差別化要因**: 7つのインタラクティブなコンテンツで、VSCode設定からプロマネ実践まで体験できる

##### 2. **キャッチコピーのアップデート**
```python
<p>難しそう...と思っていたAIツールを、一歩ずつ、あなたのペースで学ぼう</p>
```

**改善のポイント:**
- ✅ ターゲットの感情に寄り添う: "難しそう...と思っていた"
- ✅ ハードルを下げる: "一歩ずつ、あなたのペースで"
- ✅ 共感と安心感を醸成

**学んだこと:**
1. **エレベーターピッチの有効性**
   - 30秒でプロダクトの価値を伝えきる訓練
   - ターゲット・差別化・利点が明確になる
2. **ユーザー視点のメッセージング**
   - 機能説明ではなく、ユーザーの感情と課題に寄り添う
   - "何ができるか" より "どう感じるか"
3. **アジャイル手法の実践**
   - インセプションデッキは、プロダクト開発の初期段階で有効
   - チーム内の認識齟齬を防ぐ

**参考リンク:**
- [アジャイルサムライ - 達人出版会](https://tatsu-zine.com/books/agilesamurai)
- [インセプションデッキとは](https://www.ryuzee.com/contents/blog/7125)

---

### 💰 Streamlit Community Cloudの料金体系

#### **教訓10: 無料ホスティングの持続可能性**

**状況:**
- Streamlit Community Cloudで無料デプロイしたが、いつまで無料で使えるか不明だった
- 課金が必要になるタイミングを知りたかった

**学んだこと:**

##### 1. **無料プランの条件（永続的）**
✅ **条件:**
- ✅ GitHubリポジトリが **public** であること
- ✅ リソース制限: 1GB RAM、1 CPU共有
- ✅ 非アクティブ時は自動スリープ（再アクセスで復帰）

✅ **無料で使い続けられる:**
- 個人プロジェクト、学習用アプリ、オープンソースプロジェクト
- 今回のような学習アプリは永続的に無料で公開可能

##### 2. **課金が必要になるケース**
❌ **以下の場合は有料プラン必須:**
1. **プライベートリポジトリ**
   - 社内限定アプリ、クローズドソースプロジェクト
2. **リソース不足**
   - 大量データ処理、機械学習モデルの実行
   - 1GB RAMを超える処理
3. **高トラフィック**
   - 多数の同時ユーザー、リアルタイムアプリ
4. **カスタムドメイン**
   - `your-app.streamlit.app` ではなく独自ドメイン

##### 3. **有料プラン（Streamlit for Teams）**
- **料金**: $250/月（5ユーザーまで）
- **機能**:
  - プライベートリポジトリ対応
  - 認証・SSO
  - 4GB RAM、2 CPU
  - カスタムドメイン
  - 24/7サポート

**実際の状況:**
- ✅ 今回のアプリ: publicリポジトリ、1GB RAM以内 → **永続的に無料**
- ✅ 同時ユーザー数: 数十人程度なら問題なし
- ✅ 非アクティブスリープ: 学習アプリなら許容範囲

**学んだこと:**
1. **無料ホスティングの条件を理解する**
   - publicリポジトリなら永続的に無料
   - リソース制限は明確（1GB RAM）
2. **プロジェクトの要件と照らし合わせる**
   - 学習アプリ、個人プロジェクト → 無料で十分
   - 社内限定アプリ → 有料プラン検討
3. **代替案の検討**
   - AWS Bedrock連携は別サービス（Streamlitとは独立）
   - 必要に応じて他のホスティングサービスも選択可能

**参考リンク:**
- [Streamlit Community Cloud ドキュメント](https://docs.streamlit.io/streamlit-community-cloud)
- [料金プラン比較](https://streamlit.io/cloud)

---

### 📊 ハッカソン成果報告のドキュメント化

#### **教訓11: プロジェクトの学びを資産化する**

**状況:**
- 3日間のハッカソンで多くの学びがあった
- PLAN.md、SPEC.md、TODO.md、KNOWLEDGE.mdに情報が分散していた
- 成果を報告資料としてまとめる必要があった

**実施したこと:**

##### 1. **ドキュメント構成の設計**
```
docs/hackathon-report/
├── README.md                    # 成果サマリー
├── 01_project-overview.md       # プロジェクト概要
├── 02_learning-contents.md      # 学習コンテンツ詳細
├── 03_technical-learnings.md    # 技術的教訓
├── 04_development-process.md    # 開発プロセス
└── slides/
    └── presentation.md          # Marpスライド（30ページ）
```

##### 2. **情報の集約と構造化**
- **情報源**: PLAN.md、TODO.md、KNOWLEDGE.md、SPEC-*.md、contents.yaml、README.md
- **構造化**: 章立て、見出し、箇条書きで整理
- **視覚化**: 図表、コードブロック、アイコンで可読性向上

##### 3. **スライド作成（Marp形式）**
```markdown
---
marp: true
theme: default
paginate: true
---

# 目指せ！みのるんマスター！
**Claude Code活用の体験型学習アプリ**

---

## 📋 アジェンダ
1. プロジェクト概要
2. 7つの学習コンテンツ
...
```
- **30ページ**: 概要、コンテンツ、技術、プロセス、成果、今後の展開
- **変換可能**: `marp presentation.md --pdf` でPDF化

**学んだこと:**
1. **プロジェクトの学びは資産**
   - ドキュメント化することで、チームや社内に共有できる
   - 次のプロジェクトに活かせる
2. **情報の集約と構造化**
   - 散在した情報を1箇所にまとめる
   - 章立て、見出しで階層構造を作る
3. **複数フォーマットの用意**
   - テキスト（マークダウン）: 詳細な情報、検索可能
   - スライド（Marp）: プレゼン用、視覚的
4. **Marpの有効性**
   - Markdownでスライドを作成できる
   - バージョン管理しやすい（テキストファイル）
   - PDF/HTML/PPTXに変換可能

**今後の活用:**
- 社内勉強会での発表
- 技術ブログの執筆
- 次のハッカソンの参考資料
- オンボーディング資料として活用

**参考リンク:**
- [Marp 公式サイト](https://marp.app/)
- [Marp CLI ドキュメント](https://github.com/marp-team/marp-cli)

---

**更新履歴:**
- 2026-03-04: 初版作成（デプロイ・UI・Git関連の教訓）
- 2026-03-05: Qiita記事取得方法を追加
- 2026-03-06: 通知設定コンテンツの追加と実装方法を記録
- 2026-03-06: フォルダ構成のルールとリファクタリング記録を追加
- 2026-03-06: OGP最適化、YAML編集リスク、エレベーターピッチ、Streamlit料金体系、ハッカソン成果報告を追加
