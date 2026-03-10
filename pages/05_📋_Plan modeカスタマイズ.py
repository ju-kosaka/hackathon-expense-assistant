import streamlit as st
from components import render_top_button, render_footer

st.set_page_config(
    page_title="Claude Code Plan modeカスタマイズ",
    page_icon="📋",
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
        background: linear-gradient(135deg, #4A90E2 0%, #667eea 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 2rem 0 1rem 0;
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .plan-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .code-box {
        background-color: #F0F4F8;
        border-left: 5px solid #4A90E2;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
    }
    .step-box {
        background-color: #E1F5FE;
        border: 2px solid #0277BD;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .file-structure {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1.5rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        margin: 1rem 0;
        border: 1px solid #3c3c3c;
    }
    .highlight-box {
        background-color: #FFF9C4;
        border-left: 5px solid #FBC02D;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .benefit-box {
        background: linear-gradient(90deg, #E3F2FD 0%, #F3E5F5 100%);
        border: 2px solid #4A90E2;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("""
<div class="main-header">
    <h1>📋 Plan modeの計画フォーマットをカスタマイズ</h1>
    <p>プロジェクトに最適な計画形式を設定しよう</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## この学習コンテンツでできること")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎯 Plan modeの理解
    計画立案機能の基本と活用方法
    """)

with col2:
    st.markdown("""
    ### 🔧 フォーマット設定
    プロジェクトに合わせたカスタマイズ
    """)

with col3:
    st.markdown("""
    ### 📝 実践演習
    実際に設定ファイルを作成
    """)

st.markdown("""
<div class="section-header">
    💡 Plan modeとは？
</div>
""", unsafe_allow_html=True)

st.markdown("""
Claude Code の **Plan mode** は、変更を実行する前に計画を立案してくれる強力な機能です。

「どのファイルを」「どう変えるか」をClaude Codeが事前に整理してくれるため、大規模な変更も安心して進められます。
""")

st.markdown("""
<div class="plan-box">
    <h4>🎯 Plan modeの特徴</h4>
    <ul>
        <li>✅ 変更前に計画を確認できる</li>
        <li>✅ 複数ファイルにまたがる変更を整理</li>
        <li>✅ 変更の影響範囲を事前に把握</li>
        <li>✅ チーム内で計画を共有しやすい</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    ⚠️ よくある課題
</div>
""", unsafe_allow_html=True)

st.markdown("""
ただし、デフォルトの計画フォーマットには以下のような課題があります：
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>😥 課題1: フォーマットが不統一</h4>
        <p>毎回、計画の出力形式がバラバラになりがち</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>😥 課題2: 情報が不足</h4>
        <p>必要な情報が含まれていないことがある</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    ✨ 解決策: plan_output_style.mdでカスタマイズ
</div>
""", unsafe_allow_html=True)

st.markdown("""
Claude Codeでは、`.claude/` ディレクトリに `plan_output_style.md` ファイルを配置することで、計画フォーマットをカスタマイズできます。
""")

st.markdown("#### 📁 ファイル配置場所")
st.markdown("""
<div class="file-structure">
プロジェクトルート/<br>
└── .claude/<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── plan_output_style.md
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    🛠️ 実践: plan_output_style.mdを作成しよう
</div>
""", unsafe_allow_html=True)

st.markdown("### Step 1: .claudeディレクトリを作成")

st.code("""
# プロジェクトルートで実行
mkdir -p .claude
""", language="bash")

st.markdown("### Step 2: plan_output_style.mdを作成")

st.markdown("""
以下は、プロジェクトで統一された計画フォーマットの例です：
""")

st.code("""
# Plan Output Style

計画を以下の形式で出力してください：

## 📋 実装概要
[変更内容の要約を1-2文で記載]

## 🎯 目的
[この変更を行う理由や達成したいこと]

## 📁 変更ファイル一覧
[変更するファイルのリスト]
- `path/to/file1.py` - [変更内容の概要]
- `path/to/file2.py` - [変更内容の概要]

## 🔧 実装ステップ
### ステップ1: [タイトル]
- 詳細な作業内容

### ステップ2: [タイトル]
- 詳細な作業内容

## ⚠️ 注意事項
[特に注意が必要な点や影響範囲]

## ✅ 完了条件
[変更が正しく完了したと判断する基準]
""", language="markdown")

st.markdown("### Step 3: Claude Codeで確認")

st.markdown("""
1. Claude Codeを起動
2. Plan modeに切り替え（`/plan` コマンド）
3. 何か変更を依頼してみる
4. 計画が設定したフォーマットで出力されることを確認
""")

st.markdown("""
<div class="benefit-box">
    <h4>💡 カスタマイズのメリット</h4>
    <ul>
        <li>📊 <strong>一貫性</strong>: チーム全体で統一されたフォーマット</li>
        <li>🔍 <strong>可読性</strong>: 必要な情報が漏れなく整理される</li>
        <li>📝 <strong>ドキュメント化</strong>: 計画そのものがドキュメントになる</li>
        <li>🤝 <strong>コミュニケーション</strong>: レビュー時の議論がスムーズ</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    🎨 カスタマイズ例
</div>
""", unsafe_allow_html=True)

tabs = st.tabs(["シンプル版", "詳細版", "チーム開発版"])

with tabs[0]:
    st.markdown("### 🎯 シンプル版（個人開発向け）")
    st.code("""
# Plan Output

## 変更内容
[要約]

## ファイル
- `file1.py` - [変更点]
- `file2.py` - [変更点]

## ステップ
1. [作業1]
2. [作業2]
3. [作業3]
""", language="markdown")

with tabs[1]:
    st.markdown("### 📊 詳細版（大規模プロジェクト向け）")
    st.code("""
# Plan Output Style

## 🎯 変更概要
[概要を記載]

## 📋 背景と目的
### 背景
[なぜこの変更が必要か]

### 目的
[何を達成したいか]

## 🔍 影響範囲分析
### 直接影響するファイル
- [ファイルリスト]

### 間接的に影響を受ける可能性
- [関連ファイルや機能]

## 🛠️ 実装計画
### Phase 1: [フェーズ名]
- [ ] タスク1
- [ ] タスク2

### Phase 2: [フェーズ名]
- [ ] タスク3
- [ ] タスク4

## ⚠️ リスクと対策
| リスク | 対策 |
|--------|------|
| [リスク1] | [対策1] |
| [リスク2] | [対策2] |

## ✅ テスト計画
- [ ] ユニットテスト
- [ ] 統合テスト
- [ ] 手動確認項目

## 📝 完了条件
1. [条件1]
2. [条件2]
3. [条件3]
""", language="markdown")

with tabs[2]:
    st.markdown("### 🤝 チーム開発版（レビュー重視）")
    st.code("""
# Plan Output Style

## 📌 変更サマリー
**種類**: [Feature/Bugfix/Refactor/etc]
**優先度**: [High/Medium/Low]
**所要時間**: [見積もり]

## 🎯 目的
[この変更を行う理由]

## 📁 変更ファイル
| ファイル | 変更内容 | 影響度 |
|---------|---------|--------|
| `file1.py` | [内容] | High |
| `file2.py` | [内容] | Medium |

## 🔧 実装ステップ
### 1. [ステップ名]
**担当**: [誰が実装するか]
**詳細**: [作業内容]

### 2. [ステップ名]
**担当**: [誰が実装するか]
**詳細**: [作業内容]

## 🔍 レビューポイント
- [ ] [確認項目1]
- [ ] [確認項目2]
- [ ] [確認項目3]

## ⚠️ 注意事項
[特に注意すべき点]

## ✅ Definition of Done
- [ ] [完了条件1]
- [ ] [完了条件2]
- [ ] [完了条件3]
""", language="markdown")

st.markdown("""
<div class="section-header">
    🎓 実践演習
</div>
""", unsafe_allow_html=True)

st.markdown("### 演習: あなたのプロジェクト用フォーマットを作ろう")

exercise_tab1, exercise_tab2, exercise_tab3 = st.tabs(["演習問題", "ヒント", "解答例"])

with exercise_tab1:
    st.markdown("""
    以下の要件を満たす `plan_output_style.md` を作成してください：
    
    **要件**:
    1. 変更内容の要約セクション
    2. 変更するファイルのリスト
    3. 実装ステップ（最低3ステップ）
    4. 完了条件
    
    **ボーナス**:
    - 絵文字を使って視覚的にわかりやすく
    - テーブル形式で情報を整理
    """)

with exercise_tab2:
    st.markdown("""
    **ヒント**:
    - Markdownの見出し（`##`）を使ってセクションを分ける
    - リスト（`-` または `1.`）で項目を整理
    - コードブロック（` ``` `）でファイルパスを強調
    - チェックボックス（`- [ ]`）でタスクを管理
    """)

with exercise_tab3:
    st.code("""
# Plan Output Style

## 📋 変更概要
[変更内容を1-2文で要約]

## 📁 変更ファイル
| ファイルパス | 変更内容 |
|-------------|---------|
| `path/to/file1.py` | [変更の概要] |
| `path/to/file2.py` | [変更の概要] |

## 🔧 実装ステップ
### Step 1: [準備作業]
- [詳細]

### Step 2: [メイン実装]
- [詳細]

### Step 3: [テストと確認]
- [詳細]

## ✅ 完了条件
- [ ] [条件1]
- [ ] [条件2]
- [ ] [条件3]
""", language="markdown")

st.markdown("""
<div class="section-header">
    📚 参考リンク
</div>
""", unsafe_allow_html=True)

st.markdown("""
- [元記事: Claude Code Plan modeの計画フォーマットをカスタマイズする](https://qiita.com/yoshiakih/items/18cd541d03720ab08958)
- [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)
- [Markdown記法ガイド](https://www.markdownguide.org/)
""")

st.markdown("""
<div class="highlight-box">
    <h4>💡 まとめ</h4>
    <p><code>plan_output_style.md</code>を活用すれば、Claude Codeの計画フォーマットをプロジェクトに最適化できます。</p>
    <p>チーム開発では特に効果的で、全員が統一されたフォーマットで計画を確認できるようになります。</p>
</div>
""", unsafe_allow_html=True)

render_footer()
