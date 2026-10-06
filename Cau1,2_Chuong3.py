from flask import Flask, request, jsonify, render_template_string, url_for

ung_dung = Flask(__name__)

SINH_VIEN = {
    "2311020001": {
        "name": "Nguyễn Văn An",
        "Lop": "K47A",
        "scores": {"PMMM": 8.5, "CSDL": 7.0, "NMTT": 9.0}
    },
    "2311020002": {
        "name": "Trần Thị Bình",
        "Lop": "K47A",
        "scores": {"PMMM": 6.0, "CSDL": 5.5, "NMTT": 7.0}
    },
    "2311020003": {
        "name": "Lê Hoàng Cường",
        "Lop": "K47B",
        "scores": {"PMMM": 9.5, "CSDL": 9.0}
    },
    "2311020004": {
        "name": "Phạm Kim Dung",
        "Lop": "K47B",
        "scores": {"PMMM": 4.0, "CSDL": 3.5, "NMTT": 5.0}
    },
    "2311020005": {
        "name": "Hoàng Thu Hà",
        "Lop": "K47A",
        "scores": {}
    },
    "2311020006": {
        "name": "Vũ Quốc Khánh",
        "Lop": "K47C",
        "scores": {}
    }
}

MAU_TRANG_CHU = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Trang chủ</title>
</head>
<body>
    <h1>TRANG CHỦ</h1>
    <p>Tổng số sinh viên: {{ tong_sinh_vien }}</p>
    <p>Số lớp (không trùng): {{ tong_so_lop }}</p>
    <ul>
        <li><a href="{{ url_for('danh_sach_sinh_vien') }}">Xem danh sách sinh viên (/students)</a></li>
        <li><a href="{{ url_for('api_danh_sach_sinh_vien') }}">Xem API sinh viên (/api/students)</a></li>
    </ul>
</body>
</html>
"""

MAU_DANH_SACH = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Danh sách sinh viên</title>
</head>
<body>
    <h1>DANH SÁCH SINH VIÊN</h1>
    
    <div>
        Thanh lọc: 
        <a href="{{ url_for('danh_sach_sinh_vien') }}">Tất cả</a>
        {% for lop in danh_sach_lop %}
            | <a href="{{ url_for('danh_sach_sinh_vien', lop=lop) }}">{{ lop }}</a>
        {% endfor %}
    </div>

    <br>

    {% if danh_sach_sv %}
    <table border="1" cellpadding="8" cellspacing="0">
        <thead>
            <tr>
                <th>MSSV</th>
                <th>Họ tên</th>
                <th>Lớp</th>
                <th>Điểm TB</th>
                <th>Xếp loại</th>
            </tr>
        </thead>
        <tbody>
            {% for sv in danh_sach_sv %}
            <tr>
                <td><a href="/students/{{ sv.mssv }}">{{ sv.mssv }}</a></td>
                <td>{{ sv.ho_ten }}</td>
                <td>{{ sv.lop }}</td>
                <td>{{ sv.diem_tb }}</td>
                <td>{{ sv.xep_loai }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% else %}
    <p>Không có sinh viên phù hợp.</p>
    {% endif %}

    <br>
    <a href="{{ url_for('trang_chu') }}">Quay lại Trang chủ</a>
</body>
</html>
"""

def tinh_diem_trung_binh(diem_so):
    if not diem_so:
        return None
    return round(sum(diem_so.values()) / len(diem_so), 2)

def xep_loai_hoc_luc(diem_trung_binh):
    if diem_trung_binh is None:
        return "-"
    if diem_trung_binh >= 8.0:
        return "Giỏi"
    elif diem_trung_binh >= 6.5:
        return "Khá"
    elif diem_trung_binh >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

@ung_dung.route('/')
def trang_chu():
    tong_sinh_vien = len(SINH_VIEN)
    cac_lop = set(sv['Lop'] for sv in SINH_VIEN.values())
    tong_so_lop = len(cac_lop)
    return render_template_string(MAU_TRANG_CHU, tong_sinh_vien=tong_sinh_vien, tong_so_lop=tong_so_lop)

@ung_dung.route('/students')
def danh_sach_sinh_vien():
    lop_duoc_chon = request.args.get('lop', '').strip()
    tat_ca_cac_lop = sorted(list(set(sv['Lop'] for sv in SINH_VIEN.values())))
    
    sinh_vien_da_loc = []
    for mssv, thong_tin in SINH_VIEN.items():
        if lop_duoc_chon:
            if thong_tin['Lop'].lower() != lop_duoc_chon.lower():
                continue
        dtb = tinh_diem_trung_binh(thong_tin['scores'])
        loai = xep_loai_hoc_luc(dtb)
        sinh_vien_da_loc.append({
            'mssv': mssv,
            'ho_ten': thong_tin['name'],
            'lop': thong_tin['Lop'],
            'diem_tb': dtb if dtb is not None else '-',
            'xep_loai': loai
        })
        
    return render_template_string(MAU_DANH_SACH, danh_sach_sv=sinh_vien_da_loc, danh_sach_lop=tat_ca_cac_lop, lop_duoc_chon=lop_duoc_chon)

@ung_dung.route('/api/students')
def api_danh_sach_sinh_vien():
    return jsonify(SINH_VIEN)

if __name__ == '__main__':
    ung_dung.run(debug=True, port=8008)