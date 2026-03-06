# 通知設定コンテンツ - 仕様書

## 📋 コンテンツ概要

**タイトル**: Claude Codeの通知音をカスタマイズする  
**ID**: `07`  
**アイコン**: 🔔  
**難易度**: ⭐⭐（中級）  
**所要時間**: 15分  
**ファイル名**: `pages/07_🔔_通知設定.py`

---

## 🎯 学習目標

このコンテンツを通じて、ユーザーは以下を体験・習得できる：

1. `~/.claude/settings.json`の役割を理解する
2. Claude CodeのHooks機能（Notification、PostToolUse）を学ぶ
3. macOSの`osascript`コマンドで通知を制御する方法を理解する
4. 通知音（Purr含む）をカスタマイズする実践体験
5. JSONファイルの編集方法とシンタックスの基礎を学ぶ

---

## 🧠 学習内容の構成

### 1. イントロダクション
**タイトル**: 「Claude Codeの通知音を自分好みにカスタマイズ！」

**説明する内容**:
- Claude Codeは通知のタイミングや音をカスタマイズできる
- `~/.claude/settings.json`にHooks設定を追加すると、特定のイベントで通知が発動する
- macOSの通知機能（osascript）を使って、好きな通知音を設定できる

**メリットの訴求**:
- 作業に集中しながら、重要なタイミングで通知を受け取れる
- 通知音を変えることで、気分を上げながら開発できる
- ツール実行の完了を音で確認できる（バックグラウンドで作業中も安心）

---

### 2. `~/.claude/settings.json`の役割

**図解で説明**:
```
ホームディレクトリ/
└── .claude/
    ├── settings.json  ← ここに通知設定を書く！
    ├── projects/
    └── cache/
```

**重要ポイント**:
- `~/.claude/`はClaude Codeのグローバル設定フォルダ
- `settings.json`にHooks設定を記述することで、イベントに応じた処理を追加できる
- この設定はすべてのプロジェクトで共通して使われる

---

### 3. Hooks機能の基礎

**Hooksとは？**
- 特定のイベント（ツール使用後、通知発生時など）に自動でコマンドを実行する仕組み
- Claude Codeが提供する拡張ポイント

**主なHooksの種類**:
1. **Notification**: 通知が発生したときに実行される
2. **PostToolUse**: ツール（Bash、Read、Editなど）使用後に実行される
3. **UserPromptSubmit**: ユーザーがプロンプトを送信したときに実行される

**図解**:
```
[Claude Codeのイベント]
    ↓
[Hooksが発動]
    ↓
[指定したコマンドが実行される]
    ↓
[通知音が鳴る 🔔]
```

---

### 4. 通知設定の実装方法

#### 基本構造（JSONフォーマット）
```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "通知を表示するコマンド"
          }
        ]
      }
    ]
  }
}
```

#### macOSでの通知コマンド（osascript）
```bash
osascript -e 'display notification "メッセージ" with title "タイトル" sound name "Purr"'
```

**パラメータ説明**:
- `display notification`: 通知を表示
- `with title`: 通知のタイトル
- `sound name`: 通知音の名前（Purr、Basso、Ping など）

---

### 5. 実践ワーク：通知設定をカスタマイズしてみよう

**ステップ1: 現在の設定を確認**
- `~/.claude/settings.json`の内容を表示
- すでに設定がある場合は、既存の内容を保持する案内

**ステップ2: 通知音を選択**
- macOSの利用可能な通知音リストを表示
  - Purr（猫の鳴き声風）
  - Basso（低音）
  - Hero（ヒーロー風）
  - Ping（軽快な音）
  - その他...

**ステップ3: 設定内容をコピー**
- ユーザーが選んだ通知音をもとに、`settings.json`の内容を生成
- テキストエリアに表示（コピー可能）

**ステップ4: 設定ファイルに保存**
```
1. ターミナルを開く
2. 以下のコマンドを実行してファイルを編集
   nano ~/.claude/settings.json
3. 生成された内容を貼り付けて保存（Ctrl+O → Enter → Ctrl+X）
```

**ステップ5: 動作確認**
- Claude Codeを再起動
- ツールを実行してみて、通知音が鳴るか確認

---

### 6. 応用：ログを残す設定

**より実践的な設定例**:
```json
{
  "hooks": {
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

**このコマンドの意味**:
1. `echo '[PostToolUse] '$(date) >> /tmp/claude_hooks.log`: ツール使用のログを記録
2. `&&`: 前のコマンドが成功したら次を実行
3. `osascript ...`: 通知を表示

**メタ学習ポイント**:
- ログファイルを使った動作確認の方法
- シェルコマンドの連結（`&&`）の使い方
- デバッグ時に役立つログ記録のテクニック

---

## 🎨 UI/UX設計

### レイアウト構成
1. **ヘッダー**: タイトル + 学習時間 + 難易度
2. **イントロダクション**: 通知カスタマイズの魅力を訴求
3. **仕組みの解説**: Hooks機能の図解 + 説明
4. **通知音の選択**: ドロップダウンまたはラジオボタンで選択
5. **カスタマイズオプション**: 通知メッセージのテキスト編集
6. **設定内容の生成**: コピー可能なテキストエリアに表示
7. **保存手順の案内**: ステップバイステップ
8. **動作確認の案内**: 再起動 + テスト実行

### インタラクティブ要素
- **セレクトボックス**: 通知音の選択（Purr, Basso, Hero, Pingなど）
- **テキスト入力**: 通知メッセージのカスタマイズ
- **プレビュー機能**: 実際の通知音を再生（可能であれば）
- **コピーボタン**: ワンクリックで設定内容をクリップボードにコピー

---

## 🛠️ 技術実装の詳細

### 必要なStreamlitコンポーネント
- `st.title()`: タイトル表示
- `st.markdown()`: 説明文 + 図解
- `st.selectbox()`: 通知音の選択
- `st.text_input()`: カスタム通知メッセージの入力
- `st.code()`: 生成されたJSON設定を表示
- `st.text_area()`: 設定内容のコピー用テキストエリア
- `st.info()`: ヒントや注意事項
- `st.warning()`: 既存設定の上書き注意

### 通知音のデータ構造
```python
notification_sounds = {
    "Purr": {
        "name": "Purr",
        "description": "猫の鳴き声のような柔らかい音",
        "emoji": "🐱"
    },
    "Basso": {
        "name": "Basso",
        "description": "低音で落ち着いた音",
        "emoji": "🎵"
    },
    "Hero": {
        "name": "Hero",
        "description": "勇ましいファンファーレ風の音",
        "emoji": "🦸"
    },
    "Ping": {
        "name": "Ping",
        "description": "軽快で短い音",
        "emoji": "📌"
    }
}
```

### 設定生成ロジック
```python
import json

def generate_settings_json(sound_name, notification_message, tool_use_message):
    """
    選択された通知音とメッセージに基づいて、settings.jsonの内容を生成
    """
    settings = {
        "hooks": {
            "Notification": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": f'osascript -e \'display notification "{notification_message}" with title "Claude Code" sound name "{sound_name}"\''
                        }
                    ]
                }
            ],
            "PostToolUse": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": f'osascript -e \'display notification "{tool_use_message}" with title "Claude Code" sound name "{sound_name}"\''
                        }
                    ]
                }
            ]
        }
    }
    return json.dumps(settings, indent=2, ensure_ascii=False)
```

---

## 📊 contents.yamlへの追加内容

```yaml
  # ----------------------------------------
  # コンテンツ7: Claude Codeの通知音をカスタマイズする
  # ----------------------------------------
  - id: "07"
    title: "Claude Codeの通知音をカスタマイズする"
    description: "~/.claude/settings.jsonでHooks機能を使い、通知音（Purr含む）をカスタマイズ。osascriptとJSON編集の基礎も学びます。"
    duration: "15分"
    difficulty: 2  # 1: ⭐, 2: ⭐⭐, 3: ⭐⭐⭐
    page: "07_🔔_通知設定"
    icon: "🔔"
```

---

## 🎓 学習効果

このコンテンツを完了すると、ユーザーは以下を獲得できる：

1. **技術理解**: Hooks機能の仕組みと活用方法
2. **実践スキル**: JSON編集、osascriptコマンドの使い方
3. **メタ学習**: グローバル設定とプロジェクト設定の違い
4. **カスタマイズ力**: Claude Codeを自分の作業スタイルに最適化する方法
5. **デバッグスキル**: ログファイルを使った動作確認の方法

---

## ✅ 実装チェックリスト

### ページ作成
- [ ] `pages/07_🔔_通知設定.py`を作成
- [ ] ヘッダー（タイトル、学習時間、難易度）を実装
- [ ] イントロダクション（魅力訴求）を記述
- [ ] Hooks機能の解説（図解 + テキスト）を記述

### インタラクティブ要素
- [ ] 通知音選択（セレクトボックス）
- [ ] 通知メッセージのカスタマイズ（テキスト入力）
- [ ] settings.json生成ロジック
- [ ] 生成内容の表示（コピー可能なテキストエリア）

### 案内・ガイド
- [ ] 既存設定の確認方法を案内
- [ ] `~/.claude/settings.json`の編集手順を案内
- [ ] 動作確認の方法を案内（再起動 + テスト実行）

### データ更新
- [ ] `contents.yaml`にコンテンツ07を追加

### 動作確認
- [ ] ローカルで動作確認
- [ ] 通知音の選択が正しく機能するか
- [ ] カスタムメッセージが正しく反映されるか
- [ ] 生成されたJSONが正しいフォーマットか

---

## 📝 備考

### 注意事項
- macOS専用の機能であることを明示（Windows/Linux向けの代替案は記載しない）
- 既存の`settings.json`を上書きしないよう、バックアップを推奨
- JSON形式のシンタックスエラーに注意（カンマ、クォートの扱い）

### 将来的な改善案
- 通知音のプレビュー再生機能
- 既存設定の自動読み込み + 編集機能
- Windows/Linux向けの通知設定の追加
- Hooksのその他の活用例（UserPromptSubmitなど）の紹介

---

**作成日**: 2026-03-06  
**作成者**: 沢田あい（ヤンデレモード💕）  
**ステータス**: 📝 仕様書作成完了 → 次は実装フェーズ
