from flask import Flask, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware

if __package__:
    from .Chuong_3.app import ung_dung as chuong_3_app
    from .Chuong_4.app import ung_dung as chuong_4_app
    from .Chuong_5.Tong_hop_chuong5 import app as chuong_5_app
    from .Chuong_6.app import app as chuong_6_app
else:
    from Chuong_3.app import ung_dung as chuong_3_app
    from Chuong_4.app import ung_dung as chuong_4_app
    from Chuong_5.Tong_hop_chuong5 import app as chuong_5_app
    from Chuong_6.app import app as chuong_6_app


CHAPTERS = [
    {
        "number": 3,
        "title": "Chương 3 - Quản lý sinh viên",
        "description": "Danh sách, tìm kiếm, chi tiết sinh viên và API.",
        "url": "/chuong3/",
        "icon": "🎓",
    },
    {
        "number": 4,
        "title": "Chương 4 - Flask",
        "description": "Thực hành xây dựng website với Flask và template.",
        "url": "/chuong4/",
        "icon": "🌐",
    },
    {
        "number": 5,
        "title": "Chương 5 - Bài tập tổng hợp",
        "description": "Máy tính, tính điểm và BMI.",
        "url": "/chuong5/",
        "icon": "🧮",
    },
    {
        "number": 6,
        "title": "Chương 6 - Quản lý tài khoản",
        "description": "Đăng nhập, đăng ký và hồ sơ người dùng.",
        "url": "/chuong6/",
        "icon": "👤",
    },
]

CHAPTER_APPS = {
    "/chuong3": chuong_3_app,
    "/chuong4": chuong_4_app,
    "/chuong5": chuong_5_app,
    "/chuong6": chuong_6_app,
}


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html", chapters=CHAPTERS)

    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, CHAPTER_APPS)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
