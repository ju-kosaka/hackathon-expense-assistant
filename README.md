# 目指せ！みのるんマスター！

**Claude Code活用の体験型学習アプリ**

AIを使ってみたいけど、難しいと思っていてなかなか使えないあなたに。
実際に手を動かしながら、優しく寄り添いながら、Claude Codeの活用方法を学べるアプリです。

---

## 🎯 このアプリでできること

- **7つの学習コンテンツ**で段階的にスキルアップ
- **VSCode設定**から**プロマネ実践**まで幅広くカバー
- **体験型学習**で、読むだけでなく実際に手を動かせる
- **YAMLベースのコンテンツ管理**でメタ学習も習得

---

## 🚀 クイックスタート

### Webで体験（推奨）

デプロイ済みアプリ: https://hackathon-expense-assistant.streamlit.app/

### ローカルで起動

```bash
git clone https://github.com/ju-kosaka/hackathon-expense-assistant.git
cd hackathon-app
pip install -r requirements.txt
streamlit run app.py
```

ブラウザで `http://localhost:8501` を開く

---

## 📋 学習コンテンツ一覧

| ID | タイトル | 難易度 | 所要時間 |
|----|----------|--------|----------|
| 01 | VSCodeでClaude Codeを使えるようにしよう | ⭐ | 10分 |
| 02 | プチ仕様駆動開発を体験しよう | ⭐ | 15分 |
| 03 | 会議の議事録を自動生成 | ⭐⭐ | 20分 |
| 04 | Claude Codeでプロマネをぶん回す | ⭐⭐⭐ | 40分 |
| 05 | Plan modeの計画フォーマットをカスタマイズ | ⭐⭐ | 25分 |
| 06 | Claude Codeにキャラクターを設定する | ⭐ | 10分 |
| 07 | Claude Codeの通知音をカスタマイズする | ⭐⭐ | 15分 |

**合計学習時間**: 約135分（2時間15分）

---

## 💡 特徴

### 1. 段階的な学習曲線

初心者向けの基礎（⭐）から、実践的な応用（⭐⭐⭐）まで、無理なくステップアップできます。

### 2. 実践的なユースケース

すべてのコンテンツが、実際の業務で使えるテクニックに基づいています。

### 3. メタ学習要素

YAMLファイルの構造を学ぶことで、自分でコンテンツを追加できるようになります。

### 4. プチ仕様駆動開発

PLAN.md、SPEC.md、TODO.md、KNOWLEDGE.mdの4つのドキュメントを使った開発プロセスを学べます。

---

## 🛠️ 技術スタック

- **Frontend**: Streamlit (v1.42.1)
- **Backend**: Python (3.12.8)
- **AI/LLM**: Claude Code
- **インフラ**: Streamlit Community Cloud
- **設定管理**: YAML
- **バージョン管理**: Git/GitHub

---

## 📚 ドキュメント

- **プロジェクト管理**: `docs/project/`（PLAN.md、TODO.md、KNOWLEDGE.md）
- **仕様書**: `docs/specs/`（SPEC-*.md）
- **ガイド**: `docs/guides/`（add-content.md）
- **ハッカソン成果報告**: `docs/hackathon-report/`

---

## 🎓 参考文献

このアプリは、みのるん氏（@minorun365）のブログ記事を参考に開発されました：

- [Claude Codeで月末業務を5分で終わらせる話 - Qiita](https://qiita.com/minorun365/items/114f53def8cb0db60f47)
- [Claude Code Plan modeの計画フォーマットをカスタマイズする - Qiita](https://qiita.com/yoshiakih/items/18cd541d03720ab08958)

---

## 🚀 今後の展開

- 音声入力機能の追加（Web Speech API）
- 学習進捗トラッキング
- 社内事例共有機能
- コンテンツ追加ワークショップ

---

## 📄 ライセンス

MIT License

---

## 🤝 貢献

コンテンツの追加や改善のアイデアがあれば、ぜひIssueやPull Requestをお送りください！

詳細は `docs/guides/add-content.md` をご覧ください。

---

**開発期間**: 2026年3月4日〜6日（3日間）  
**開発者**: Claude Code + ユーザー  
**GitHubリポジトリ**: https://github.com/ju-kosaka/hackathon-expense-assistant
