import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(
    page_title="TOP - 目指せ！みのるんマスター！",
    page_icon="🎓",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #A78BFA 0%, #4A90E2 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .main-header h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.95;
    }
    .content-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s, box-shadow 0.2s;
        cursor: pointer;
        border-left: 5px solid #4A90E2;
    }
    .content-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
    }
    .card-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2C3E50;
        margin-bottom: 0.5rem;
    }
    .card-description {
        color: #5A6C7D;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    .card-meta {
        display: flex;
        gap: 1rem;
        align-items: center;
        margin-top: 1rem;
    }
    .meta-badge {
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .badge-duration {
        background-color: #E3F2FD;
        color: #1976D2;
    }
    .badge-difficulty {
        background-color: #FFF3E0;
        color: #F57C00;
    }
    .hint-box {
        background-color: #F0F4F8;
        border-left: 4px solid #A78BFA;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
    }
    .hint-box h3 {
        color: #A78BFA;
        margin-bottom: 0.5rem;
    }
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        .main-header p {
            font-size: 1rem;
        }
        .content-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🎓 目指せ！みのるんマスター！</h1>
    <p>AI活用の実践スキルを体験を通じて学ぼう</p>
</div>
""", unsafe_allow_html=True)

def load_contents():
    """contents.yamlから学習コンテンツを読み込む"""
    yaml_path = Path(__file__).parent / "contents.yaml"
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data['contents']

def get_difficulty_stars(difficulty):
    """難易度を星に変換"""
    return "⭐" * difficulty

contents = load_contents()

st.markdown("### 📚 学習コンテンツ一覧")

for content in contents:
    col1, col2 = st.columns([1, 9])
    
    with col1:
        st.markdown(f"<div class='card-icon'>{content['icon']}</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<div class='card-title'>{content['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-description'>{content['description']}</div>", unsafe_allow_html=True)
        
        col_meta1, col_meta2, col_meta3 = st.columns([2, 2, 6])
        with col_meta1:
            st.markdown(f"<span class='meta-badge badge-duration'>⏱ {content['duration']}</span>", unsafe_allow_html=True)
        with col_meta2:
            stars = get_difficulty_stars(content['difficulty'])
            st.markdown(f"<span class='meta-badge badge-difficulty'>{stars}</span>", unsafe_allow_html=True)
        with col_meta3:
            if st.button(f"学習を始める →", key=f"btn_{content['id']}"):
                st.switch_page(f"pages/{content['page']}.py")
    
    st.markdown("<hr style='margin: 1.5rem 0; border: none; border-top: 1px solid #E0E0E0;'>", unsafe_allow_html=True)

st.markdown("""
<div class="hint-box">
    <h3>💡 開発者向けヒント</h3>
    <p>このアプリの学習コンテンツは <code>contents.yaml</code> で管理されています。</p>
    <p>YAMLファイルを編集して、新しいコンテンツを追加してみましょう！</p>
</div>
""", unsafe_allow_html=True)

github_url = "https://github.com/ju-kosaka/hackathon-expense-assistant/blob/main/contents.yaml"
st.markdown(f"[📂 contents.yaml を GitHub で見る]({github_url})")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; padding: 1rem;'>
    <p>Powered by Claude AI | Hackathon MVP</p>
</div>
""", unsafe_allow_html=True)
