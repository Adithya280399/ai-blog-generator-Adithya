from scheduler import scheduler
from flask import Flask, request, jsonify
from seo_fetcher import get_seo_metrics
from ai_generator import generate_blog_post
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Keyword required'}), 400

    seo_data = get_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo_data)
    # Create safe file name
    safe_filename = keyword.lower().replace(" ", "_")

    # ✅ Save as HTML
    html_path = os.path.join("generated_posts", f"{safe_filename}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        html_content = blog_post.replace("{AFF_LINK_1}", "<a href='https://example.com/product1'>Product 1</a>") \
                            .replace("{AFF_LINK_2}", "<a href='https://example.com/product2'>Product 2</a>")

        f.write(f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{keyword} - AI Blog</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                background-color: #f9f9f9;
                color: #333;
                line-height: 1.6;
            }}
            h1, h2 {{
                color: #2c3e50;
            }}
            a {{
                color: #1e90ff;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            ul, ol {{
                padding-left: 20px;
            }}
            code {{
                background-color: #eee;
                padding: 2px 4px;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
    <h1>{keyword.title()} - Blog Post</h1>
    {html_content}
    </body>
    </html>
    """)

    # ✅ Save the blog post to a file
    safe_filename = keyword.lower().replace(" ", "_") + ".md"
    filepath = os.path.join("generated_posts", safe_filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(blog_post)

    return jsonify({
        'keyword': keyword,
        'seo_data': seo_data,
        'post': blog_post,
        'html_file': html_path
    })

@app.route('/preview', methods=['GET'])
def preview():
    keyword = request.args.get('keyword')
    if not keyword:
        return "Keyword required", 400

    safe_filename = keyword.lower().replace(" ", "_")
    html_path = os.path.join("generated_posts", f"{safe_filename}.html")

    if not os.path.exists(html_path):
        return "Blog post not found", 404

    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)
