import streamlit as st
import os
from components import render_top_button, render_footer

st.set_page_config(
    page_title="会議の議事録を自動生成",
    page_icon="📋",
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
    .step-box {
        background-color: #F8F9FA;
        border-left: 4px solid #4A90E2;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    .result-box {
        background-color: #F8F9FA;
        border-left: 4px solid #56C288;
        padding: 1.5rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #FFF3E0;
        border-left: 4px solid #F57C00;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("""
<div class="main-header">
    <h1>📋 会議の議事録を自動生成</h1>
    <p>文字起こしデータから構造化された議事録とネクストアクションを生成</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="warning-box">
    ⚠️ <strong>このコンテンツは現在休止中です</strong><br>
    AWS Bedrock APIの使用により課金が発生するため、実行機能を無効化しています。<br>
    ページの内容は学習用として閲覧可能です。
</div>
""", unsafe_allow_html=True)

st.markdown("## このツールでできること")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🗑️ フィラー除去
    「えー」「あの」「その」などの不要な言葉を自動削除
    """)

with col2:
    st.markdown("""
    ### 📚 専門用語認識
    事前に指定した専門領域の用語を正しく認識・整形
    """)

with col3:
    st.markdown("""
    ### ✅ ネクストアクション
    会議内容から次にやるべきことを3つ自動抽出
    """)

st.markdown("---")

st.markdown("## ステップ1: 専門領域を指定")

st.info("""
💡 **なぜ専門領域の指定が必要？**

文字起こしデータは音声認識の精度により、専門用語が正しく変換されていないことがあります。
事前に専門領域を指定することで、Claudeが関連用語を学習し、文脈から正しく推測できます。

例:
- 「すくらむ」→「スクラム」
- 「でぃーぷらーにんぐ」→「ディープラーニング」
""")

domain_input = st.text_input(
    "専門領域を入力してください（カンマ・読点・スペース区切り）",
    placeholder="例: アジャイル・スクラム、生成AI、クラウドコンピューティング",
    help="Claudeがこの領域に関連する専門用語リストを自動生成します"
)

if domain_input:
    # 複数の区切り文字に対応
    import re
    domains = [d.strip() for d in re.split(r'[,、\s]+', domain_input) if d.strip()]
    st.markdown("""
    <div class="result-box">
        ✅ 指定された専門領域 ({}個): <strong>{}</strong><br>
        Claudeがこの領域の用語リストを生成して、議事録作成に活用します。
    </div>
    """.format(len(domains), '、'.join(domains)), unsafe_allow_html=True)

st.markdown("---")

st.markdown("## ステップ2: 参加者情報（任意）")

participants_input = st.text_input(
    "参加者名を入力してください（カンマ・読点・スペース区切り）",
    placeholder="例: 田中太郎、佐藤花子、鈴木一郎 または 田中太郎 佐藤花子 鈴木一郎",
    help="入力しない場合でも、会議中の発言から自動推測します（カタカナ表記）"
)

if participants_input:
    # 複数の区切り文字に対応（全角・半角カンマ、全角・半角スペース、読点）
    import re
    participants = [p.strip() for p in re.split(r'[,、\s]+', participants_input) if p.strip()]
    st.success(f"✅ 参加者 {len(participants)}名: {', '.join(participants)}")

st.markdown("---")

st.markdown("## ステップ3: 文字起こしデータを入力")

transcript_input = st.text_area(
    "文字起こしデータを貼り付けてください",
    height=300,
    placeholder="""例:
えー、今日はですね、あの、すくらむについてお話しします。
田中さん、いかがですか？
はい、えー、でいりーすくらむは毎朝やってます。
そうですね、あの、すぷりんとは2週間でやってますね。
佐藤さんは？
えー、れとろすぺくてぃぶが大事だと思います。
""",
    help="音声認識ツール（Whisper等）で生成した文字起こしテキストを貼り付けてください"
)

st.markdown("---")

st.markdown("## ステップ4: 議事録を生成")

def generate_minutes(transcript: str, domains: str = "", participants: str = "") -> str:
    """議事録生成機能（現在無効化中）"""
    st.warning("⚠️ この機能は課金が発生するため、現在無効化されています。")
    return None

if st.button("🚀 議事録を生成", type="primary", disabled=True):
    if not transcript_input:
        st.error("⚠️ 文字起こしデータを入力してください")
    else:
        result = generate_minutes(transcript_input, domain_input, participants_input)
        
        if result:
            st.markdown("---")
            st.markdown("## 📋 生成された議事録")
            st.markdown(result)
            
            # ダウンロードボタン
            st.download_button(
                label="📥 議事録をダウンロード",
                data=result,
                file_name="meeting_minutes.md",
                mime="text/markdown"
            )
        else:
            st.info("💡 この機能は休止中です。以下は生成される議事録のイメージです。")
            with st.expander("📋 生成される議事録のイメージ（デモ）"):
                st.markdown(f"""
### 議事録

#### 会議概要
- **日時**: 2026年3月4日
- **参加者**: {participants_input if participants_input else "タナカさん, サトウさん（推測）"}
- **テーマ**: {domain_input if domain_input else "未指定"}

#### 議論内容

**スクラムの実施状況について**

タナカさんから、デイリースクラムを毎朝実施している旨の報告がありました。
スプリントは2週間サイクルで運用しているとのことです。

サトウさんからは、レトロスペクティブ（振り返り）の重要性について意見がありました。

#### ネクストアクション

1. デイリースクラムの継続実施（担当: タナカ）
2. 2週間スプリントの運用見直し検討
3. レトロスペクティブの実施方法を改善

#### 備考
- フィラー（「えー」「あの」等）を除去済み
- 専門用語を文脈から推測して正式表記に変換済み
            """)

st.markdown("---")

st.markdown("## 💡 使い方のコツ")

with st.expander("専門領域の指定例"):
    st.markdown("""
    - **IT系**: アジャイル開発, クラウド, セキュリティ, DevOps
    - **AI系**: 機械学習, 深層学習, LLM, プロンプトエンジニアリング
    - **ビジネス**: マーケティング, 会計, 人事, 経営戦略
    - **医療**: 診断, 治療, 医薬品, カルテ
    
    複数の領域を組み合わせることも可能です。
    """)

with st.expander("文字起こしデータの品質について"):
    st.markdown("""
    ### 推奨される文字起こしツール
    - OpenAI Whisper API
    - Google Cloud Speech-to-Text
    - AWS Transcribe
    
    ### 対応できる品質
    - ✅ フィラーが多い（「えー」「あの」等）
    - ✅ 専門用語が間違っている（「すくらむ」等）
    - ✅ 参加者名が推測できない（音だけでは漢字不明）
    - ⚠️ 音声が聞き取れず文字起こし自体が不完全な場合は、精度が落ちます
    """)

with st.expander("参加者名の推測ロジック"):
    st.markdown("""
    ### 自動推測の仕組み
    会議中に「〇〇さん、いかがですか？」のような発言があった場合、
    その「〇〇さん」を参加者として推測します。
    
    ### カタカナ表記の理由
    日本語の音声認識では、漢字を正確に判定することが困難です。
    例えば「たなか」が「田中」なのか「田仲」なのか判断できないため、
    カタカナで「タナカさん」と表記します。
    
    ### 事前登録のメリット
    参加者を事前に登録しておくと、正式な名前（漢字）で議事録を生成できます。
    """)

st.markdown("---")

st.markdown("### 📚 参考リンク")
st.markdown("- [参考記事: Claude Codeで月末業務を5分で終わらせる話](https://qiita.com/minorun365/items/114f53def8cb0db60f47)")
st.markdown("- [OpenAI Whisper（音声認識）](https://openai.com/research/whisper)")

render_footer()
