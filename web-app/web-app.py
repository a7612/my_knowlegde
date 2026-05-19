from flask import Flask, render_template_string
import markdown
import re
import os

app = Flask(__name__)

# Đường dẫn đến thư mục wiki
WIKI_DIR = r"C:\Users\nhan\Documents\.obsidian\oh-my-god\my_knowlegde\wiki"

def convert_wikilinks(text):
    # 1. Lấy danh sách tất cả file .md hiện có trong vault để kiểm tra sự tồn tại
    vault_root = os.path.dirname(WIKI_DIR)
    existing_files = set()
    for root, dirs, files in os.walk(vault_root):
        for f in files:
            if f.endswith('.md'):
                existing_files.add(f.lower())

    # Regex hỗ trợ cả [[slug|text]] và [[slug]]
    pattern = r'\[\[([^|\]]+)(?:\|([^\]]+))?\]\]'
    
    def replace_link(match):
        slug = match.group(1)
        display_text = match.group(2) if match.group(2) else slug
        
        # Kiểm tra xem file có tồn tại không (so sánh tên file không phân biệt hoa thường)
        target_filename = f"{os.path.basename(slug)}.md".lower()
        
        if target_filename in existing_files:
            return f'<a href="/page/{slug}">{display_text}</a>'
        else:
            # Nếu không tồn tại, thêm text cảnh báo và đổi màu link sang cam/vàng cho dễ nhận biết
            return f'<a href="/page/{slug}" style="color: #e67e22;">{display_text}</a> <small style="color: #e74c3c;">(cần bổ sung)</small>'
            
    return re.sub(pattern, replace_link, text)

@app.route('/')
def index():
    index_path = os.path.join(WIKI_DIR, 'index.md')
    if not os.path.exists(index_path):
        return "Lỗi: Không tìm thấy file wiki/index.md.", 404
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Xử lý wikilinks trước khi convert markdown
    content = convert_wikilinks(content)
    # Chuyển đổi markdown sang HTML
    html_content = markdown.markdown(content, extensions=['extra', 'toc'])
    
    template = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shadow Wiki</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; max-width: 900px; margin: 40px auto; padding: 0 20px; color: #333; background-color: #f9f9f9; }
            .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
            h2 { color: #2980b9; margin-top: 30px; }
            a { color: #3498db; text-decoration: none; transition: color 0.2s; }
            a:hover { color: #21618c; text-decoration: underline; }
            ul { padding-left: 20px; }
            li { margin-bottom: 8px; }
            code { background: #eee; padding: 2px 5px; border-radius: 3px; font-family: 'Consolas', monospace; }
            pre { background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 5px; overflow-x: auto; }
            .footer { margin-top: 50px; font-size: 0.9em; color: #7f8c8d; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            {{ content|safe }}
        </div>
        <div class="footer">
            The Shadow Wiki Project by tags90 (Ng Cao Nhan)
        </div>
    </body>
    </html>
    """
    return render_template_string(template, content=html_content)

@app.route('/page/<path:slug>')
def page(slug):
    # Lấy tên file gốc từ đường dẫn (ví dụ: "wiki/concepts/abc" -> "abc.md")
    filename_to_find = f"{os.path.basename(slug)}.md"
    
    found_path = None
    # Tìm kiếm trong toàn bộ vault (bao gồm cả thư mục wiki và my_knowlegde)
    vault_root = os.path.dirname(WIKI_DIR)
    for root, dirs, files in os.walk(vault_root):
        if filename_to_find in files:
            found_path = os.path.join(root, filename_to_find)
            break
            
    if not found_path:
        return f"Không tìm thấy trang: {slug}", 404
        
    with open(found_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = convert_wikilinks(content)
    html_content = markdown.markdown(content, extensions=['extra', 'toc'])
    
    template = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shadow Wiki - {{ slug }}</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; max-width: 900px; margin: 40px auto; padding: 0 20px; color: #333; background-color: #f9f9f9; }
            .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
            .back-link { margin-bottom: 20px; display: inline-block; color: #7f8c8d; }
            a { color: #3498db; text-decoration: none; }
            a:hover { text-decoration: underline; }
            pre { background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 5px; overflow-x: auto; }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-link">← Quay lại Trang chủ</a>
            {{ content|safe }}
        </div>
    </body>
    </html>
    """
    return render_template_string(template, content=html_content, slug=slug)

if __name__ == '__main__':
    print("Web App đang chạy tại http://127.0.0.1:2222")
    app.run(host='127.0.0.1', port=2222, debug=True)
