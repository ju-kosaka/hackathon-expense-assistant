#!/usr/bin/env python3
import os
import sys
import yaml
import re
from pathlib import Path
import anthropic

CLAUDE_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

def get_next_content_id():
    yaml_path = Path("contents.yaml")
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if not data or 'contents' not in data or not data['contents']:
        return "01"
    
    max_id = max(int(content['id']) for content in data['contents'])
    return f"{max_id + 1:02d}"

def fetch_blog_content(url):
    print(f"📥 ブログコンテンツを取得中: {url}")
    
    if not CLAUDE_API_KEY:
        print("⚠️  ANTHROPIC_API_KEY が設定されていません。")
        print("環境変数を設定するか、手動でコンテンツを入力してください。")
        return None
    
    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": f"以下のURLから記事の内容を要約して、タイトル、概要、主要なポイントを抽出してください: {url}"
            }]
        )
        return message.content[0].text
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None

def generate_tutorial_content(blog_content, title, icon, difficulty):
    print("🤖 Claudeにチュートリアルコンテンツを生成させています...")
    
    if not CLAUDE_API_KEY:
        print("⚠️  ANTHROPIC_API_KEY が設定されていません。")
        return None
    
    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
    
    prompt = f"""
以下のブログコンテンツをもとに、Streamlitアプリの学習ページを作成してください。

【要件】
- タイトル: {title}
- アイコン: {icon}
- 難易度: {difficulty}
- 既存のページスタイルに合わせる
- render_top_button()とrender_footer()を必ず含める
- 実践的な学習体験を提供する内容にする

【ブログコンテンツ】
{blog_content}

【既存ページの参考スタイル】
```python
import streamlit as st
from components import render_top_button, render_footer

st.set_page_config(
    page_title="タイトル",
    page_icon="{icon}",
    layout="wide"
)

# スタイル定義
st.markdown(\"\"\"
<style>
    .main-header {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }}
</style>
\"\"\", unsafe_allow_html=True)

render_top_button()

st.markdown(\"\"\"
<div class="main-header">
    <h1>{icon} {title}</h1>
    <p>説明文</p>
</div>
\"\"\", unsafe_allow_html=True)

# コンテンツ本体

render_footer()
```

完全なPythonコードを出力してください。
"""
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8192,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        content = message.content[0].text
        code_match = re.search(r'```python\n(.*?)```', content, re.DOTALL)
        if code_match:
            return code_match.group(1)
        return content
        
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None

def create_new_page(content_id, icon, title, page_content):
    filename = f"pages/{content_id}_{icon}_{title}.py"
    filepath = Path(filename)
    
    print(f"📝 ページを作成中: {filename}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_content)
    
    print(f"✅ ページを作成しました: {filename}")
    return filename

def update_contents_yaml(content_id, title, description, duration, difficulty, page, icon):
    yaml_path = Path("contents.yaml")
    
    print("📋 contents.yaml を更新中...")
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    new_content = {
        'id': content_id,
        'title': title,
        'description': description,
        'duration': duration,
        'difficulty': difficulty,
        'page': page,
        'icon': icon
    }
    
    data['contents'].append(new_content)
    
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print("✅ contents.yaml を更新しました")

def main():
    print("=" * 60)
    print("🚀 新規コンテンツ追加スクリプト")
    print("=" * 60)
    print()
    
    content_id = get_next_content_id()
    print(f"📌 次のコンテンツID: {content_id}")
    print()
    
    print("📝 新規コンテンツの情報を入力してください")
    print()
    
    url = input("🔗 ブログ記事のURL（省略可）: ").strip()
    
    blog_content = ""
    if url:
        blog_content = fetch_blog_content(url)
        if not blog_content:
            print("⚠️  コンテンツ取得に失敗したため、手動入力に切り替えます")
    
    title = input("📌 タイトル: ").strip()
    icon = input("🎨 アイコン（絵文字）: ").strip()
    description = input("📄 説明文: ").strip()
    duration = input("⏱  所要時間（例: 15分）: ").strip()
    difficulty = int(input("⭐ 難易度（1-3）: ").strip())
    
    print()
    print("🤖 チュートリアルページを生成中...")
    
    if blog_content:
        page_content = generate_tutorial_content(blog_content, title, icon, difficulty)
    else:
        manual_content = input("📝 学習内容の詳細を入力してください: ").strip()
        page_content = generate_tutorial_content(manual_content, title, icon, difficulty)
    
    if not page_content:
        print("❌ ページ生成に失敗しました")
        sys.exit(1)
    
    page_name = f"{content_id}_{icon}_{title}"
    filename = create_new_page(content_id, icon, title, page_content)
    
    update_contents_yaml(
        content_id=content_id,
        title=title,
        description=description,
        duration=duration,
        difficulty=difficulty,
        page=page_name,
        icon=icon
    )
    
    print()
    print("=" * 60)
    print("✅ 新規コンテンツの追加が完了しました！")
    print("=" * 60)
    print()
    print("📝 次のステップ:")
    print("1. ローカルでStreamlitアプリを確認してください")
    print("   $ streamlit run 🏠_TOP.py")
    print()
    print("2. 問題なければGitにコミット＆プッシュしてください")
    print(f"   $ git add {filename} contents.yaml")
    print(f'   $ git commit -m "Add: {title}の学習コンテンツを追加"')
    print("   $ git push")
    print()

if __name__ == "__main__":
    main()
