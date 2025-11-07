

echo "Starting file organization..."


BASE_DIR="$HOME/Downloads"


mkdir -p "$BASE_DIR/documents"
mkdir -p "$BASE_DIR/images"
mkdir -p "$BASE_DIR/scripts"


mv -n "$BASE_DIR"/*.{pdf,docx,txt} "$BASE_DIR/documents/" 2>/dev/null
mv -n "$BASE_DIR"/*.{jpg,jpeg,png,gif} "$BASE_DIR/images/" 2>/dev/null
mv -n "$BASE_DIR"/*.{sh,py} "$BASE_DIR/scripts/" 2>/dev/null

echo "File organization complete."
echo "Check $BASE_DIR for new 'documents', 'images', and 'scripts' folders."