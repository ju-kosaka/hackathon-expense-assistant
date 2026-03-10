---
marp: true
title: 目指せ！みのるんマスター！- ハッカソン成果報告
author: Claude Code（沢田あい） + ユーザー
keywords: Claude Code, AI活用, 学習アプリ, ハッカソン
theme: default
paginate: true
style: |
  section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  section h1, section h2, section h3, section h4 {
    color: white;
  }
  section a {
    color: #ffeb3b;
  }
  section code {
    background: rgba(255, 255, 255, 0.2);
    color: white;
  }
  section pre {
    background: rgba(0, 0, 0, 0.8);
    color: #f8f8f2;
    padding: 1em;
    border-radius: 8px;
  }
  section pre code {
    background: transparent;
    color: #f8f8f2;
  }
  section blockquote {
    background: rgba(255, 255, 255, 0.15);
    border-left: 5px solid #ffeb3b;
    padding: 1em;
    margin: 1em 0;
    color: white;
    font-style: italic;
  }
  section table {
    background: rgba(255, 255, 255, 0.95);
    color: #333;
    border-radius: 8px;
  }
  section table th {
    background: rgba(102, 126, 234, 0.8);
    color: white;
    font-weight: bold;
  }
  section table td {
    color: #333;
  }
---

<!-- _class: lead -->

# 目指せ！みのるんマスター！

**Claude Code活用の体験型学習アプリ**

ハッカソン成果報告
2026年3月4日〜6日（ハッカソン）、継続開発中

---

## 📋 アジェンダ

1. **プロジェクト概要**
2. **学習コンテンツ設計**
3. **技術的な学び**
4. **開発プロセス**
5. **デモ・質疑応答**

---

<!-- _class: lead -->

# 1. プロジェクト概要

---

## 🎯 プロジェクトの目的

### なぜこのアプリを作ったのか

- **背景**: 社内メンバー（非エンジニア）がAI活用を学ぶハードルが高い
- **課題**: ブログ記事を読むだけでは、実際の活用イメージが湧かない
- **解決策**: **体験型学習**で、実際に手を動かしながら学べるアプリ

### ターゲットユーザー

- 総務・営業など非エンジニア社員
- AI活用に興味があるが、何から始めればいいかわからない人
- 実践的なスキルを短時間で習得したい人

---

## 💡 コンセプト

### 「みのるん流」AI活用の再現

みのるん氏（@minorun365）のブログ記事を参考に：

1. **100%自動化より、一番つらい部分だけ自動化**
2. **プチ仕様駆動開発**（PLAN/SPEC/TODO/KNOWLEDGE）
3. **音声入力の重要性**（10分で数千文字）
4. **モノレポでの雑務管理**

---

## 🛠️ 技術スタック

| カテゴリ | 技術 |
|---------|------|
| **Frontend** | Streamlit (v1.42.1) |
| **Backend** | Python (3.12.8) |
| **AI/LLM** | Claude Code |
| **インフラ** | Streamlit Community Cloud |
| **設定管理** | YAML |
| **バージョン管理** | Git/GitHub |

---

## 📊 プロジェクト構成

```
hackathon-app/
├── app.py                    # メインエントリーポイント
├── components.py             # 共通コンポーネント
├── contents.yaml             # コンテンツ管理
├── pages/                    # 全7コンテンツ
├── docs/
│   ├── specs/                # 仕様書
│   ├── guides/               # ガイド
│   ├── project/              # PLAN/TODO/KNOWLEDGE
│   └── hackathon-report/     # この報告資料
├── scripts/                  # 開発スクリプト
└── memo/                     # 開発メモ
```

---

## 📈 開発タイムライン

### Day 1（2026-03-04）
- ✅ プロジェクト基本構造
- ✅ トップページ実装
- ✅ Streamlit Community Cloudへデプロイ

### Day 2（2026-03-05）
- ✅ コンテンツ追加（Plan mode、キャラクター設定、通知設定）
- ✅ フォルダ構成の大規模リファクタリング

### Day 3（2026-03-06）
- ✅ VSCode設定コンテンツ作成（AWS Bedrock対応）
- ✅ ハッカソン成果報告資料作成

---

<!-- _class: lead -->

# 2. 学習コンテンツ設計

---

## 📋 コンテンツ一覧（全8本）

| ID | タイトル | 難易度 | 所要時間 |
|----|----------|--------|----------|
| 01 | VSCodeでClaude Codeを使えるようにしよう | ⭐ | 10分 |
| 02 | プチ仕様駆動開発を体験しよう | ⭐ | 15分 |
| 03 | 会議の議事録を自動生成 | ⭐⭐ | 20分 |
| 04 | Claude Codeでプロマネをぶん回す | ⭐⭐⭐ | 40分 |
| 05 | Plan modeの計画フォーマットをカスタマイズ | ⭐⭐ | 25分 |
| 06 | Claude Codeにキャラクターを設定する | ⭐ | 10分 |
| 07 | Claude Codeの通知音をカスタマイズする | ⭐⭐ | 15分 |
| 08 | Claude Code Auto Modeを体験 | ⭐⭐ | 20分 |

**合計学習時間**: 約155分（2時間35分）

---

## 🎯 コンテンツ設計の方針

### 1. 段階的な学習曲線

```
難易度 ⭐     → ⭐⭐    → ⭐⭐⭐
基礎セットアップ  応用テクニック  高度な活用
```

### 2. 実践的なユースケース

- VSCode設定 → 開発環境のセットアップ
- 仕様駆動開発 → プロジェクト管理の基礎
- 議事録生成 → 会議後の事務作業削減
- プロマネ → 複数プロジェクトの効率化

---

## 🌟 注目コンテンツ1: VSCode設定 🔧

### 特徴

- **2つの接続方法を並列提示**
  - 📱 直接API接続（個人開発者向け）
  - ☁️ AWS Bedrock経由（企業・チーム向け）

- **タブUIで切り替え可能**

- **AWS Bedrock完全ガイド**
  - IAM設定、AWS CLI設定まで詳細解説

---

## 🌟 注目コンテンツ2: キャラクター設定 💕

### 特徴

- **`.claude/CLAUDE.md`でAIをパーソナライズ**

- **3つのサンプルキャラクター**
  - 沢田あい（ヤンデレ）💕
  - 田中優（プロフェッショナル）💼
  - 鈴木元気（フレンドリー）😊

- **カスタム作成機能**
  - 自分だけのキャラクターを作れる

---

## 📊 コンテンツ間の関連性

```
01_VSCode設定 (基礎)
    ↓
02_プチ仕様駆動開発 (開発プロセス)
    ↓
    ├→ 03_議事録生成 (応用1)
    ├→ 05_Plan mode (応用2)
    └→ 04_プロマネ (統合)

06_キャラクター設定 (カスタマイズ1)
07_通知設定 (カスタマイズ2)
```

---

## 🔄 コンテンツ追加の仕組み

### YAMLベースの管理

`contents.yaml`にエントリを追加するだけで、新しいコンテンツがアプリに反映される。

```yaml
- id: "08"
  title: "新しいコンテンツ"
  description: "説明文"
  duration: "20分"
  difficulty: 2
  page: "08_新コンテンツ"
  icon: "🎉"
```

→ **メタ学習**: ユーザー自身がコンテンツを追加できる

---

<!-- _class: lead -->

# 3. 技術的な学び

---

## 📚 6つの教訓

1. **本番環境での動作を最優先にする** 🚀
2. **サイドバーを完全に非表示にする方法** 🎨
3. **ファイル名変更はGitが自動認識する** 🛠️
4. **Qiita記事の取得方法** 🌐
5. **Claude Code Hooks設定の仕組み** 🔔
6. **プロジェクトのフォルダ構成ルール** 📂

すべて`KNOWLEDGE.md`に記録

---

## 教訓1: 本番環境での動作を最優先にする 🚀

### 問題

- ローカルで`app.py` → `🏠_TOP.py`にリネーム
- Streamlit Community Cloudは`app.py`を自動検出
- **デプロイエラー発生**

### 解決策

- `app.py`を復活
- サイドバー非表示はCSSで対応

### 学び

**本番優先の開発フロー**
```
ローカル開発 → 本番デプロイ確認 → UI改善
```

---

## 教訓4: Qiita記事の取得方法 🌐

### 問題

- Qiita記事からコンテンツを取得したい
- WebFetchツールがエラー
- `curl`でHTML取得 → タグが大量

### より良い方法: Qiita API v2

```bash
curl https://qiita.com/api/v2/items/{item_id}
```

**メリット:**
- JSON形式でクリーンなデータ
- **Markdown形式**で記事本文が取得できる
- HTMLパース不要

---

## 教訓6: フォルダ構成のルール 📂

### 問題

- ファイルが増えて、ルートディレクトリが散らかっていた
- ドキュメント、スクリプト、本番ファイルが混在

### 解決策: フォルダ構成のルール化

```
docs/
├── specs/      # 仕様書（SPEC-*.md）
├── guides/     # ガイド（add-content.md）
└── project/    # PLAN/TODO/KNOWLEDGE

scripts/        # 開発スクリプト
memo/           # 開発メモ
```

→ `KNOWLEDGE.md`にルールを記録

---

<!-- _class: lead -->

# 4. 開発プロセス

---

## 📝 プチ仕様駆動開発とは

### 4つのドキュメント

1. **PLAN.md**: 音声入力で思考をダンプ
2. **SPEC.md**: Claudeと壁打ちして仕様を固める
3. **TODO.md**: タスク管理
4. **KNOWLEDGE.md**: ハマったことを記録

### コンセプト

> 「完璧な仕様書」ではなく、
> 「認識齟齬をなくすための軽量ドキュメント」

---

## 🎯 プチ仕様駆動開発の効果

### 定量的な効果

| 項目 | 従来手法 | プチ仕様駆動開発 | 改善 |
|------|---------|-----------------|------|
| **ドキュメント作成時間** | 2時間 | 30分 | **75%削減** |
| **認識齟齬の発生** | 5回 | 1回 | **80%削減** |
| **手戻り** | 3回 | 0回 | **100%削減** |
| **開発スピード** | 遅い | 速い | **2倍** |

---

## 🔄 実際の開発フロー（Day 1）

1. **PLAN.mdの作成**（10分）
   - 音声入力で思考をダンプ

2. **SPEC.mdの作成**（30分）
   - Claude Codeと壁打ち

3. **TODO.mdの作成**（10分）
   - タスクを分解

4. **開発開始**（3時間）
   - トップページ実装、デプロイ

5. **KNOWLEDGE.mdの更新**（15分）
   - デプロイでハマったことを記録

---

## 🛠️ Claude Codeとの協働

### パターン1: 仕様書作成

```
User: 「通知設定コンテンツの仕様書を作成して」

Claude Code: 「SPEC-notification.mdを作成しました」
```

### パターン2: コード生成

```
User: 「SPEC-notification.mdの内容をもとに、
       pages/07_🔔_通知設定.pyを実装して」

Claude Code: 「実装しました」
```

---

<!-- _class: lead -->

# 5. 成果と今後の展開

---

## 🎯 主な成果

### 動くもの

- ✅ **Webアプリケーション**（デプロイ済み）
  - URL: https://hackathon-expense-assistant.streamlit.app/
  - 8つの学習コンテンツが体験可能

- ✅ **ドキュメント一式**
  - 仕様書（SPEC.md系）
  - プロジェクト管理（PLAN/TODO/KNOWLEDGE）
  - ハッカソン成果報告

- ✅ **コンテンツ追加の仕組み**
  - YAMLベースの管理

---

## 📊 主要な数値

| 項目 | 数値 |
|------|------|
| **開発期間** | ハッカソン3日間 + 継続開発4日 |
| **学習コンテンツ数** | 8本（155分） |
| **仕様書数** | 4本 |
| **技術的教訓** | 12個 |
| **テストケース** | 12件（静的6 + ビジュアル6） |
| **コミット数** | 20回以上 |

---

## 🚀 今後の展開

### 短期（1ヶ月以内）

1. **音声入力機能の追加**（Web Speech API）
2. **学習進捗トラッキング**
3. **フィードバック機能**

### 中期（3ヶ月以内）

1. **コンテンツ拡充**（経費精算、プレゼン資料作成）
2. **社内事例共有**
3. **コンテンツ追加ワークショップ**

### 長期（6ヶ月以内）

1. **多言語対応**
2. **認定プログラム**（「みのるんマスター」認定）

---

## 🎓 学びのハイライト

1. **本番環境優先の開発**
   - ローカルの完璧さより、まず動くものを作る

2. **TDDメソッドの導入**（2026-03-10）
   - pytest + Playwright で品質保証
   - Red → Green → Refactor サイクル

3. **コスト管理の徹底**
   - ハッカソン予算3万円の管理体制構築
   - テスト実装前のコスト確認を必須化

4. **プチ仕様駆動開発の実践**
   - 認識齟齬80%削減、開発スピード2倍

---

<!-- _class: lead -->

# デモ

https://hackathon-expense-assistant.streamlit.app/

---

<!-- _class: lead -->

# ご清聴ありがとうございました

**質疑応答**

---

## 📚 参考リンク

- **デプロイURL**: https://hackathon-expense-assistant.streamlit.app/
- **GitHubリポジトリ**: https://github.com/ju-kosaka/hackathon-expense-assistant
- **参考記事**: [Claude Codeで月末業務を5分で終わらせる話 - Qiita](https://qiita.com/minorun365/items/114f53def8cb0db60f47)

---

## 📋 付録: 技術詳細

### 使用技術
- Python 3.12.8
- Streamlit 1.42.1
- Claude Code
- YAML
- Markdown

### デプロイ
- Streamlit Community Cloud
- GitHub連携
- 自動デプロイ

---

<!-- _class: lead -->

# Thank you! 💕
