import streamlit as st
import os
import boto3
import json
from components import render_top_button, render_footer

st.set_page_config(
    page_title="Claude Codeでプロマネをぶん回す",
    page_icon="🎯",
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
    .folder-box {
        background-color: #F0F4F8;
        border-left: 5px solid #4A90E2;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
    }
    .pipeline-box {
        background: linear-gradient(90deg, #E3F2FD 0%, #F3E5F5 100%);
        border: 2px solid #4A90E2;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .skill-cycle {
        background-color: #FFF3E0;
        border: 3px dashed #F57C00;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }
    .claude-md-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .step-box {
        background-color: #E1F5FE;
        border: 2px solid #0277BD;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .highlight-box {
        background-color: #FFF9C4;
        border-left: 5px solid #FBC02D;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🎯 Claude Codeでプロマネをぶん回す</h1>
    <p>フォルダ構造をハブにした開発プロマネの実践体験</p>
</div>
""", unsafe_allow_html=True)

render_top_button()

st.markdown("## この学習コンテンツでできること")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📁 フォルダ設計
    情報の流れを設計する7つのフォルダ構造を理解
    """)

with col2:
    st.markdown("""
    ### 🔄 パイプライン構築
    MTG → レポート → 共有の自動化フローを体験
    """)

with col3:
    st.markdown("""
    ### 🎓 スキル化
    手動作業からスキル化へのボトムアップアプローチ
    """)

st.markdown("---")

st.markdown("""
<div class="section-header">
    📁 セクション1: プロジェクトのフォルダ構成がすべてのハブ
</div>
""", unsafe_allow_html=True)

st.info("""
💡 **PM業務の本質は「情報の流れを設計すること」**

散らばった情報（Slack、メール、ドキュメント、コード）を1つのフォルダに集約し、
そこを起点にClaude Codeが全てを管理する。これがプロマネをぶん回す秘訣です。
""")

st.markdown("### 7つのフォルダとその役割")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="folder-box">
    <strong>📘 CLAUDE.md</strong><br>
    プロジェクトの「脳」。ステークホルダー、専門用語、制約を記述。<br>
    <em>例: プロジェクト名、関係者リスト、頻出クエリ</em>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="folder-box">
    <strong>🧠 .claude/skills/</strong><br>
    PM業務のビルディングブロック。繰り返す作業をスキル化。<br>
    <em>例: 議事録作成、レポート生成、データ分析</em>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="folder-box">
    <strong>🎤 minutes/</strong><br>
    情報の一次基地。音声・文字起こし・議事録の段階的加工。<br>
    <em>例: raw.txt → edited.txt → final.md</em>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="folder-box">
    <strong>📊 reports/</strong><br>
    加工済みアウトプット。ワークフロー・分析結果を保存。<br>
    <em>例: weekly-report.pdf, analysis.md</em>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="folder-box">
    <strong>📚 docs/</strong><br>
    業務棚卸し。業務設計書やオンボーディング資料。<br>
    <em>例: onboarding.md, workflow.md</em>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="folder-box">
    <strong>🎯 work-description/</strong><br>
    タスクの定義書。各業務タスクの詳細手順と目的を明示。<br>
    <em>例: task-001.md, sprint-planning.md</em>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="folder-box">
    <strong>💾 data/</strong><br>
    分析用の生データ。CSVやログファイルなど加工前データ集約。<br>
    <em>例: expense.csv, logs/, analytics/</em>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### フォルダ構造のテンプレート")

folder_structure = """project-root/
├── CLAUDE.md
├── .claude/
│   └── skills/
│       ├── transcribe-and-update.sh
│       ├── create-minutes.sh
│       └── share-internal-minutes.sh
├── minutes/
│   ├── 2026-03-04-raw.txt
│   ├── 2026-03-04-edited.txt
│   └── 2026-03-04-final.md
├── reports/
│   ├── weekly-report-2026-03-04.pdf
│   └── analysis.md
├── docs/
│   ├── onboarding.md
│   └── workflow.md
├── work-description/
│   ├── task-001.md
│   └── sprint-planning.md
└── data/
    ├── expense.csv
    └── analytics/
"""

st.code(folder_structure, language="")

st.download_button(
    label="📥 フォルダ構造テンプレートをダウンロード",
    data=folder_structure,
    file_name="pm-folder-structure.txt",
    mime="text/plain"
)

st.markdown("---")

st.markdown("""
<div class="section-header">
    🔄 セクション2: 実演 - パイプラインのフロー
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pipeline-box">
<h3 style='margin-top: 0;'>📍 情報がどう流れるか（内部MTGの例）</h3>

<strong>ステップ1: 情報収集</strong><br>
🎤 <strong>内部MTG</strong> → 音声録音 → <code>minutes/raw.txt</code> (文字起こし)<br>
<em>↓ スキル: [/transcribe-and-update]</em><br><br>

<strong>ステップ2: 一次加工</strong><br>
📝 <strong>minutes/edited.txt</strong> → フィラー除去・整形<br>
<strong>Notion (内部議事録)</strong> → チーム内共有<br>
<em>↓ スキル: [/share-internal-minutes]</em><br><br>

<strong>ステップ3: 二次加工</strong><br>
💼 <strong>Slack (内部共有)</strong> → チャンネルに投稿<br>
<em>↓ スキル: [/create-minutes]</em><br><br>

<strong>ステップ4: 最終成果物</strong><br>
📄 <strong>Notion (外部テンプレート)</strong> → ステークホルダー向け整形<br>
<em>↓ スキル: [/fill-external-minutes]</em><br><br>

<strong>ステップ5: 配布</strong><br>
📧 <strong>PDF + メール</strong> → 外部配信<br>
<em>各ステップにスナップショットが残る = 情報の流れを設計すること</em>
</div>
""", unsafe_allow_html=True)

st.markdown("### パイプラインのポイント")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### ✅ 各ステップにスナップショットが残る
    - `minutes/` フォルダに加工段階が全て保存
    - 後から「なぜこうなった？」を追跡可能
    - エラーが起きても、前の段階に戻れる
    """)

with col2:
    st.markdown("""
    #### ✅ スキル化で自動化
    - 繰り返す作業は `.claude/skills/` にスキル化
    - 次回から `/transcribe-and-update` で一発実行
    - パイプライン全体が自動化される
    """)

st.markdown("---")

st.markdown("""
<div class="section-header">
    🎓 セクション3: スキル構築はボトムアップで生える
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="skill-cycle">
<h3 style='margin-top: 0;'>🔄 手動 → 繰り返し → スキル化 → リファクタ</h3>

<strong>1. 手動で頼む</strong><br>
「この文字起こしから議事録を作って」と普通に依頼<br><br>

<strong>2. 繰り返すなら「スキル化」</strong><br>
2-3回同じことを頼んだら「これをスキル化して」と言う<br>
→ Claude Codeが <code>.claude/skills/create-minutes.sh</code> を作成<br><br>

<strong>3. 構造が見えたら「リファクタ」</strong><br>
複数のスキルに共通部分が見えたら統合・整理<br>
→ より汎用的なスキルに進化<br><br>

<strong>4. 被ったら「リファクタ」</strong><br>
同じようなスキルが増えたら整理整頓
</div>
""", unsafe_allow_html=True)

st.info("""
💡 **なぜボトムアップ？**

最初から完璧な設計を目指すと、実際の業務フローとズレが生じます。
まずは手動で試し、繰り返す中でパターンを発見し、それをスキル化する。
この方が実際の業務に即した自動化が実現できます。

**操作の起点はVS Codeのターミナル1枚。**
""")

st.markdown("### スキルファイルの例")

skill_example = """# .claude/skills/create-minutes.sh
# 議事録作成スキル

# 説明: 文字起こしデータから議事録を生成
# 入力: minutes/raw.txt
# 出力: minutes/final.md

# 実行内容:
# 1. minutes/raw.txt を読み込み
# 2. フィラーを除去
# 3. 専門用語を整形
# 4. ネクストアクションを抽出
# 5. minutes/final.md に保存
# 6. Notion にアップロード

echo "議事録を生成中..."
python scripts/generate_minutes.py minutes/raw.txt -o minutes/final.md
echo "完了！ minutes/final.md を確認してください"
"""

st.code(skill_example, language="bash")

st.download_button(
    label="📥 スキルファイル例をダウンロード",
    data=skill_example,
    file_name="create-minutes.sh",
    mime="text/plain"
)

st.markdown("---")

st.markdown("""
<div class="section-header">
    🧠 セクション4: CLAUDE.md の役割 - パイプラインに「文脈」を与える
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="claude-md-box">
<h3 style='margin-top: 0;'>📘 CLAUDE.md = プロジェクトの脳</h3>

CLAUDE.mdは、Claude Codeがプロジェクトを理解するための「文脈ファイル」です。
ここに書かれた情報を元に、スキルが自動的に判断を行います。

<strong>記載内容の例:</strong>
<ul>
<li>ステークホルダーの名前と役割（田中さん = PM、佐藤さん = エンジニア）</li>
<li>業務特有の用語と制約（「スクラム」「スプリント」「レトロスペクティブ」）</li>
<li>頻出クエリテンプレート（「議事録を作成」「レポートを生成」）</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("### CLAUDE.md 生成フォーム")

st.markdown("以下の質問に答えると、Claudeがあなたのプロジェクト用のCLAUDE.mdを自動生成します。")

with st.form("claude_md_form"):
    project_name = st.text_input(
        "プロジェクト名",
        placeholder="例: ハッカソンアプリ開発"
    )
    
    stakeholders = st.text_area(
        "ステークホルダー（名前と役割）",
        placeholder="例:\n田中太郎 - プロジェクトマネージャー\n佐藤花子 - エンジニア\n鈴木一郎 - デザイナー",
        height=100
    )
    
    domain_terms = st.text_area(
        "専門用語・制約",
        placeholder="例: アジャイル開発、スクラム、デイリースクラム、スプリント、AWS Bedrock、Streamlit",
        height=80
    )
    
    common_queries = st.text_area(
        "よく使うクエリ（任意）",
        placeholder="例:\n- 議事録を作成して\n- 週次レポートを生成して\n- データ分析をして",
        height=100
    )
    
    submit_button = st.form_submit_button("🚀 CLAUDE.md を生成", type="primary")

if submit_button:
    if not project_name or not stakeholders or not domain_terms:
        st.error("⚠️ プロジェクト名、ステークホルダー、専門用語は必須です")
    else:
        def generate_claude_md(project_name, stakeholders, domain_terms, common_queries):
            try:
                bedrock = boto3.client(
                    service_name='bedrock-runtime',
                    region_name='us-east-1'
                )
            except Exception as e:
                st.error(f"⚠️ AWS Bedrock への接続に失敗しました: {str(e)}")
                return None
            
            prompt = f"""あなたは優秀なプロジェクトマネージャーのアシスタントです。以下の情報から、Claude Codeが参照するCLAUDE.mdファイルを生成してください。

【プロジェクト情報】
プロジェクト名: {project_name}

ステークホルダー:
{stakeholders}

専門用語・制約:
{domain_terms}

よく使うクエリ:
{common_queries if common_queries else "なし"}

【指示】
以下のフォーマットでCLAUDE.mdを生成してください。Markdown形式で出力し、Claude Codeがこのファイルを読むだけでプロジェクトの全体像を理解できるようにしてください。

【出力フォーマット】

# CLAUDE.md - プロジェクトの脳

## プロジェクト概要
- **プロジェクト名**: [プロジェクト名]
- **目的**: [プロジェクトの目的を推測して記載]

## ステークホルダー
[名前と役割をリスト化]

## 専門用語・制約
[専門用語を箇条書きで説明付きで記載]

## 頻出クエリテンプレート
[よく使うクエリをリスト化、または汎用的なクエリを提案]

## フォルダ構造
```
project-root/
├── CLAUDE.md
├── .claude/skills/
├── minutes/
├── reports/
├── docs/
├── work-description/
└── data/
```

## スキル一覧
[プロジェクトで使いそうなスキルを3-5個提案]

---
**生成日**: {st.session_state.get('current_timestamp', '2026-03-04')}
**使い方**: このファイルをプロジェクトルートに配置し、Claude Codeに「CLAUDE.mdを読んで」と伝えてください。
"""
            
            try:
                with st.spinner("Claudeが CLAUDE.md を生成中..."):
                    body = json.dumps({
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": 4000,
                        "messages": [{
                            "role": "user",
                            "content": prompt
                        }]
                    })
                    
                    response = bedrock.invoke_model(
                        modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
                        body=body
                    )
                    
                    response_body = json.loads(response['body'].read())
                    return response_body['content'][0]['text']
            
            except Exception as e:
                st.error(f"❌ エラーが発生しました: {str(e)}")
                return None
        
        result = generate_claude_md(project_name, stakeholders, domain_terms, common_queries)
        
        if result:
            st.markdown("---")
            st.markdown("## 📘 生成された CLAUDE.md")
            st.markdown(result)
            
            st.download_button(
                label="📥 CLAUDE.md をダウンロード",
                data=result,
                file_name="CLAUDE.md",
                mime="text/markdown"
            )
            
            st.success("""
            ✅ **CLAUDE.md 生成完了！**
            
            **次のステップ:**
            1. ダウンロードした CLAUDE.md をプロジェクトルートに配置
            2. Claude Code を開いて「CLAUDE.md を読んでください」と伝える
            3. Claudeがプロジェクトの文脈を理解した状態で作業開始
            """)
        else:
            st.markdown("""
            <div class="highlight-box">
            <strong>⚠️ エラー時のデモ表示</strong><br>
            実際には AWS Bedrock を使って CLAUDE.md が自動生成されます。
            </div>
            """, unsafe_allow_html=True)
            
            default_queries = "- 議事録を作成して\n- レポートを生成して"
            queries_text = common_queries if common_queries else default_queries
            
            demo_claude_md = f"""# CLAUDE.md - プロジェクトの脳

## プロジェクト概要
- **プロジェクト名**: {project_name}
- **目的**: {project_name}の効率的な開発とプロジェクト管理

## ステークホルダー
{stakeholders}

## 専門用語・制約
{domain_terms}

## 頻出クエリテンプレート
{queries_text}

## フォルダ構造
```
project-root/
├── CLAUDE.md
├── .claude/skills/
├── minutes/
├── reports/
├── docs/
├── work-description/
└── data/
```

## スキル一覧
- 議事録作成
- 週次レポート生成
- データ分析

---
**生成日**: 2026-03-04
**使い方**: このファイルをプロジェクトルートに配置し、Claude Codeに「CLAUDE.mdを読んで」と伝えてください。
"""
            st.markdown("### デモ: 生成される CLAUDE.md のイメージ")
            st.code(demo_claude_md, language="markdown")

st.markdown("---")

st.markdown("""
<div class="section-header">
    🎯 セクション5: 真似するための最初の一歩
</div>
""", unsafe_allow_html=True)

st.markdown("### あなたが今日からできる3ステップ")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="step-box">
    <h4>1️⃣ フォルダが散らかってきたら切る</h4>
    <p>プロジェクトを始めて、ファイルが増えてきたタイミングで、上記の7つのフォルダ構造を作成する。</p>
    <p><strong>目安:</strong> 5-10個のファイルが散らかってきたら</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="step-box">
    <h4>2️⃣ Claude Codeに手動で1-2業務を繰り返す</h4>
    <p>まずは手動で「議事録を作って」「レポートを作って」と依頼を繰り返す。うまくいったら、次へ。</p>
    <p><strong>目安:</strong> 同じ作業を2-3回頼んだら</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="step-box">
    <h4>3️⃣ 繰り返しなら「スキル化」と言う</h4>
    <p>「この作業をスキル化して」と伝えると、Claude Codeが <code>.claude/skills/</code> にスクリプトを作成。</p>
    <p><strong>次回から:</strong> <code>/create-minutes</code> で一発実行</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<strong>💡 ポイント: 完璧を目指さない</strong><br>
最初から完璧なフォルダ構造やスキルを作ろうとしない。
散らかってきたらリファクタ、繰り返したらスキル化。この繰り返しで自然と最適化されていきます。
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 💡 まとめ")

st.success("""
**Claude Codeでプロマネをぶん回すための5つのポイント**

1. **フォルダ構造がハブ** - 情報の流れを設計する7つのフォルダ
2. **パイプラインのフロー** - MTG → レポート → 配信の自動化
3. **ボトムアップなスキル構築** - 手動 → 繰り返し → スキル化 → リファクタ
4. **CLAUDE.md** - プロジェクトの脳・文脈を与える
5. **最初の一歩** - 散らかったらフォルダを切る、繰り返したらスキル化

**PM業務の本質は「情報の流れを設計すること」。**
Claude Codeをうまく使えば、あなたのプロマネ業務は10倍速くなります。
""")

st.markdown("---")

st.markdown("## 📚 参考リンク")
st.markdown("- [参考記事: Claude Codeでプロマネをぶん回すやり方](https://x.com/minorun365)")
st.markdown("- [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code)")

render_footer()
