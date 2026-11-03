from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

POSTS = [
    {
        "id": 1,
        "title": "HTML cơ bản",
        "author": "Admin",
        "content": "Tìm hiểu cách xây dựng cấu trúc một trang web bằng HTML.",
        "created": date(2026, 10, 13),
        "tags": ["HTML", "Công nghệ"]
    },
    {
        "id": 2,
        "title": "CSS cơ bản",
        "author": "Admin",
        "content": "Học cách trình bày giao diện website bằng CSS.",
        "created": date(2026, 10, 12),
        "tags": ["CSS", "Thiết kế web"]
    }
]

@app.template_filter("ngay")
def format_date(value, fmt="%d/%m/%Y"):
    if value is None:
        return ""
    return value.strftime(fmt)

@app.context_processor
def inject_globals():
    return {
        "site_name": "Mini Blog",
        "current_year": date.today().year,
        "post_count": len(POSTS)
    }

@app.route("/")
def index():
    posts = sorted(POSTS, key=lambda p: p["created"], reverse=True)
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)