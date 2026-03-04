# TODO.md - タスク管理

## 未着手（Day 2予定）

### IAMユーザー作成（議事録生成機能のデプロイ用）
- [ ] AWS Console（https://console.aws.amazon.com/iam/）でIAMユーザー作成
  - User name: `gijiroku-man`
  - Console accessは**オフ**
  
- [ ] ポリシー作成・アタッチ
  - Policy name: `BedrockInvokeModelOnly`
  - JSON:
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "bedrock:InvokeModel",
                "Resource": "arn:aws:bedrock:us-east-1::foundation-model/us.anthropic.claude-3-5-sonnet-20241022-v2:0"
            }
        ]
    }
    ```
  
- [ ] アクセスキー発行
  - Security credentials → Create access key
  - Use case: Application running outside AWS
  - アクセスキーIDとシークレットキーをコピー
  
- [ ] Streamlit Community Cloud の Secrets に設定
  - Settings → Secrets
  - 以下を追加:
    ```toml
    AWS_ACCESS_KEY_ID = "発行したアクセスキーID"
    AWS_SECRET_ACCESS_KEY = "発行したシークレットキー"
    AWS_DEFAULT_REGION = "us-east-1"
    ```

- [ ] デプロイ後の動作確認
  - 議事録生成機能が動作するか確認

### Claude API連携（経費精算機能）
- [ ] 経費精算ページにもClaude API連携を実装
- [ ] CSVファイルの解析機能
- [ ] 勘定科目の自動マッピング
- [ ] Markdown出力機能

### 音声入力機能（Web Speech API）
- [ ] ブラウザのWeb Speech API統合
- [ ] 音声→テキスト変換
- [ ] PLAN.mdへの自動入力

### GitHub連携
- [ ] GitHubリポジトリへの自動push機能
- [ ] 4ドキュメント（PLAN/SPEC/TODO/KNOWLEDGE）の自動コミット

### 発表資料準備
- [ ] ハッカソン発表用のスライド作成
- [ ] デモシナリオ作成
- [ ] できること・できないことの整理

---

## 進行中（Day 1）
（現在進行中のタスクはありません）

---

## 完了（Day 1）

### 基本構造
- [x] プロジェクト初期化
- [x] Git/GitHub設定
- [x] PLAN.md作成
- [x] SPEC.md作成
- [x] reason.md作成（freee API制約）
- [x] hackathon-cost.md作成（費用記録）

### トップページ
- [x] アプリ名決定（「目指せ！みのるんマスター！」）
- [x] contents.yaml作成（学習コンテンツ管理）
- [x] トップページUI実装
- [x] カード形式の一覧表示
- [x] メタ学習要素（YAMLヒント）
- [x] レスポンシブデザイン

### 学習コンテンツ1: 経費精算を5分で終わらせる
- [x] ページ作成（`pages/01_💰_経費精算.py`）
- [x] CSVアップロード機能
- [x] データプレビュー表示

### 学習コンテンツ2: プチ仕様駆動開発を体験しよう
- [x] ページ作成（`pages/02_📝_プチ仕様駆動開発体験.py`）
- [x] 4ドキュメントの説明
- [x] テンプレート例の提示
- [x] 実践フォームの実装

### 学習コンテンツ3: 会議の議事録を自動生成
- [x] ページ作成（`pages/03_📋_会議議事録生成.py`）
- [x] 専門領域入力フォーム
- [x] 参加者入力フォーム（複数区切り文字対応）
- [x] 文字起こしデータ入力エリア
- [x] AWS Bedrock連携実装
- [x] 議事録生成機能（ローカル動作確認済み）
- [x] Markdownダウンロード機能

### デプロイ
- [x] Streamlit Community Cloudにデプロイ
- [x] Python バージョン指定（3.11）
- [x] requirements.txt作成
- [x] .gitignore設定

---

## ブロッカー・懸念事項

### IAM権限不足
- Claude Codeユーザー（`claude-code-user`）にIAM管理権限がない
- → AWS Consoleで手動作成が必要

### コスト管理
- Day 1実績: $5.25（約693円）
- 予算残: 29,307円（97.7%）
- 問題なし

---

## 次回セッション時のアクション

1. IAMユーザー `gijiroku-man` を作成（上記手順）
2. アクセスキーをStreamlit Secretsに設定
3. デプロイ先で議事録生成機能をテスト
4. 経費精算機能のClaude API連携実装
5. 音声入力機能の実装検討

---

## 更新履歴
- 2026-03-04 18:00: Day 1完了時点でのタスク整理
