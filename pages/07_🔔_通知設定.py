import streamlit as st
import json
from components import render_top_button, render_footer

st.set_page_config(
    page_title="Claude Codeの通知音をカスタマイズする",
    page_icon="🔔",
    layout="wide"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .section-header {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 2rem 0 1rem 0;
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .step-box {
        background-color: #F0F4F8;
        border-left: 5px solid #667eea;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .sound-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border: 2px solid #E0E0E0;
        transition: all 0.3s ease;
    }
    .sound-card:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        border-color: #667eea;
    }
    .benefit-box {
        background: linear-gradient(90deg, #e0f7fa 0%, #b2ebf2 100%);
        border: 2px solid #00bcd4;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff9c4;
        border-left: 5px solid #fbc02d;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("""
<div class="main-header">
    <h1>🔔 Claude Codeの通知音をカスタマイズする</h1>
    <p>作業を楽しくする通知設定をマスターしよう</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## この学習コンテンツでできること")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎯 Hooks機能の理解
    Claude Code Hooksの仕組みを学ぶ
    """)

with col2:
    st.markdown("""
    ### 🔔 通知カスタマイズ
    好きな通知音で作業を楽しく
    """)

with col3:
    st.markdown("""
    ### 🛠️ JSON編集スキル
    settings.jsonの編集方法を習得
    """)

st.markdown("""
<div class="section-header">
    ✨ 通知カスタマイズとは？
</div>
""", unsafe_allow_html=True)

st.markdown("""
Claude Codeは、**Hooks機能**を使って通知のタイミングや音をカスタマイズできます。

`~/.claude/settings.json`にHooks設定を追加すると、特定のイベント（ツール実行後、通知発生時など）で自動的に通知が発動します。
""")

st.markdown("""
<div class="benefit-box">
    <h4>💡 通知カスタマイズのメリット</h4>
    <ul>
        <li>✅ <strong>作業に集中</strong>: 重要なタイミングで通知を受け取れる</li>
        <li>✅ <strong>モチベーションUP</strong>: 好きな音で開発が楽しくなる</li>
        <li>✅ <strong>バックグラウンド作業</strong>: ツール実行完了を音で確認できる</li>
        <li>✅ <strong>自由にカスタマイズ</strong>: 通知メッセージや音を自分好みに</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    📁 ~/.claude/settings.jsonの役割
</div>
""", unsafe_allow_html=True)

st.markdown("""
### ファイル構造

```
ホームディレクトリ/
└── .claude/
    ├── settings.json  ← ここに通知設定を書く！
    ├── projects/
    └── cache/
```

### 重要なポイント

1. **`~/.claude/`はグローバル設定フォルダ**  
   すべてのプロジェクトで共通して使われる

2. **`settings.json`にHooks設定を記述**  
   JSON形式でイベントに応じた処理を追加

3. **イベント発生時に自動実行**  
   設定したコマンドが自動で実行される
""")

st.markdown("""
<div class="section-header">
    🔗 Hooks機能の基礎
</div>
""", unsafe_allow_html=True)

st.markdown("""
### Hooksとは？

特定のイベント（ツール使用後、通知発生時など）に**自動でコマンドを実行**する仕組みです。

### 主なHooksの種類

1. **Notification**: 通知が発生したときに実行される
2. **PostToolUse**: ツール（Bash、Read、Editなど）使用後に実行される
3. **UserPromptSubmit**: ユーザーがプロンプトを送信したときに実行される

### 動作の流れ

```
[Claude Codeのイベント]
    ↓
[Hooksが発動]
    ↓
[指定したコマンドが実行される]
    ↓
[通知音が鳴る 🔔]
```
""")

st.markdown("""
<div class="section-header">
    🎵 通知音を選ぼう
</div>
""", unsafe_allow_html=True)

st.markdown("### macOSで利用可能な通知音")

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
    },
    "Pop": {
        "name": "Pop",
        "description": "ポップな軽い音",
        "emoji": "🎈"
    },
    "Submarine": {
        "name": "Submarine",
        "description": "ソナーのような音",
        "emoji": "🚢"
    }
}

selected_sound = st.selectbox(
    "通知音を選択してください",
    options=list(notification_sounds.keys()),
    format_func=lambda x: f"{notification_sounds[x]['emoji']} {notification_sounds[x]['name']} - {notification_sounds[x]['description']}"
)

st.markdown(f"""
<div class="sound-card">
    <h3>{notification_sounds[selected_sound]['emoji']} {notification_sounds[selected_sound]['name']}</h3>
    <p><strong>特徴:</strong> {notification_sounds[selected_sound]['description']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    ✏️ 通知メッセージをカスタマイズ
</div>
""", unsafe_allow_html=True)

notification_message = st.text_input(
    "通知時のメッセージ",
    value="Claude Code からの通知",
    help="Notificationイベント発生時に表示されるメッセージ"
)

tool_use_message = st.text_input(
    "ツール実行完了時のメッセージ",
    value="ツールの実行が完了しました",
    help="PostToolUseイベント発生時に表示されるメッセージ"
)

enable_logging = st.checkbox(
    "ログファイルを記録する（推奨）",
    value=True,
    help="実行履歴を /tmp/claude_hooks.log に記録します"
)

st.markdown("""
<div class="section-header">
    📋 生成されたsettings.json
</div>
""", unsafe_allow_html=True)

def generate_settings_json(sound_name, notif_msg, tool_msg, logging=True):
    """
    選択された通知音とメッセージに基づいて、settings.jsonの内容を生成
    """
    if logging:
        notification_cmd = f"echo '[Notification] '$(date) >> /tmp/claude_hooks.log && osascript -e 'display notification \"{notif_msg}\" with title \"Claude Code\" sound name \"{sound_name}\"'"
        tool_use_cmd = f"echo '[PostToolUse] '$(date) >> /tmp/claude_hooks.log && osascript -e 'display notification \"{tool_msg}\" with title \"Claude Code\" sound name \"{sound_name}\"'"
    else:
        notification_cmd = f"osascript -e 'display notification \"{notif_msg}\" with title \"Claude Code\" sound name \"{sound_name}\"'"
        tool_use_cmd = f"osascript -e 'display notification \"{tool_msg}\" with title \"Claude Code\" sound name \"{sound_name}\"'"
    
    settings = {
        "hooks": {
            "Notification": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": notification_cmd
                        }
                    ]
                }
            ],
            "PostToolUse": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": tool_use_cmd
                        }
                    ]
                }
            ]
        }
    }
    return json.dumps(settings, indent=2, ensure_ascii=False)

generated_json = generate_settings_json(
    selected_sound,
    notification_message,
    tool_use_message,
    enable_logging
)

st.markdown("""
<div class="success-box">
    ✅ settings.jsonの内容が生成されました！下のテキストをコピーして使ってください。
</div>
""", unsafe_allow_html=True)

st.text_area(
    "生成されたsettings.jsonの内容（コピーしてね）",
    value=generated_json,
    height=400
)

st.markdown("""
<div class="section-header">
    🔧 設定方法（ステップバイステップ）
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>ステップ1: 既存の設定を確認（重要！）</h3>
    <p>すでに<code>~/.claude/settings.json</code>がある場合、既存の設定を上書きしないように注意が必要です。</p>
    <p>まず、以下のコマンドで既存の設定を確認してください：</p>
</div>
""", unsafe_allow_html=True)

st.code("""# 既存設定を確認
cat ~/.claude/settings.json

# もしファイルが存在しない場合は、新規作成できます
""", language="bash")

st.markdown("""
<div class="warning-box">
    <h4>⚠️ 既存設定がある場合</h4>
    <p>既存の設定を保持したい場合は、生成されたJSONの<code>hooks</code>部分だけを既存のJSONにマージしてください。</p>
    <p>完全に上書きしても問題ない場合は、次のステップに進んでください。</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>ステップ2: settings.jsonを編集</h3>
    <p>ターミナルを開いて、以下のコマンドを実行します：</p>
</div>
""", unsafe_allow_html=True)

st.code("""# nanoエディタで編集
nano ~/.claude/settings.json

# または、VS Codeで編集
code ~/.claude/settings.json
""", language="bash")

st.markdown("""
<div class="info-box">
    <h4>💡 nanoエディタの操作方法</h4>
    <ul>
        <li><code>Ctrl+O</code>: 保存</li>
        <li><code>Enter</code>: ファイル名を確認</li>
        <li><code>Ctrl+X</code>: 終了</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>ステップ3: 生成されたJSONを貼り付け</h3>
    <p>上で生成されたJSONの内容をコピーして、<code>~/.claude/settings.json</code>に貼り付けて保存します。</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>ステップ4: Claude Codeを再起動</h3>
    <p>Claude Codeを再起動すると、新しい通知設定が読み込まれます。</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>ステップ5: 動作確認</h3>
    <p>Claude Codeで何かツール（Bashコマンド、ファイル読み込みなど）を実行してみて、通知音が鳴るか確認しましょう！</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    🧠 応用：ログファイルを確認する
</div>
""", unsafe_allow_html=True)

st.markdown("""
ログ記録を有効にした場合、実行履歴を確認できます。

### ログファイルの確認方法
""")

st.code("""# ログファイルの内容を確認
cat /tmp/claude_hooks.log

# リアルタイムで監視
tail -f /tmp/claude_hooks.log
""", language="bash")

st.markdown("""
### ログファイルのメリット

- ✅ **動作確認**: Hooksが正しく実行されているか確認できる
- ✅ **デバッグ**: 問題が発生した時の原因を特定しやすい
- ✅ **履歴管理**: いつ何が実行されたか記録が残る
""")

st.markdown("""
<div class="section-header">
    📚 技術解説：osascriptとは？
</div>
""", unsafe_allow_html=True)

st.markdown("""
`osascript`は、macOSのAppleScriptを実行するコマンドラインツールです。

### 基本構文

```bash
osascript -e 'display notification "メッセージ" with title "タイトル" sound name "音名"'
```

### パラメータ説明

- `display notification`: 通知を表示
- `with title`: 通知のタイトル
- `sound name`: 通知音の名前（Purr、Basso、Hero など）

### 例

```bash
# Purrの音で通知
osascript -e 'display notification "完了しました" with title "Claude Code" sound name "Purr"'
```

このコマンドを実行すると、macOSの通知センターに通知が表示され、Purrの音が鳴ります。
""")

st.markdown("""
<div class="section-header">
    🎓 まとめ
</div>
""", unsafe_allow_html=True)

st.success("""
### 通知設定の4つのポイント

1. **`~/.claude/settings.json`に設定を保存**
   - JSON形式でHooks設定を記述
   - グローバル設定なので全プロジェクトで有効

2. **通知音とメッセージをカスタマイズ**
   - macOSの通知音から好きな音を選択
   - 通知メッセージも自由に変更可能

3. **ログファイルで動作確認**
   - `/tmp/claude_hooks.log`に実行履歴が記録される
   - デバッグ時に役立つ

4. **再起動して確認**
   - Claude Codeを再起動
   - ツールを実行して通知音が鳴るか試す

### 次のステップ
実際にあなたの環境で通知設定をカスタマイズしてみましょう！
作業がもっと楽しくなるはずです🔔
""")

st.markdown("---")

st.markdown("### 📚 参考リンク")
st.markdown("- [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)")
st.markdown("- [このアプリのGitHubリポジトリ](https://github.com/ju-kosaka/hackathon-expense-assistant)")

render_footer()
