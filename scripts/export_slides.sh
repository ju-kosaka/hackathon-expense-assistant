#!/bin/bash

# Marpスライドを複数フォーマットで一括出力するスクリプト
# 作成日: 2026-03-10

set -e  # エラーが発生したら停止

# カラー出力
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Marp スライド一括出力スクリプト 📊${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 1. 現在日付を取得
DATE=$(date +%Y%m%d)
echo -e "${GREEN}📅 日付:${NC} $DATE"
echo ""

# 2. パスの設定
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SLIDES_DIR="$PROJECT_ROOT/docs/hackathon-report/slides"
INPUT_FILE="$SLIDES_DIR/presentation.md"
OUTPUT_DIR="$SLIDES_DIR/output"

echo -e "${GREEN}📁 プロジェクトルート:${NC} $PROJECT_ROOT"
echo -e "${GREEN}📝 入力ファイル:${NC} $INPUT_FILE"
echo -e "${GREEN}📂 出力先:${NC} $OUTPUT_DIR"
echo ""

# 3. 入力ファイルの確認
if [ ! -f "$INPUT_FILE" ]; then
    echo -e "${RED}❌ エラー: presentation.mdが見つかりません${NC}"
    echo -e "${RED}   パス: $INPUT_FILE${NC}"
    exit 1
fi

# 4. marp-cliの確認
if ! command -v marp &> /dev/null; then
    echo -e "${RED}❌ エラー: marp-cliがインストールされていません${NC}"
    echo ""
    echo -e "${YELLOW}インストール方法:${NC}"
    echo "  npm install -g @marp-team/marp-cli"
    echo ""
    exit 1
fi

echo -e "${GREEN}✅ marp-cli: インストール済み${NC}"
echo ""

# 5. 出力ディレクトリの作成
mkdir -p "$OUTPUT_DIR"

# 6. ファイル名のベース部分
BASE_NAME="目指せみのるんマスター_成果報告"

# 7. 各フォーマットで出力
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  出力開始 🚀${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# PDF出力
echo -e "${YELLOW}📄 PDF出力中...${NC}"
PDF_FILE="$OUTPUT_DIR/${BASE_NAME}_${DATE}.pdf"
if marp "$INPUT_FILE" --pdf --allow-local-files -o "$PDF_FILE"; then
    echo -e "${GREEN}✅ PDF生成成功:${NC} $(basename "$PDF_FILE")"
else
    echo -e "${RED}❌ PDF生成失敗${NC}"
fi
echo ""

# HTML出力
echo -e "${YELLOW}🌐 HTML出力中...${NC}"
HTML_FILE="$OUTPUT_DIR/hackathon-report_${DATE}.html"
if marp "$INPUT_FILE" --html --allow-local-files -o "$HTML_FILE"; then
    echo -e "${GREEN}✅ HTML生成成功:${NC} $(basename "$HTML_FILE")"
else
    echo -e "${RED}❌ HTML生成失敗${NC}"
fi
echo ""

# PPTX出力
echo -e "${YELLOW}📊 PPTX出力中...${NC}"
PPTX_FILE="$OUTPUT_DIR/${BASE_NAME}_${DATE}.pptx"
if marp "$INPUT_FILE" --pptx --allow-local-files -o "$PPTX_FILE"; then
    echo -e "${GREEN}✅ PPTX生成成功:${NC} $(basename "$PPTX_FILE")"
else
    echo -e "${RED}❌ PPTX生成失敗${NC}"
fi
echo ""

# 8. 生成されたファイル一覧を表示
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  生成されたファイル 📋${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ -d "$OUTPUT_DIR" ]; then
    ls -lh "$OUTPUT_DIR" | grep "$DATE" | awk '{printf "  %s  %s\n", $9, $5}'
else
    echo -e "${RED}❌ 出力ディレクトリが見つかりません${NC}"
fi

echo ""
echo -e "${GREEN}✨ すべての処理が完了しました！${NC}"
echo ""
