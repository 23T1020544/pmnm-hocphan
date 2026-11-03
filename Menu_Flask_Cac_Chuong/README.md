# Menu các chương Flask

## Chạy ứng dụng

Mở terminal tại thư mục `Menu_Flask_Cac_Chuong`, cài các thư viện và khởi động menu:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Mở `http://127.0.0.1:5000/` để chọn chương. Các ứng dụng chương được gắn dưới
các đường dẫn `/chuong3/`, `/chuong4/`, `/chuong5/` và `/chuong6/`; các route
con của mỗi chương vẫn nằm trong thư mục chương tương ứng.

## Cấu trúc

- `app.py`: menu chính và điều phối các ứng dụng chương.
- `Chuong_3/`, `Chuong_4/`, `Chuong_5/`, `Chuong_6/`: ứng dụng Flask, template
  và tài nguyên riêng của từng chương.
- `templates/` và `static/`: giao diện và CSS của menu chính.
