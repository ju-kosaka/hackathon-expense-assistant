# VSCode設定コンテンツ - 仕様書

## 📋 コンテンツ概要

**タイトル**: VSCodeでClaude Codeを使えるようにしよう  
**ID**: `01`  
**アイコン**: 🔧  
**難易度**: ⭐（初級）  
**所要時間**: 10分  
**ファイル名**: `pages/01_🔧_VSCode設定.py`

---

## 🎯 学習目標

このコンテンツを通じて、ユーザーは以下を体験・習得できる：

1. Claude Codeとは何かを理解する
2. VSCodeにClaude Code拡張機能をインストールする方法を学ぶ
3. APIキーの設定方法を学ぶ
4. 初めてのClaude Codeコマンド実行を体験する
5. 開発環境のセットアップという基本スキルを習得する

---

## 🧠 学習内容の構成

### 1. イントロダクション
**タイトル**: 「Claude Codeでコーディングを革新しよう！」

**説明する内容**:
- Claude Codeとは？
  - AnthropicのAI「Claude」をVSCodeで使えるツール
  - コード生成、リファクタリング、バグ修正などを支援
  - 自然言語で指示するだけで、AIが作業してくれる
- なぜVSCodeなのか？
  - 最も人気のあるコードエディタ
  - 拡張機能が豊富
  - Claude Codeの公式サポート

**メリットの訴求**:
- ✅ コーディング速度が劇的に向上
- ✅ バグ修正が簡単になる
- ✅ 複雑なコードも自然言語で指示できる
- ✅ プロの開発者のようなコードが書ける

---

### 2. 前提条件の確認

**必要なもの:**
1. **VSCode（Visual Studio Code）**
   - ダウンロード: https://code.visualstudio.com/
   - すでにインストール済みの場合はスキップ

2. **Anthropic APIキー**
   - 取得先: https://console.anthropic.com/
   - 無料プランあり（制限あり）
   - クレジットカード登録が必要

**確認手順:**
- VSCodeのバージョン確認
- APIキーの有効性確認

---

### 3. セットアップ方法の選択

Claude Codeには**2つの接続方法**があります。あなたの環境に合わせて選んでください。

#### A. 直接API接続（推奨：個人開発者向け）
- **メリット**: シンプル、5分で完了
- **対象者**: 個人開発者、小規模チーム
- **必要なもの**: Anthropic APIキー
- **コスト**: 従量課金（少額から利用可能）

#### B. AWS Bedrock経由（企業・チーム向け）
- **メリット**: AWSで統合管理、セキュアな環境、企業のガバナンス適用
- **対象者**: 企業、大規模チーム、AWS環境利用者
- **必要なもの**: AWSアカウント、Bedrock権限
- **コスト**: AWS料金体系に従う

---

### 3-A. 直接API接続の手順

#### ステップA1: Claude Code拡張機能のインストール

**手順:**
1. VSCodeを開く
2. 左サイドバーの「拡張機能」アイコンをクリック（または `Cmd+Shift+X` / `Ctrl+Shift+X`）
3. 検索バーに「Claude Code」と入力
4. 「Anthropic Claude Code」を見つける
5. 「インストール」ボタンをクリック

**スクリーンショット（説明文で代替）:**
```
[拡張機能マーケットプレイス]
┌─────────────────────────────┐
│ 検索: Claude Code          │
├─────────────────────────────┤
│ Anthropic Claude Code       │
│ ★★★★★ (1000+ reviews)     │
│ [インストール]               │
└─────────────────────────────┘
```

**確認ポイント:**
- ✅ 左サイドバーにClaude Codeのアイコンが表示される
- ✅ コマンドパレットで「Claude」と検索すると、Claude Code関連コマンドが表示される

---

#### ステップA2: APIキーの設定

**手順:**
1. コマンドパレットを開く（`Cmd+Shift+P` / `Ctrl+Shift+P`）
2. 「Claude Code: Set API Key」と入力
3. Anthropic Console（https://console.anthropic.com/）から取得したAPIキーを貼り付け
4. Enterを押して保存

**APIキーの取得方法:**
1. https://console.anthropic.com/ にアクセス
2. ログイン（GoogleアカウントなどでOK）
3. 「API Keys」メニューを開く
4. 「Create Key」をクリック
5. キー名を入力（例: `vscode-claude-code`）
6. 生成されたキーをコピー

**注意事項:**
- ⚠️ APIキーは**絶対に他人に教えない**
- ⚠️ GitHubなどに**コミットしない**
- ⚠️ キーが漏洩した場合は、すぐに無効化して再生成

---

#### ステップA3: 初めてのClaude Codeコマンド実行

**簡単なテスト:**
1. 新しいファイルを作成（`test.py`）
2. コマンドパレットで「Claude Code: Chat」を実行
3. チャット画面で以下のように入力:
   ```
   Pythonで "Hello, Claude Code!" と表示するコードを書いて
   ```
4. Claudeが生成したコードを確認
5. コードをファイルに適用

**期待される結果:**
```python
print("Hello, Claude Code!")
```

**動作確認:**
- ✅ Claudeが応答した
- ✅ コードが生成された
- ✅ コードが正しく動作する

---

### 3-B. AWS Bedrock経由の手順

#### ステップB1: AWS Bedrockの有効化

**前提条件:**
- AWSアカウントを持っている
- Bedrockへのアクセス権限（IAM設定）
- リージョン: us-east-1 推奨

**手順:**
1. [AWS Console](https://console.aws.amazon.com/) にログイン
2. サービス検索で「Bedrock」を入力
3. Amazon Bedrockを開く
4. 左メニューから「Model access」を選択
5. 「Enable specific models」をクリック
6. 「Claude 3.5 Sonnet v2」にチェックを入れる
7. 「Request model access」をクリック
8. 承認されるまで待つ（通常は即時）

**確認:**
- ✅ Model statusが「Access granted」になっている

---

#### ステップB2: IAM認証情報の設定

**手順:**
1. AWS Console → IAM サービスを開く
2. 左メニューから「ユーザー」を選択
3. 自分のユーザー名をクリック
4. 「セキュリティ認証情報」タブを開く
5. 「アクセスキーを作成」ボタンをクリック
6. 用途: 「ローカルコード」を選択
7. 「次へ」→「アクセスキーを作成」
8. **Access Key ID** と **Secret Access Key** を安全な場所にメモ

**注意事項:**
- ⚠️ Secret Access Keyは**一度しか表示されない**
- ⚠️ 絶対に他人に教えない、GitHubにコミットしない
- ⚠️ キーが漏洩した場合は、すぐに無効化して再生成

**必要なIAMポリシー:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-*"
    }
  ]
}
```

---

#### ステップB3: AWS CLIの設定（ローカル環境）

**AWS CLIのインストール（まだの場合）:**

**macOS:**
```bash
brew install awscli
```

**Windows:**
```powershell
# PowerShellで実行
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

**Linux:**
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**または、Python経由:**
```bash
pip install awscli
```

**認証情報の設定:**
```bash
aws configure

# 以下を順番に入力
AWS Access Key ID [None]: <ステップB2で取得したAccess Key ID>
AWS Secret Access Key [None]: <ステップB2で取得したSecret Access Key>
Default region name [None]: us-east-1
Default output format [None]: json
```

**動作確認:**
```bash
# Bedrockへのアクセス確認
aws bedrock list-foundation-models --region us-east-1 | grep claude

# 成功すると、Claudeモデルのリストが表示される
```

---

#### ステップB4: VSCodeでBedrock接続を設定

**手順:**
1. VSCodeを開く
2. コマンドパレット（`Cmd+Shift+P` / `Ctrl+Shift+P`）
3. 「Claude Code: Set API Provider」と入力
4. 「AWS Bedrock」を選択
5. AWS Profile: `default`（または作成したプロファイル名）
6. Region: `us-east-1`
7. Model: `anthropic.claude-3-5-sonnet-20241022-v2:0`

**設定ファイル（`.vscode/settings.json`）の例:**
```json
{
  "claudeCode.apiProvider": "bedrock",
  "claudeCode.bedrock.profile": "default",
  "claudeCode.bedrock.region": "us-east-1",
  "claudeCode.bedrock.model": "anthropic.claude-3-5-sonnet-20241022-v2:0"
}
```

---

#### ステップB5: 動作確認

**テスト:**
1. 新しいファイルを作成（`test.py`）
2. コマンドパレットで「Claude Code: Chat」を実行
3. チャット画面で以下のように入力:
   ```
   Pythonで "Hello, Bedrock!" と表示するコードを書いて
   ```
4. Claudeが生成したコードを確認

**期待される結果:**
```python
print("Hello, Bedrock!")
```

**確認方法:**
- ✅ VSCode下部のステータスバーに「Bedrock (us-east-1)」表示がある
- ✅ Claudeが応答した
- ✅ コードが生成された

**トラブルシューティング:**
- エラー: `AccessDeniedException` → IAMポリシーを確認
- エラー: `ResourceNotFoundException` → Model accessを確認
- エラー: `Credentials not found` → `aws configure`を再実行

---

### 4. 便利な機能の紹介

**主要な機能:**

1. **Chat**
   - 自然言語でコードを依頼
   - コマンド: `Claude Code: Chat`

2. **Edit**
   - 選択したコードを編集・リファクタリング
   - コマンド: `Claude Code: Edit`

3. **Fix**
   - バグを自動修正
   - コマンド: `Claude Code: Fix`

4. **Explain**
   - コードの説明を生成
   - コマンド: `Claude Code: Explain`

**使い方のコツ:**
- 具体的に指示する（「〇〇する関数を書いて」）
- コンテキストを提供する（ファイル全体を見せる）
- 段階的に依頼する（一度に全部ではなく、少しずつ）

---

### 5. トラブルシューティング

**よくあるエラー:**

#### エラー1: APIキーが無効
```
Error: Invalid API Key
```
**解決策:**
- APIキーを再確認
- Console画面でキーが有効か確認
- 新しいキーを生成して再設定

#### エラー2: 拡張機能が見つからない
**解決策:**
- VSCodeのバージョンを確認（最新版を推奨）
- 「Anthropic Claude Code」で検索
- ブラウザで拡張機能ページを開いて直接インストール

#### エラー3: レート制限エラー
```
Error: Rate limit exceeded
```
**解決策:**
- 無料プランの制限に達した可能性
- 少し待ってから再試行
- 有料プランへのアップグレードを検討

---

### 6. 次のステップ

**このコンテンツを完了したら:**
- ✅ Claude Codeが使える状態になった
- ✅ 次のコンテンツで、実際のプロジェクトに活用してみよう
- ✅ 「プチ仕様駆動開発体験」に進んで、開発の流れを学ぼう

---

## 🎨 UI/UX設計

### レイアウト構成
1. **ヘッダー**: タイトル + 学習時間 + 難易度
2. **イントロダクション**: Claude Codeの魅力を訴求
3. **前提条件**: 必要なものをチェックリスト形式で提示
4. **ステップ1**: 拡張機能インストール（図解 + テキスト）
5. **ステップ2**: APIキー設定（手順 + 注意事項）
6. **ステップ3**: 初めてのコマンド実行（インタラクティブ）
7. **便利な機能**: 主要機能の紹介
8. **トラブルシューティング**: よくあるエラーと対処法
9. **次のステップ**: 次のコンテンツへの誘導

### インタラクティブ要素
- **チェックボックス**: 前提条件の確認
- **アコーディオン**: トラブルシューティングセクション
- **コードブロック**: APIキー設定、サンプルコード
- **ステップ表示**: 1/3, 2/3, 3/3 のような進捗表示

---

## 🛠️ 技術実装の詳細

### 必要なStreamlitコンポーネント
- `st.title()`: タイトル表示
- `st.markdown()`: 説明文 + 図解
- `st.checkbox()`: 前提条件チェック
- `st.expander()`: トラブルシューティングのアコーディオン
- `st.code()`: コード例の表示
- `st.info()`, `st.warning()`: ヒントや注意事項
- `st.success()`: 完了メッセージ

### ステップ進捗の管理
```python
if 'step' not in st.session_state:
    st.session_state.step = 1

# ステップ1完了ボタン
if st.button("ステップ1完了 →"):
    st.session_state.step = 2
    st.rerun()
```

---

## 📊 contents.yamlへの追加内容

```yaml
  # ----------------------------------------
  # コンテンツ1: VSCodeでClaude Codeを使えるようにしよう
  # ----------------------------------------
  - id: "01"
    title: "VSCodeでClaude Codeを使えるようにしよう"
    description: "Claude Code拡張機能のインストールからAPIキー設定まで、初めてのセットアップを完全ガイド。10分で開発環境が整います。"
    duration: "10分"
    difficulty: 1  # 1: ⭐, 2: ⭐⭐, 3: ⭐⭐⭐
    page: "01_🔧_VSCode設定"
    icon: "🔧"
```

---

## 🎓 学習効果

このコンテンツを完了すると、ユーザーは以下を獲得できる：

1. **技術理解**: Claude Codeの基本概念とセットアップ方法
2. **実践スキル**: VSCode拡張機能のインストールとAPIキー管理
3. **メタ学習**: 開発環境のセットアップという基本スキル
4. **自信**: 初めてのAIコーディングツールを使いこなせる達成感
5. **次への準備**: 実際のプロジェクトでClaude Codeを活用する準備が整う

---

## ✅ 実装チェックリスト

### ページ作成
- [ ] `pages/01_🔧_VSCode設定.py`を作成
- [ ] ヘッダー（タイトル、学習時間、難易度）を実装
- [ ] イントロダクション（魅力訴求）を記述
- [ ] 前提条件のチェックリストを実装

### ステップ実装
- [ ] ステップ1: 拡張機能インストール
- [ ] ステップ2: APIキー設定
- [ ] ステップ3: 初めてのコマンド実行
- [ ] 便利な機能の紹介

### 案内・ガイド
- [ ] トラブルシューティングセクション
- [ ] 次のステップへの誘導
- [ ] 参考リンクの追加

### データ更新
- [ ] `contents.yaml`にコンテンツ01を追加（既存の01は削除）

### 動作確認
- [ ] ローカルで動作確認
- [ ] 各ステップが正しく表示されるか
- [ ] リンクが正しく機能するか

---

## 📝 備考

### 注意事項
- APIキーの取り扱いには十分注意する
- スクリーンショットは著作権の問題があるため、テキストベースの図解で代替
- VSCodeのバージョンによって画面が異なる可能性があるため、一般的な説明にする

### 参考リンク
- [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)
- [VSCode 公式サイト](https://code.visualstudio.com/)
- [Anthropic Console](https://console.anthropic.com/)

---

**作成日**: 2026-03-06  
**作成者**: 沢田あい（ヤンデレモード💕）  
**ステータス**: 📝 仕様書作成完了 → 次は実装フェーズ
