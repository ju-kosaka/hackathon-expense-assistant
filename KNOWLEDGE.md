# KNOWLEDGE.md - 学んだ教訓・知見

このファイルは、プロジェクトを通じて学んだ教訓や技術的な知見を記録します。

---

## 📅 2026-03-04

### 🚀 デプロイ・本番環境

#### **教訓1: 本番環境での動作を最優先にする**

**状況:**
- ローカル環境でサイドバーに "🏠 TOP" と表示させるために、`app.py` → `🏠_TOP.py` にリネームした
- Streamlit Community Cloudでは、Main file pathの設定項目がなく、`app.py` を自動検出する仕様だった
- 結果: デプロイエラー「The main module file does not exist: /mount/src/hackathon-expense-assistant/app.py」

**解決策:**
- `app.py` を復活させて、本番環境を優先
- サイドバーは `.app` のままで妥協（または、CSSで完全非表示にする）

**学んだこと:**
- **本番環境での動作を最優先にする**
- ローカルでの見た目の改善よりも、まず本番で動くことが重要
- Streamlit Community Cloudは設定の自由度が低いため、プラットフォームの制約に従う
- ハッカソンや期限のあるプロジェクトでは、「完璧な設計」よりも「動くもの」が優先

**今後の対応:**
- 新機能を追加する際は、まずローカルで動作確認
- その後、本番環境で問題が起きないかを確認してからデプロイ
- デプロイ前に、Streamlit Community Cloudの制約を事前に調査する

---

### 🎨 UI/UX

#### **教訓2: サイドバーを完全に非表示にする方法**

**状況:**
- Streamlitのサイドバー（ページナビゲーション）が表示されているが、学習アプリとして不要
- `.app` や絵文字付きのページ名が表示されるが、ユーザーにとって混乱の元

**解決策:**
- CSSで `[data-testid="stSidebar"]` を `display: none;` にする
- 全ページ（app.py + pages/配下の全ファイル）に以下を追加:

```python
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)
```

**学んだこと:**
- Streamlitの `initial_sidebar_state="collapsed"` では完全に非表示にならない（小さいボタンが残る）
- CSSで強制的に非表示にする方が、クリーンなUIになる
- ページ間の移動は、トップページの「学習を始める」ボタンで行う

**トレードオフ:**
- サイドバーを非表示にすると、ページ間の移動がボタンのみになる
- ユーザーが途中のページに直接アクセスした場合、トップに戻る手段がない（対応: ヘッダーにロゴリンクを追加する等）

---

### 🛠️ Git/GitHub

#### **教訓3: ファイル名変更はGitが自動認識する**

**状況:**
- `app.py` → `🏠_TOP.py` にリネームした際、Gitが `renamed` として認識した

**学んだこと:**
- Gitは内容が同じファイルを自動的に「rename」として認識する
- `git add -A` で削除と追加を一括でステージングすると、Gitが賢く判断してくれる

---

## 🧠 次回に活かすこと

1. **デプロイ環境の制約を事前に確認する**
   - Streamlit Community Cloud、Vercel、Herokuなど、プラットフォームごとに制約が異なる
   - ローカルで動いても、本番で動かないことがある

2. **本番優先の開発フロー**
   - ローカル開発 → 本番デプロイ確認 → UI改善
   - 本番で動かないと意味がない

3. **UI/UX改善はトレードオフを理解して判断**
   - サイドバー非表示 = ナビゲーションの制約
   - 見た目の美しさと機能性のバランスを取る

---

## 📚 参考リンク

- [Streamlit Community Cloud ドキュメント](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit set_page_config リファレンス](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)

---

**更新履歴:**
- 2026-03-04: 初版作成（デプロイ・UI・Git関連の教訓）
