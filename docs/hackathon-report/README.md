# ハッカソン成果報告

**プロジェクト名**: 目指せ！みのるんマスター！  
**サブタイトル**: Claude Code活用の体験型学習アプリ  
**開発期間**: 2026年3月4日〜6日（ハッカソン）、継続開発中  
**デプロイURL**: https://hackathon-expense-assistant.streamlit.app/

---

## 📋 報告資料の構成

この報告資料は、ハッカソンで開発した「目指せ！みのるんマスター！」の成果をまとめたものです。

### 📄 テキスト版ドキュメント

1. **[01_project-overview.md](./01_project-overview.md)**  
   プロジェクト概要、開発背景、コンセプト、技術スタック

2. **[02_learning-contents.md](./02_learning-contents.md)**  
   学習コンテンツ設計（全8コンテンツの詳細）

3. **[03_technical-learnings.md](./03_technical-learnings.md)**  
   技術的な学び（6つの教訓）

4. **[04_development-process.md](./04_development-process.md)**  
   開発プロセス（プチ仕様駆動開発の実践）

### 🎨 プレゼンテーション資料

- **[slides/presentation.md](./slides/presentation.md)**  
  Marp形式のスライド（テキスト版から生成）

---

## 🎯 プロジェクトの概要（エグゼクティブサマリー）

### 何を作ったか
**「目指せ！みのるんマスター！」** - Claude Code活用の体験型学習アプリ

非エンジニアが**実際に手を動かしながら**AI活用を学べるWebアプリケーション。
みのるん氏（@minorun365）のブログ記事やITmedia記事を参考に、Claude Codeの活用方法を8つの学習コンテンツで体験できる。

### 主な成果
- ✅ **8つの学習コンテンツを実装**（VSCode設定、仕様駆動開発、通知設定、Auto Modeなど）
- ✅ **YAMLベースのコンテンツ管理**で、非エンジニアでも追加可能
- ✅ **Streamlit Community Cloudにデプロイ**し、誰でもアクセス可能
- ✅ **プチ仕様駆動開発**を実践し、PLAN/SPEC/TODO/KNOWLEDGEを完備
- ✅ **12の技術的教訓**を記録し、次のプロジェクトに活かせる知見を蓄積
- ✅ **TDDメソッド（pytest + Playwright）を導入**、テストファースト開発を実践

### 学びのハイライト
1. **本番環境優先の開発**：ローカルの完璧さより、まず動くものを作る
2. **フォルダ構成のルール化**：docs/specs、docs/project、scripts/で整理
3. **外部API活用**：Qiita API v2でMarkdown形式のコンテンツ取得
4. **通知機能の実装**：osascriptでmacOS通知をカスタマイズ
5. **TDDメソッドの導入**：Red→Green→Refactorサイクルで品質保証
6. **コスト管理の徒底**：ハッカソン予算（3万円）の管理体制構築

---

## 📊 主要な数値

- **開発期間**: ハッカソン3日間 + 継続開発（4日）
- **学習コンテンツ数**: 8本（合計155分）
- **仕様書数**: 4本（SPEC.md + SPEC-{vscode-setup, setcharacter, notification}.md）
- **技術的教訓**: 12つ（KNOWLEDGE.mdに記録）
- **テストケース**: 12件（静的テスト6 + ビジュアルテスト6）
- **コミット数**: 20回以上
- **使用技術**: Python, Streamlit, Claude Code, YAML, Markdown, pytest, Playwright

---

## 🚀 次のステップ

### 今後の拡張予定
1. **音声入力機能**：Web Speech APIでハンズフリー体験
2. **学習進捗トラッキング**：ユーザーごとの進捗管理
3. **社内事例共有**：実際の活用事例を投稿できる機能
4. **コンテンツ追加**：経費精算、プレゼン資料作成など

### 社内展開案
- 非エンジニアメンバー向けのハンズオン研修
- 各部署での活用事例の収集
- コンテンツ追加ワークショップの開催

---

## 📚 詳細ドキュメントへのリンク

各章の詳細は、以下のドキュメントをご覧ください：

- [01_project-overview.md](./01_project-overview.md) - プロジェクト概要
- [02_learning-contents.md](./02_learning-contents.md) - 学習コンテンツ設計
- [03_technical-learnings.md](./03_technical-learnings.md) - 技術的な学び
- [04_development-process.md](./04_development-process.md) - 開発プロセス

---

**作成日**: 2026-03-06  
**作成者**: Claude Code（沢田あい）+ ユーザー  
**プロジェクトURL**: https://github.com/ju-kosaka/hackathon-expense-assistant
