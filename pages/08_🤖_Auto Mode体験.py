import streamlit as st
from components import render_top_button, render_footer

st.set_page_config(
    page_title="Claude Code Auto Mode体験",
    page_icon="🤖",
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
    .feature-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .comparison-box {
        background-color: #E1F5FE;
        border: 2px solid #0277BD;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .tip-box {
        background-color: #FFF9C4;
        border-left: 5px solid #FBC02D;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("""
<div class="main-header">
    <h1>🤖 Claude Code Auto Modeを体験</h1>
    <p>承認後もAIが自動で作業を進める「オートモード」の使い方を学ぼう</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## このコンテンツで学べること")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### ⚡ Auto Modeとは
    承認後も自動で作業を進める新機能
    """)

with col2:
    st.markdown("""
    ### 🔄 手動承認との違い
    作業効率とコントロールのバランス
    """)

with col3:
    st.markdown("""
    ### 🎯 使い分けのコツ
    シーンに応じた最適な選択方法
    """)

st.markdown("---")

st.markdown("""
<div class="section-header">
    💡 Auto Modeとは？
</div>
""", unsafe_allow_html=True)

st.markdown("""
Claude Code の **Auto Mode（オートモード）** は、2026年3月5日にAnthropicから発表された新機能です。

従来は、Claudeが提案した変更を1つ1つ承認する必要がありましたが、Auto Modeでは**最初に承認すれば、その後はAIが自動で作業を進めてくれます**。
""")

st.markdown("""
<div class="feature-box">
    <h4>🎯 Auto Modeの特徴</h4>
    <ul>
        <li>✅ 最初の承認後、自動で複数のタスクを実行</li>
        <li>✅ 手動承認の手間を大幅に削減</li>
        <li>✅ 大規模なリファクタリングやバッチ処理に最適</li>
        <li>✅ いつでも手動モードに戻せる</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="section-header">
    ⚖️ 手動承認モードとの比較
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="comparison-box">
        <h4>🧑 手動承認モード（デフォルト）</h4>
        <p><strong>メリット:</strong></p>
        <ul>
            <li>1つ1つの変更を確認できる</li>
            <li>細かいコントロールが可能</li>
            <li>学習・理解しながら進められる</li>
        </ul>
        <p><strong>デメリット:</strong></p>
        <ul>
            <li>承認の手間がかかる</li>
            <li>大量の変更には不向き</li>
        </ul>
        <p><strong>こんな時に:</strong></p>
        <ul>
            <li>新しい機能の実装</li>
            <li>クリティカルな修正</li>
            <li>Claude Codeに慣れていない時</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="comparison-box">
        <h4>🤖 Auto Mode（新機能）</h4>
        <p><strong>メリット:</strong></p>
        <ul>
            <li>承認の手間が大幅に削減</li>
            <li>大量の変更を高速処理</li>
            <li>作業効率が飛躍的に向上</li>
        </ul>
        <p><strong>デメリット:</strong></p>
        <ul>
            <li>途中の変更が見えにくい</li>
            <li>予期しない変更が入る可能性</li>
        </ul>
        <p><strong>こんな時に:</strong></p>
        <ul>
            <li>大規模なリファクタリング</li>
            <li>バッチ処理</li>
            <li>信頼できるタスクの自動化</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="section-header">
    🚀 Auto Modeの使い方
</div>
""", unsafe_allow_html=True)

st.markdown("### Step 1: Auto Modeを有効にする")

st.code("""
# Claude Codeの設定で Auto Mode を有効化
# 現在はリサーチプレビュー版が公開されている段階のため、正式リリース後にコンテンツをアップデートします
""", language="bash")

st.markdown("### Step 2: タスクを依頼する")

st.code("""
# 例: すべてのコンポーネントにテストを追加
「すべてのReactコンポーネントにユニットテストを追加してください」
""", language="text")

st.markdown("### Step 3: 最初の提案を承認")

st.markdown("""
Claudeが最初の変更を提案します。内容を確認して承認すると、**Auto Modeでは自動的に残りのタスクも実行されます**。
""")

st.markdown("### Step 4: 完了を確認")

st.markdown("""
すべてのタスクが完了したら、変更内容を確認します。

```bash
git diff
```
""")

st.markdown("---")

st.markdown("""
<div class="section-header">
    💡 使い分けのコツ
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tip-box">
    <h4>🎯 Auto Modeを使うべき場面</h4>
    <ul>
        <li>✅ <strong>大規模なリファクタリング</strong>: 命名規則の統一、フォルダ構成の変更など</li>
        <li>✅ <strong>繰り返しタスク</strong>: 全ファイルへのヘッダー追加、import文の整理など</li>
        <li>✅ <strong>信頼できるパターン</strong>: 以前にも成功したタスクの再実行</li>
        <li>✅ <strong>時間がない時</strong>: デモ直前の最終調整など</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tip-box">
    <h4>🧑 手動承認モードを使うべき場面</h4>
    <ul>
        <li>✅ <strong>新しい機能の実装</strong>: 要件が不明確な時</li>
        <li>✅ <strong>クリティカルな修正</strong>: セキュリティ・パフォーマンスに影響する変更</li>
        <li>✅ <strong>学習目的</strong>: Claudeの提案を理解しながら進めたい時</li>
        <li>✅ <strong>コードレビュー的に</strong>: 1つ1つの変更を確認したい時</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="section-header">
    📚 参考リンク
</div>
""", unsafe_allow_html=True)

st.markdown("""
- [元記事: Claude Codeに「オートモード」登場 承認後もAIで自動作業](https://www.itmedia.co.jp/news/articles/2603/05/news116.html)
- [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)
- [Anthropic 公式サイト](https://www.anthropic.com/)
""")

st.markdown("""
<div class="tip-box">
    <h4>💡 まとめ</h4>
    <p>Auto Modeは作業効率を飛躍的に向上させる強力な機能です。</p>
    <p>手動承認モードとの使い分けを理解して、シーンに応じて最適な選択をしましょう。</p>
</div>
""", unsafe_allow_html=True)

render_footer()
