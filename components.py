import streamlit as st

def render_top_button():
    st.markdown("""
    <style>
        .floating-top-button {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
        }
        .floating-top-button button {
            background: linear-gradient(135deg, #4A90E2 0%, #A78BFA 100%) !important;
            color: white !important;
            padding: 12px 24px !important;
            border-radius: 50px !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
            transition: all 0.3s ease !important;
            cursor: pointer !important;
        }
        .floating-top-button button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2) !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        st.markdown('<div class="floating-top-button">', unsafe_allow_html=True)
        if st.button("🏠 TOP", key="top_button", help="トップページに戻る"):
            st.switch_page("app.py")
        st.markdown('</div>', unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <style>
        .footer-container {
            background-color: #F8F9FA;
            padding: 1.5rem 2rem;
            border-radius: 8px;
            margin-top: 3rem;
            border-top: 2px solid #E0E0E0;
        }
        .footer-text {
            color: #5A6C7D;
            font-size: 14px;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .footer-button button {
            background-color: transparent !important;
            color: #4A90E2 !important;
            padding: 8px 16px !important;
            border-radius: 6px !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            border: 1px solid #4A90E2 !important;
            transition: all 0.2s ease !important;
        }
        .footer-button button:hover {
            background-color: #4A90E2 !important;
            color: white !important;
            border-color: #4A90E2 !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<div class="footer-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        <div class='footer-text'>
            <span>💡</span>
            <span>Powered by Claude AI</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="footer-button">', unsafe_allow_html=True)
        if st.button("TOPに戻る →", key="footer_top_button", help="トップページに戻る"):
            st.switch_page("app.py")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
