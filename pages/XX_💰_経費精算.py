import streamlit as st
import pandas as pd
from datetime import datetime
from components import render_top_button, render_footer

st.set_page_config(
    page_title="経費精算アシスタント",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .main-header {
        background: linear-gradient(135deg, #A78BFA 0%, #4A90E2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .upload-section {
        border: 2px dashed #4A90E2;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        background-color: #F8F9FA;
    }
    .result-box {
        background-color: #F8F9FA;
        border-left: 4px solid #56C288;
        padding: 1.5rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        font-size: 18px;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #357ABD;
    }
</style>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("""
<div class="main-header">
    <h1>🤖 経費精算アシスタント</h1>
    <p>AIがあなたの経費精算を爆速化します</p>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs(["📁 CSVアップロード", "💬 音声入力", "📊 結果"])

with tabs[0]:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown("### 📁 CSVファイルをアップロード")
    st.markdown("freeeまたはマネーフォワードからエクスポートしたCSVファイルをドラッグ＆ドロップ")
    
    uploaded_file = st.file_uploader(
        "ここにファイルをドロップ または クリックして選択",
        type=['csv'],
        help="freee/マネーフォワードのCSVファイルに対応"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        st.success("✅ ファイルをアップロードしました！")
        
        try:
            df = pd.read_csv(uploaded_file)
            st.markdown("#### プレビュー（最初の5行）")
            st.dataframe(df.head(), use_container_width=True)
            
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(f"""
            ✓ **{len(df)}件**のレコードを検出  
            ✓ **{len(df.columns)}個**のカラムを確認  
            ✓ 自動分類の準備完了
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
            if st.button("🚀 Claude で解析開始", key="analyze"):
                with st.spinner("Claudeが解析中..."):
                    st.info("⚠️ Claude API連携は次のステップで実装します")
                    
        except Exception as e:
            st.error(f"❌ ファイルの読み込みに失敗しました: {str(e)}")

with tabs[1]:
    st.markdown("### 💬 音声で指示を入力")
    st.info("🎤 Web Speech APIによる音声入力機能は次のステップで実装します")
    
    text_input = st.text_area(
        "または、テキストで入力してください",
        height=150,
        placeholder="例: 今月の経費精算をやって"
    )
    
    if st.button("📝 指示を送信", key="voice"):
        if text_input:
            st.success(f"受信しました: {text_input}")
        else:
            st.warning("⚠️ 入力がありません")

with tabs[2]:
    st.markdown("### 📊 解析結果")
    
    if uploaded_file is None:
        st.info("👈 まずはCSVファイルをアップロードしてください")
    else:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 生成されるドキュメント
        
        1. **PLAN.md** - 音声入力の内容
        2. **SPEC.md** - 仕様の壁打ち結果
        3. **TODO.md** - タスク管理
        4. **KNOWLEDGE.md** - ナレッジ・学び
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Markdownをダウンロード", key="download"):
                st.info("⚠️ ダウンロード機能は次のステップで実装します")
        
        with col2:
            if st.button("🚀 GitHub にpush", key="github"):
                st.info("⚠️ GitHub連携は次のステップで実装します")

render_footer()
