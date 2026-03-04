import streamlit as st

st.set_page_config(
    page_title="プチ仕様駆動開発を体験しよう",
    page_icon="📝",
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
    .step-box h3 {
        color: #4A90E2;
        margin-bottom: 1rem;
    }
    .doc-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #56C288;
    }
    .code-block {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 5px;
        font-family: monospace;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #E8F5E9;
        border-left: 4px solid #56C288;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>📝 プチ仕様駆動開発を体験しよう</h1>
    <p>4つのドキュメントでClaude Codeとの協働を最適化</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## なぜ4つのドキュメントが必要なのか")

st.info("""
Claude Codeにいきなり作業させると、**認識のズレ**が発生して手戻りが増えます。

4つのドキュメントを使うことで：
- ✅ やりたいことを整理できる
- ✅ Claudeとの認識齟齬がなくなる
- ✅ コンテキストをリセットしても再開できる
- ✅ 同じミスを二度と繰り返さない
""")

st.markdown("---")

st.markdown("## 4つのドキュメントとその役割")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="doc-card">
        <h3>📋 PLAN.md</h3>
        <p><strong>役割：</strong> やりたいことを音声入力で10分喋りまくる</p>
        <p><strong>内容：</strong></p>
        <ul>
            <li>プロジェクトの背景</li>
            <li>現状の課題</li>
            <li>やりたいこと</li>
            <li>前提条件</li>
        </ul>
        <p><strong>ポイント：</strong> フィラー混じりでOK！思いつくまま全部ダンプ</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="doc-card">
        <h3>✅ TODO.md</h3>
        <p><strong>役割：</strong> タスク管理。コンテキストをリセットしても再開できる</p>
        <p><strong>内容：</strong></p>
        <ul>
            <li>具体的なタスク一覧</li>
            <li>進捗状況（未着手/進行中/完了）</li>
            <li>優先度</li>
        </ul>
        <p><strong>ポイント：</strong> 細かく分解して、1つずつ潰していく</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="doc-card">
        <h3>📐 SPEC.md</h3>
        <p><strong>役割：</strong> 仕様の壁打ち結果。Claudeと認識齟齬をなくす</p>
        <p><strong>内容：</strong></p>
        <ul>
            <li>機能要件</li>
            <li>技術スタック</li>
            <li>UI/UXデザイン</li>
            <li>制約事項</li>
        </ul>
        <p><strong>ポイント：</strong> Claudeと対話しながら詳細化する</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="doc-card">
        <h3>💡 KNOWLEDGE.md</h3>
        <p><strong>役割：</strong> 学び・ナレッジ。一度ハマったことには二度とハマらない</p>
        <p><strong>内容：</strong></p>
        <ul>
            <li>ハマったポイント</li>
            <li>解決方法</li>
            <li>注意点</li>
            <li>次回への改善策</li>
        </ul>
        <p><strong>ポイント：</strong> ハマった瞬間にすぐ記録</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 実践：4つのドキュメントを作ってみよう")

st.markdown("""
<div class="step-box">
    <h3>ステップ1: PLAN.mdを作成する</h3>
    <p>まず、あなたが解決したい課題や作りたいものを自由に書き出しましょう。</p>
</div>
""", unsafe_allow_html=True)

with st.expander("💡 PLAN.mdのテンプレート例"):
    st.code("""# PLAN.md - やりたいこと

## 背景
- 毎月の経費精算に30分かかっている
- 手作業でのコピペが面倒
- ミスが発生しやすい

## 現状の課題
- MoneyForwardからCSVをダウンロード
- Gmailで領収書を1件ずつ検索
- freeeに手入力
- 申請ボタンを押す

## やりたいこと
- CSVをアップロードするだけで、Claudeが自動で分類
- 勘定科目を自動マッピング
- freee入力用のMarkdownを生成
- コピペで申請完了

## 前提条件
- freee APIは使わない（OAuth認証が複雑）
- CSV→Markdown変換方式で進める
- 社内メンバーも使えるようにWebアプリ化
""", language="markdown")

plan_input = st.text_area(
    "あなたのPLAN.mdを書いてみよう",
    height=200,
    placeholder="例: 毎週の報告書作成を自動化したい。現状は手作業で30分かかっている..."
)

if plan_input:
    st.markdown("""
    <div class="success-box">
        ✅ 素晴らしい！PLAN.mdができました。次はこれをClaude Codeと壁打ちして、SPEC.mdを作りましょう。
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>ステップ2: SPEC.mdを作成する</h3>
    <p>PLAN.mdをもとに、Claudeと対話しながら仕様を詰めていきます。</p>
</div>
""", unsafe_allow_html=True)

with st.expander("💡 SPEC.mdのテンプレート例"):
    st.code("""# SPEC.md - 仕様書

## アプリ概要
経費精算を5分で終わらせるWebアプリ

## ターゲットユーザー
- 毎月経費精算をする社内メンバー
- IT知識がない総務・営業

## 機能要件
### 必須機能
- CSVアップロード
- Claude APIでの自動分類
- Markdown出力

### 将来実装
- GitHub連携
- 音声入力

## 技術スタック
- Frontend: Streamlit
- Backend: Python
- AI: Claude (Anthropic)

## UI/UXデザイン
- フレンドリー
- シンプル
- AI感

## 制約事項
- freee APIは使わない（認証が複雑）
- CSV方式で進める
""", language="markdown")

st.info("👉 実際のプロジェクトでは、Claude Codeに「PLAN.mdをもとにSPEC.mdを作って」と指示します")

st.markdown("""
<div class="step-box">
    <h3>ステップ3: TODO.mdを作成する</h3>
    <p>SPEC.mdから具体的なタスクに分解します。</p>
</div>
""", unsafe_allow_html=True)

with st.expander("💡 TODO.mdのテンプレート例"):
    st.code("""# TODO.md - タスク管理

## 未着手
- [ ] Streamlit基本構成
- [ ] CSVアップロード機能
- [ ] Claude API連携

## 進行中
- [進行中] ローカルで動作確認

## 完了
- [x] プロジェクト初期化
- [x] requirements.txt作成
- [x] .gitignore作成
""", language="markdown")

st.markdown("""
<div class="step-box">
    <h3>ステップ4: KNOWLEDGE.mdを作成する</h3>
    <p>作業中にハマったことを即座に記録します。</p>
</div>
""", unsafe_allow_html=True)

with st.expander("💡 KNOWLEDGE.mdのテンプレート例"):
    st.code("""# KNOWLEDGE.md - 学びとナレッジ

## ハマったこと

### Streamlit Community Cloudでデプロイが止まる
**問題:**
- Python 3.13との互換性問題
- 依存関係の解決に失敗

**解決方法:**
- `.python-version`ファイルで Python 3.11 を指定
- requirements.txtのバージョン制約を緩める

**次回への改善:**
- 最初から`.python-version`を設定する
- バージョンは`>=`で指定する

### CSVの文字コード問題
**問題:**
- Shift_JISのCSVが文字化け

**解決方法:**
```python
df = pd.read_csv(file, encoding='shift_jis')
```

**次回への改善:**
- エンコーディング自動判定を実装
""", language="markdown")

st.markdown("---")

st.markdown("## 実際のClaude Codeでの使い方")

st.markdown("""
<div class="step-box">
    <h3>🚀 プロジェクト開始時</h3>
    <ol>
        <li>新しいリポジトリを作成</li>
        <li>Claude Codeを起動</li>
        <li>「このプロジェクトの初期化をして。PLAN.mdに音声入力で思考をダンプしたから、これをもとにSPEC.md、TODO.mdを作成して」と指示</li>
        <li>Claudeが4つのドキュメントを自動生成</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>🔄 作業再開時</h3>
    <ol>
        <li>TODO.mdを確認</li>
        <li>「TODO.mdの次のタスクをやって」と指示</li>
        <li>完了したら「TODO.mdを更新して」</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <h3>⚠️ ハマった時</h3>
    <ol>
        <li>「KNOWLEDGE.mdに今のエラーと解決方法を記録して」と指示</li>
        <li>次回、同じ問題に遭遇しても、Claudeがナレッジを参照して即解決</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## まとめ")

st.success("""
### プチ仕様駆動開発の3つのメリット

1. **認識のズレを防ぐ**
   - SPEC.mdで仕様を明確化
   - 手戻りが激減

2. **作業を中断・再開しやすい**
   - TODO.mdでタスク管理
   - コンテキストをリセットしても大丈夫

3. **同じミスを繰り返さない**
   - KNOWLEDGE.mdにナレッジ蓄積
   - 学習曲線が加速

### 次のステップ
実際にあなたのプロジェクトで4つのドキュメントを作成してみましょう！
Claude Codeと一緒に進めれば、驚くほどスムーズに開発が進みます。
""")

st.markdown("---")

st.markdown("### 📚 参考リンク")
st.markdown("- [参考記事: Claude Codeで月末業務を5分で終わらせる話](https://qiita.com/minorun365/items/114f53def8cb0db60f47)")
st.markdown("- [このアプリのGitHubリポジトリ](https://github.com/ju-kosaka/hackathon-expense-assistant)")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; padding: 1rem;'>
    <p>Powered by Claude AI | Hackathon MVP</p>
</div>
""", unsafe_allow_html=True)
