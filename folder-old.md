# フォルダ構成（リファクタリング前）

**記録日時:** 2026-03-06  
**目的:** フォルダ整理前の構成をバックアップ

---

## 📂 完全なフォルダ構成

```
hackathon-app/
├── .claude/                                # Claude Code設定
│   └── CLAUDE.md                          # キャラクター設定
│
├── .devcontainer/                          # Dev Container設定
│   └── devcontainer.json
│
├── .git/                                   # Gitリポジトリ
│
├── .streamlit/                             # Streamlit設定
│   ├── config.toml
│   └── secrets.toml
│
├── .gitignore                              # Git除外設定
├── .python-version                         # Python バージョン指定
│
├── app.py                                  # メインファイル（本番用）
├── 🏠_TOP.py                               # ローカル開発用TOP
├── components.py                           # 共通コンポーネント
├── contents.yaml                           # コンテンツ管理
├── requirements.txt                        # 依存パッケージ
│
├── pages/                                  # Streamlitページ
│   ├── 01_💰_経費精算.py
│   ├── 02_📝_プチ仕様駆動開発体験.py
│   ├── 03_📋_会議議事録生成.py
│   ├── 04_🎯_プロマネ実践.py
│   ├── 05_📋_Plan modeカスタマイズ.py
│   ├── 06_💕_キャラクター設定.py
│   └── 07_🔔_通知設定.py
│
├── SPEC.md                                 # メイン仕様書
├── SPEC-setcharacter.md                    # キャラクター設定の仕様書
├── SPEC-notification.md                    # 通知設定の仕様書
│
├── PLAN.md                                 # 開発計画
├── TODO.md                                 # TODOリスト
├── KNOWLEDGE.md                            # 学んだ教訓・知見
│
├── README.md                               # プロジェクトREADME
├── README_ADD_CONTENT.md                   # コンテンツ追加手順
├── add-content.md                          # コンテンツ追加メモ
│
├── add_new_content.py                      # コンテンツ自動生成スクリプト
│
├── memo/                                   # メモフォルダ
│   └── streamlit_integration_consideration.md
│
├── static/                                 # 静的ファイル
│   └── sounds/
│       └── notification.mp3
│
└── venv/                                   # Python仮想環境
```

---

## 📊 ファイル分類

### **必須ファイル（本番環境で使用）**
- `app.py` - メインエントリーポイント
- `components.py` - 全ページから参照される共通コンポーネント
- `contents.yaml` - コンテンツ管理
- `requirements.txt` - 依存パッケージ
- `pages/*.py` - 全7コンテンツページ

### **開発用ファイル**
- `🏠_TOP.py` - ローカル開発用（本番では不使用）
- `add_new_content.py` - コンテンツ自動生成スクリプト

### **ドキュメント**
- `SPEC.md`, `SPEC-setcharacter.md`, `SPEC-notification.md` - 仕様書
- `PLAN.md` - 開発計画
- `TODO.md` - TODOリスト
- `KNOWLEDGE.md` - 学んだ教訓・知見
- `README.md` - プロジェクトREADME
- `README_ADD_CONTENT.md` - コンテンツ追加手順
- `add-content.md` - コンテンツ追加メモ

### **設定ファイル**
- `.gitignore` - Git除外設定
- `.python-version` - Pythonバージョン
- `.streamlit/config.toml` - Streamlit設定
- `.streamlit/secrets.toml` - シークレット管理
- `.claude/CLAUDE.md` - Claude Code設定
- `.devcontainer/devcontainer.json` - Dev Container設定

### **その他**
- `memo/` - 開発メモ
- `static/` - 静的ファイル（音声等）

---

## 🔗 依存関係マップ

### **Pythonファイルの依存関係**

```
app.py
├── import streamlit as st
├── import yaml
└── from pathlib import Path
    → 依存: contents.yaml

🏠_TOP.py
├── import streamlit as st
├── import yaml
└── from pathlib import Path
    → 依存: contents.yaml

components.py
└── import streamlit as st

pages/01_💰_経費精算.py
├── import streamlit as st
├── import pandas as pd
├── from datetime import datetime
└── from components import render_top_button, render_footer
    → 依存: components.py

pages/02_📝_プチ仕様駆動開発体験.py
├── import streamlit as st
└── from components import render_top_button, render_footer
    → 依存: components.py

pages/03_📋_会議議事録生成.py
├── import streamlit as st
├── import os
├── import boto3
├── import json
└── from components import render_top_button, render_footer
    → 依存: components.py

pages/04_🎯_プロマネ実践.py
├── import streamlit as st
├── import os
├── import boto3
├── import json
└── from components import render_top_button, render_footer
    → 依存: components.py

pages/05_📋_Plan modeカスタマイズ.py
├── import streamlit as st
└── from components import render_top_button, render_footer
    → 依存: components.py

pages/06_💕_キャラクター設定.py
├── import streamlit as st
└── from components import render_top_button, render_footer
    → 依存: components.py

pages/07_🔔_通知設定.py
├── import streamlit as st
├── import json
└── from components import render_top_button, render_footer
    → 依存: components.py

add_new_content.py
├── import os
├── import sys
├── import yaml
├── import re
├── from pathlib import Path
└── import anthropic
```

### **重要な依存関係**
1. **全ページ → `components.py`**: すべてのコンテンツページが `components.py` をインポート
2. **`app.py` & `🏠_TOP.py` → `contents.yaml`**: TOPページがコンテンツ一覧を読み込む
3. **`components.py` → `app.py`**: TOPボタンが `st.switch_page("app.py")` を使用

---

## ⚠️ 移動時の注意事項

### **移動してはいけないファイル**
- `app.py` - ルートに必須（Streamlit Community Cloud の制約）
- `components.py` - ルートに必須（`from components import` で参照）
- `contents.yaml` - ルートに必須（相対パス参照）
- `pages/` - ルートに必須（Streamlitの仕様）
- `requirements.txt` - ルートに必須（デプロイ時に参照）

### **移動可能なファイル**
- 仕様書: `SPEC*.md`
- プロジェクト管理: `PLAN.md`, `TODO.md`, `KNOWLEDGE.md`
- ガイド: `README_ADD_CONTENT.md`, `add-content.md`
- 開発スクリプト: `add_new_content.py`, `🏠_TOP.py`
- その他: `memo/`, `static/`

---

## 📝 備考

このドキュメントは、フォルダ整理（リファクタリング）前の状態を記録したものです。
整理後に問題が発生した場合、この構成に戻すことができます。

**次のステップ:** 提案1に基づいてフォルダを整理
- `docs/specs/` - 仕様書
- `docs/guides/` - ガイド・手順書
- `docs/project/` - プロジェクト管理
- `scripts/` - 開発スクリプト
