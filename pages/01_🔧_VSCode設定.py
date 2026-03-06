import streamlit as st
from components import render_top_button, render_footer

st.set_page_config(
    page_title="VSCodeでClaude Codeを使えるようにしよう",
    page_icon="🔧",
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
        background: linear-gradient(135deg, #A78BFA 0%, #4A90E2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 2rem 0 1rem 0;
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .step-box {
        background-color: #F0F4F8;
        border-left: 5px solid #4A90E2;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
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
    .method-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border: 2px solid #E0E0E0;
    }
</style>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("""
<div class="main-header">
    <h1>🔧 VSCodeでClaude Codeを使えるようにしよう</h1>
    <p>AIコーディングツールのセットアップを完全ガイド</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## この学習コンテンツでできること")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎯 Claude Codeとは
    AI支援コーディングツールを理解
    """)

with col2:
    st.markdown("""
    ### 🔧 セットアップ
    VSCodeへの導入手順を習得
    """)

with col3:
    st.markdown("""
    ### ⚡ 初回実行
    実際にAIを使ってコード生成
    """)

st.markdown("""
<div class="section-header">
    ✨ Claude Codeとは？
</div>
""", unsafe_allow_html=True)

st.markdown("""
**Claude Code**は、AnthropicのAI「Claude」をVSCodeで使えるツールです。

- 🤖 自然言語でコードを生成
- 🔍 バグを自動検出・修正
- 📝 コードの説明を自動生成
- ♻️ リファクタリングを支援

**なぜVSCodeなのか？**
- 最も人気のあるコードエディタ
- 拡張機能が豊富
- Claude Codeの公式サポート
""")

st.markdown("""
<div class="benefit-box">
    <h4>💡 Claude Codeのメリット</h4>
    <ul>
        <li>✅ <strong>コーディング速度が劇的に向上</strong>: AIが補助してくれる</li>
        <li>✅ <strong>バグ修正が簡単</strong>: 自動検出・修正機能</li>
        <li>✅ <strong>自然言語で指示できる</strong>: 専門用語不要</li>
        <li>✅ <strong>プロレベルのコード</strong>: ベストプラクティスに従う</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    📋 前提条件の確認
</div>
""", unsafe_allow_html=True)

st.markdown("### 必要なもの")

prerequisite1 = st.checkbox("✅ VSCode（Visual Studio Code）がインストール済み")
if not prerequisite1:
    st.info("💡 [VSCode公式サイト](https://code.visualstudio.com/)からダウンロードしてください")

prerequisite2 = st.checkbox("✅ インターネット接続がある")

st.markdown("""
<div class="section-header">
    🔀 セットアップ方法の選択
</div>
""", unsafe_allow_html=True)

st.markdown("""
Claude Codeには**2つの接続方法**があります。あなたの環境に合わせて選んでください。
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="method-card">
        <h3>📱 直接API接続</h3>
        <p><strong>推奨：個人開発者向け</strong></p>
        <ul>
            <li><strong>対象</strong>: 個人開発者、小規模チーム</li>
            <li><strong>メリット</strong>: シンプル、5分で完了</li>
            <li><strong>必要なもの</strong>: Anthropic APIキー</li>
            <li><strong>コスト</strong>: 従量課金（少額から）</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="method-card">
        <h3>☁️ AWS Bedrock経由</h3>
        <p><strong>企業・チーム向け</strong></p>
        <ul>
            <li><strong>対象</strong>: 企業、大規模チーム</li>
            <li><strong>メリット</strong>: AWS統合管理、セキュア</li>
            <li><strong>必要なもの</strong>: AWSアカウント、Bedrock権限</li>
            <li><strong>コスト</strong>: AWS料金体系</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### どちらの方法でセットアップしますか？")

setup_method = st.tabs(["📱 直接API接続", "☁️ AWS Bedrock"])

with setup_method[0]:
    st.markdown("""
    <div class="section-header">
        📱 直接API接続の手順
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップA1: Claude Code拡張機能のインストール</h3>
        <ol>
            <li>VSCodeを開く</li>
            <li>左サイドバーの「拡張機能」アイコンをクリック（または <code>Cmd+Shift+X</code> / <code>Ctrl+Shift+X</code>）</li>
            <li>検索バーに「Claude Code」と入力</li>
            <li>「Anthropic Claude Code」を見つける</li>
            <li>「インストール」ボタンをクリック</li>
        </ol>
        <p><strong>確認ポイント:</strong></p>
        <ul>
            <li>✅ 左サイドバーにClaude Codeのアイコンが表示される</li>
            <li>✅ コマンドパレットで「Claude」と検索すると、関連コマンドが表示される</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップA2: APIキーの設定</h3>
        <h4>APIキーの取得方法:</h4>
        <ol>
            <li><a href="https://console.anthropic.com/" target="_blank">Anthropic Console</a> にアクセス</li>
            <li>ログイン（GoogleアカウントなどでOK）</li>
            <li>「API Keys」メニューを開く</li>
            <li>「Create Key」をクリック</li>
            <li>キー名を入力（例: <code>vscode-claude-code</code>）</li>
            <li>生成されたキーをコピー</li>
        </ol>
        <h4>VSCodeでの設定:</h4>
        <ol>
            <li>コマンドパレットを開く（<code>Cmd+Shift+P</code> / <code>Ctrl+Shift+P</code>）</li>
            <li>「Claude Code: Set API Key」と入力</li>
            <li>取得したAPIキーを貼り付け</li>
            <li>Enterを押して保存</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
        <h4>⚠️ APIキーの取り扱い注意</h4>
        <ul>
            <li>APIキーは<strong>絶対に他人に教えない</strong></li>
            <li>GitHubなどに<strong>コミットしない</strong></li>
            <li>キーが漏洩した場合は、すぐに無効化して再生成</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップA3: 初めてのClaude Codeコマンド実行</h3>
        <h4>簡単なテスト:</h4>
        <ol>
            <li>新しいファイルを作成（<code>test.py</code>）</li>
            <li>コマンドパレットで「Claude Code: Chat」を実行</li>
            <li>チャット画面で以下のように入力:<br>
                <code>Pythonで "Hello, Claude Code!" と表示するコードを書いて</code></li>
            <li>Claudeが生成したコードを確認</li>
            <li>コードをファイルに適用</li>
        </ol>
        <h4>期待される結果:</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""print("Hello, Claude Code!")""", language="python")
    
    st.markdown("""
    <div class="success-box">
        <h4>✅ 動作確認</h4>
        <ul>
            <li>Claudeが応答した</li>
            <li>コードが生成された</li>
            <li>コードが正しく動作する</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with setup_method[1]:
    st.markdown("""
    <div class="section-header">
        ☁️ AWS Bedrock経由の手順
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 この方法は、AWSアカウントを持っている企業・チーム向けです")
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップB1: AWS Bedrockの有効化</h3>
        <h4>前提条件:</h4>
        <ul>
            <li>AWSアカウントを持っている</li>
            <li>Bedrockへのアクセス権限（IAM設定）</li>
            <li>リージョン: us-east-1 推奨</li>
        </ul>
        <h4>手順:</h4>
        <ol>
            <li><a href="https://console.aws.amazon.com/" target="_blank">AWS Console</a> にログイン</li>
            <li>サービス検索で「Bedrock」を入力</li>
            <li>Amazon Bedrockを開く</li>
            <li>左メニューから「Model access」を選択</li>
            <li>「Enable specific models」をクリック</li>
            <li>「Claude 3.5 Sonnet v2」にチェックを入れる</li>
            <li>「Request model access」をクリック</li>
            <li>承認されるまで待つ（通常は即時）</li>
        </ol>
        <p><strong>確認:</strong> Model statusが「Access granted」になっている</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップB2: IAM認証情報の設定</h3>
        <h4>手順:</h4>
        <ol>
            <li>AWS Console → IAM サービスを開く</li>
            <li>左メニューから「ユーザー」を選択</li>
            <li>自分のユーザー名をクリック</li>
            <li>「セキュリティ認証情報」タブを開く</li>
            <li>「アクセスキーを作成」ボタンをクリック</li>
            <li>用途: 「ローカルコード」を選択</li>
            <li>「次へ」→「アクセスキーを作成」</li>
            <li><strong>Access Key ID</strong> と <strong>Secret Access Key</strong> を安全な場所にメモ</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
        <h4>⚠️ 注意事項</h4>
        <ul>
            <li>Secret Access Keyは<strong>一度しか表示されない</strong></li>
            <li>絶対に他人に教えない、GitHubにコミットしない</li>
            <li>キーが漏洩した場合は、すぐに無効化して再生成</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 必要なIAMポリシー:")
    st.code("""{
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
}""", language="json")
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップB3: AWS CLIの設定</h3>
        <h4>AWS CLIのインストール（まだの場合）:</h4>
        <p><strong>macOS:</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("brew install awscli", language="bash")
    
    st.markdown("**Windows:**")
    st.code("msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi", language="powershell")
    
    st.markdown("**または、Python経由:**")
    st.code("pip install awscli", language="bash")
    
    st.markdown("#### 認証情報の設定:")
    st.code("""aws configure

# 以下を順番に入力
AWS Access Key ID [None]: <ステップB2で取得したAccess Key ID>
AWS Secret Access Key [None]: <ステップB2で取得したSecret Access Key>
Default region name [None]: us-east-1
Default output format [None]: json""", language="bash")
    
    st.markdown("#### 動作確認:")
    st.code("""# Bedrockへのアクセス確認
aws bedrock list-foundation-models --region us-east-1 | grep claude

# 成功すると、Claudeモデルのリストが表示される""", language="bash")
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップB4: VSCodeでBedrock接続を設定</h3>
        <h4>手順:</h4>
        <ol>
            <li>VSCodeを開く</li>
            <li>コマンドパレット（<code>Cmd+Shift+P</code> / <code>Ctrl+Shift+P</code>）</li>
            <li>「Claude Code: Set API Provider」と入力</li>
            <li>「AWS Bedrock」を選択</li>
            <li>AWS Profile: <code>default</code>（または作成したプロファイル名）</li>
            <li>Region: <code>us-east-1</code></li>
            <li>Model: <code>anthropic.claude-3-5-sonnet-20241022-v2:0</code></li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 設定ファイル（.vscode/settings.json）の例:")
    st.code("""{
  "claudeCode.apiProvider": "bedrock",
  "claudeCode.bedrock.profile": "default",
  "claudeCode.bedrock.region": "us-east-1",
  "claudeCode.bedrock.model": "anthropic.claude-3-5-sonnet-20241022-v2:0"
}""", language="json")
    
    st.markdown("""
    <div class="step-box">
        <h3>ステップB5: 動作確認</h3>
        <h4>テスト:</h4>
        <ol>
            <li>新しいファイルを作成（<code>test.py</code>）</li>
            <li>コマンドパレットで「Claude Code: Chat」を実行</li>
            <li>チャット画面で以下のように入力:<br>
                <code>Pythonで "Hello, Bedrock!" と表示するコードを書いて</code></li>
            <li>Claudeが生成したコードを確認</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""print("Hello, Bedrock!")""", language="python")
    
    st.markdown("""
    <div class="success-box">
        <h4>✅ 確認方法</h4>
        <ul>
            <li>VSCode下部のステータスバーに「Bedrock (us-east-1)」表示がある</li>
            <li>Claudeが応答した</li>
            <li>コードが生成された</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4>🔧 トラブルシューティング</h4>
        <ul>
            <li>エラー: <code>AccessDeniedException</code> → IAMポリシーを確認</li>
            <li>エラー: <code>ResourceNotFoundException</code> → Model accessを確認</li>
            <li>エラー: <code>Credentials not found</code> → <code>aws configure</code>を再実行</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    🚀 便利な機能の紹介
</div>
""", unsafe_allow_html=True)

st.markdown("### 主要な機能")

feature_tabs = st.tabs(["💬 Chat", "✏️ Edit", "🔧 Fix", "📖 Explain"])

with feature_tabs[0]:
    st.markdown("""
    ### Chat - 自然言語でコードを依頼
    
    **使い方:**
    - コマンド: `Claude Code: Chat`
    - 自然言語でコードを依頼
    - 例: 「ソート機能を実装して」
    """)
    st.code("""# 例: Pythonでクイックソートを実装して
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)""", language="python")

with feature_tabs[1]:
    st.markdown("""
    ### Edit - コードを編集・リファクタリング
    
    **使い方:**
    - コード選択 → コマンド: `Claude Code: Edit`
    - 選択したコードを改善
    - 例: 「この関数をもっと効率的にして」
    """)

with feature_tabs[2]:
    st.markdown("""
    ### Fix - バグを自動修正
    
    **使い方:**
    - エラー箇所を選択 → コマンド: `Claude Code: Fix`
    - Claudeが自動でバグを修正
    - 例: 構文エラー、ロジックエラーなど
    """)

with feature_tabs[3]:
    st.markdown("""
    ### Explain - コードの説明を生成
    
    **使い方:**
    - コード選択 → コマンド: `Claude Code: Explain`
    - Claudeがコードの動作を説明
    - 複雑なコードの理解に便利
    """)

st.markdown("""
<div class="section-header">
    💡 使い方のコツ
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ Good
    - 「〇〇する関数を書いて」
    - 「このコードを効率的にして」
    - 「エラーを修正して」
    - 具体的に指示する
    """)

with col2:
    st.markdown("""
    ### ❌ Bad
    - 「コード書いて」
    - 「なんかいい感じに」
    - 曖昧な指示
    - 一度に全部依頼
    """)

st.markdown("""
<div class="section-header">
    🎓 まとめ
</div>
""", unsafe_allow_html=True)

st.success("""
### セットアップ完了！

✅ **Claude Codeが使える状態になりました**
- VSCodeにClaude Code拡張機能をインストール
- APIキー（または AWS Bedrock）を設定
- 初めてのコマンド実行を体験

### 次のステップ
実際のプロジェクトでClaude Codeを活用してみましょう！
- 次のコンテンツ「プチ仕様駆動開発体験」に進んで、開発の流れを学ぼう
- Claude Codeを使って、実際にアプリを作ってみよう
""")

st.markdown("---")

st.markdown("### 📚 参考リンク")
st.markdown("- [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)")
st.markdown("- [VSCode 公式サイト](https://code.visualstudio.com/)")
st.markdown("- [Anthropic Console](https://console.anthropic.com/)")
st.markdown("- [AWS Bedrock](https://aws.amazon.com/bedrock/)")

render_footer()
