import io
import csv
from flask import Flask, request, jsonify, render_template_string, url_for, redirect, abort, make_response

ung_dung = Flask(__name__)

# Dữ liệu sinh viên dùng chung
SINH_VIEN = {
    "23T1020001": {
        "name": "Nguyễn Văn An",
        "Lop": "K47A",
        "scores": {"PMMM": 8.5, "CSDL": 7.0, "NMTT": 9.0}
    },
    "23T1020002": {
        "name": "Trần Thị Bình",
        "Lop": "K47A",
        "scores": {"PMMM": 6.0, "CSDL": 5.5, "NMTT": 7.0}
    },
    "23T1020003": {
        "name": "Lê Hoàng Cường",
        "Lop": "K47B",
        "scores": {"PMMM": 9.5, "CSDL": 9.0}
    },
    "23T1020004": {
        "name": "Phạm Kim Dung",
        "Lop": "K47B",
        "scores": {"PMMM": 4.0, "CSDL": 3.5, "NMTT": 5.0}
    },
    "23T1020005": {
        "name": "Hoàng Thu Hà",
        "Lop": "K47A",
        "scores": {}
    },
    "23T1020006": {
        "name": "Vũ Quốc Khánh",
        "Lop": "K47C",
        "scores": {}
    }
}

STYLE_CHUNG = """
<style>
    :root {
        --mau-chinh: #4f46e5;
        --mau-chinh-hover: #4338ca;
        --mau-nen: #f8fafc;
        --mau-the: #ffffff;
        --mau-chu: #1e293b;
        --mau-phu: #64748b;
        --mau-vien: #e2e8f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    body { background-color: var(--mau-nen); color: var(--mau-chu); display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
    .hop-chua { background-color: var(--mau-the); border-radius: 12px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05); width: 100%; max-width: 800px; padding: 32px; border: 1px solid var(--mau-vien); }
    h1 { color: var(--mau-chinh); margin-bottom: 20px; font-size: 24px; border-bottom: 2px solid var(--mau-vien); padding-bottom: 10px; }
    h3 { margin-top: 24px; margin-bottom: 12px; color: var(--mau-chu); }
    p { margin-bottom: 12px; font-size: 15px; color: var(--mau-phu); }
    p b { color: var(--mau-chu); }
    a { color: var(--mau-chinh); text-decoration: none; font-weight: 500; }
    a:hover { text-decoration: underline; }
    .the-danh-sach { list-style: none; margin: 16px 0; }
    .the-danh-sach li { margin-bottom: 10px; }
    .the-danh-sach a { display: inline-block; padding: 10px 16px; background-color: #f1f5f9; border-radius: 8px; width: 100%; transition: all 0.2s; }
    .the-danh-sach a:hover { background-color: var(--mau-chinh); color: white; text-decoration: none; }
    .bo-loc { background-color: #f1f5f9; padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; font-size: 14px; }
    .bo-loc a { margin: 0 4px; padding: 4px 8px; border-radius: 4px; }
    .bo-loc a.kich-hoat { background-color: var(--mau-chinh); color: white; text-decoration: none; }
    table { width: 100%; border-collapse: collapse; margin-top: 16px; border-radius: 8px; overflow: hidden; border: 1px solid var(--mau-vien); }
    th, td { padding: 12px 16px; text-align: left; }
    th { background-color: #f8fafc; color: var(--mau-phu); font-weight: 600; border-bottom: 1px solid var(--mau-vien); }
    td { border-bottom: 1px solid var(--mau-vien); }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background-color: #f8fafc; }
    .nut-bam { display: inline-block; background-color: var(--mau-chinh); color: white; padding: 10px 18px; border-radius: 8px; border: none; font-size: 14px; font-weight: 500; cursor: pointer; transition: background-color 0.2s; text-decoration: none; margin-top: 10px; }
    .nut-bam:hover { background-color: var(--mau-chinh-hover); text-decoration: none; color: white; }
    .nut-quay-lai { display: inline-block; margin-top: 24px; color: var(--mau-phu); font-size: 14px; }
    .khung-tim-kiem { display: flex; gap: 8px; margin-bottom: 20px; }
    .khung-tim-kiem input[type="text"] { flex: 1; padding: 10px 14px; border: 1px solid var(--mau-vien); border-radius: 8px; font-size: 14px; outline: none; }
    .khung-tim-kiem input[type="text"]:focus { border-color: var(--mau-chinh); }
</style>
"""

# ==========================================
# CÂU 1: GIAO DIỆN TRANG CHỦ
# ==========================================
GIAO_DIEN_CAU_1 = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang chủ - Câu 1</title>
    {STYLE_CHUNG}
</head>
<body>
    <div class="hop-chua">
        <h1>TRANG CHỦ QUẢN LÝ SINH VIÊN (CÂU 1)</h1>
        <p><b>Tổng số sinh viên:</b> {{{{ tong_sinh_vien }}}}</p>
        <p><b>Số lớp (không trùng):</b> {{{{ tong_so_lop }}}}</p>
        
        <ul class="the-danh-sach">
            <li><a href="{{{{ url_for('danh_sach_sinh_vien') }}}}">Xem danh sách sinh viên (/students) - Câu 2</a></li>
            <li><a href="{{{{ url_for('tim_kiem_sinh_vien') }}}}">Tìm kiếm sinh viên an toàn (/search) - Câu 6</a></li>
            <li><a href="{{{{ url_for('api_danh_sach_sinh_vien') }}}}">Xem API sinh viên (/api/students)</a></li>
        </ul>
    </div>
</body>
</html>
"""

# ==========================================
# CÂU 2: GIAO DIỆN DANH SÁCH SINH VIÊN
# ==========================================
GIAO_DIEN_CAU_2 = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Danh sách sinh viên - Câu 2</title>
    {STYLE_CHUNG}
</head>
<body>
    <div class="hop-chua">
        <h1>DANH SÁCH SINH VIÊN (CÂU 2)</h1>
        
        <div class="bo-loc">
            <b>Lọc theo lớp:</b> 
            <a href="{{{{ url_for('danh_sach_sinh_vien') }}}}" class="{{% if not lop_duoc_chon %}}kich-hoat{{% endif %}}">Tất cả</a>
            {{% for lop in danh_sach_lop %}}
                | <a href="{{{{ url_for('danh_sach_sinh_vien', lop=lop) }}}}" class="{{% if lop_duoc_chon == lop %}}kich-hoat{{% endif %}}">{{{{ lop }}}}</a>
            {{% endfor %}}
        </div>

        {{% if danh_sach_sv %}}
        <table>
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
                {{% for sv in danh_sach_sv %}}
                <tr>
                    <td><a href="{{{{ url_for('chi_tiet_sinh_vien', mssv=sv.mssv) }}}}">{{{{ sv.mssv }}}}</a></td>
                    <td>{{{{ sv.ho_ten }}}}</td>
                    <td>{{{{ sv.lop }}}}</td>
                    <td>{{{{ sv.diem_tb }}}}</td>
                    <td>{{{{ sv.xep_loai }}}}</td>
                </tr>
                {{% endfor %}}
            </tbody>
        </table>
        {{% else %}}
        <p>Không tìm thấy sinh viên nào.</p>
        {{% endif %}}

        <a href="{{{{ url_for('trang_chu') }}}}" class="nut-quay-lai">← Quay lại Trang chủ</a>
    </div>
</body>
</html>
"""

# ==========================================
# CÂU 3: GIAO DIỆN CHI TIẾT SINH VIÊN
# ==========================================
GIAO_DIEN_CAU_3 = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chi tiết sinh viên - Câu 3</title>
    {STYLE_CHUNG}
</head>
<body>
    <div class="hop-chua">
        <h1>CHI TIẾT SINH VIÊN (CÂU 3)</h1>
        <p><b>Họ và tên:</b> {{{{ thong_tin.ho_ten }}}}</p>
        <p><b>MSSV:</b> {{{{ thong_tin.mssv }}}}</p>
        <p><b>Lớp:</b> <a href="{{{{ url_for('danh_sach_sinh_vien', lop=thong_tin.lop) }}}}">{{{{ thong_tin.lop }}}}</a></p>
        <p><b>Điểm trung bình:</b> {{{{ thong_tin.diem_tb }}}}</p>
        <p><b>Xếp loại:</b> {{{{ thong_tin.xep_loai }}}}</p>

        <h3>Bảng điểm học phần</h3>
        {{% if thong_tin.bang_diem %}}
        <table>
            <thead>
                <tr>
                    <th>Môn học</th>
                    <th>Điểm số</th>
                </tr>
            </thead>
            <tbody>
                {{% for mon, diem in thong_tin.bang_diem.items() %}}
                <tr>
                    <td>{{{{ mon }}}}</td>
                    <td>{{{{ diem }}}}</td>
                </tr>
                {{% endfor %}}
            </tbody>
        </table>
        {{% else %}}
        <p>Chưa có điểm học phần.</p>
        {{% endif %}}

        <div style="margin-top: 20px; padding-top: 15px; border-top: 1px dashed var(--mau-vien);">
            <p><b>Chức năng mở rộng:</b></p>
            <a href="{{{{ url_for('trang_rut_gon_cau_4', mssv=thong_tin.mssv) }}}}" class="nut-bam">Xem câu 4 (URL Rút gọn)</a>
            <a href="{{{{ url_for('trang_xuat_csv_cau_5', mssv=thong_tin.mssv) }}}}" class="nut-bam">Xem câu 5 (Xuất file CSV)</a>
        </div>

        <br>
        <a href="{{{{ url_for('danh_sach_sinh_vien') }}}}" class="nut-quay-lai">← Quay lại Danh sách sinh viên</a>
    </div>
</body>
</html>
"""

# ==========================================
# CÂU 4: GIAO DIỆN XEM URL RÚT GỌN /sv/<mssv>
# ==========================================
GIAO_DIEN_CAU_4 = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rút gọn URL - Câu 4</title>
    {STYLE_CHUNG}
</head>
<body>
    <div class="hop-chua">
        <h1>RÚT GỌN URL SINH VIÊN (CÂU 4)</h1>
        <p><b>MSSV:</b> {{{{ mssv }}}}</p>
        <p><b>Đường dẫn rút gọn:</b> <code>/sv/{{{{ mssv }}}}</code></p>
        <p><b>Đường dẫn gốc:</b> <code>/students/{{{{ mssv }}}}</code></p>
        <p style="color: green;"><b>Mô tả:</b> Khi truy cập <code>/sv/{{{{ mssv }}}}</code>, hệ thống sẽ trả về mã chuyển hướng <b>301 Permanent Redirect</b> sang đường dẫn chi tiết gốc.</p>
        
        <br>
        <a href="{{{{ url_for('rut_gon_chi_tiet_sinh_vien', mssv=mssv) }}}}" class="nut-bam">Thử truy cập /sv/{{{{ mssv }}}} (Chuyển hướng 301)</a>
        <br><br>
        <a href="{{{{ url_for('chi_tiet_sinh_vien', mssv=mssv) }}}}" class="nut-quay-lai">← Quay lại trang chi tiết</a>
    </div>
</body>
</html>
"""

# ==========================================
# CÂU 5: GIAO DIỆN XUẤT FILE CSV
# ==========================================
GIAO_DIEN_CAU_5 = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xuất file CSV - Câu 5</title>
    {STYLE_CHUNG}
</head>
<body>
    <div class="hop-chua">
        <h1>XUẤT BẢNG ĐIỂM FILE CSV (CÂU 5)</h1>
        <p><b>Họ tên:</b> {{{{ sv.name }}}}</p>
        <p><b>MSSV:</b> {{{{ mssv }}}}</p>
        <p><b>Đường dẫn tải CSV:</b> <code>/students/{{{{ mssv }}}}/export</code></p>
        
        <h3>Xem trước nội dung File CSV:</h3>
        <pre style="background: #f1f5f9; padding: 12px; border-radius: 8px; font-family: monospace;">hoc_phan,diem
{{% for mon, diem in sv.scores.items() %}}{{{{ mon }}}},{{{{ diem }}}}
{{% endfor %}}</pre>

        <br>
        <a href="{{{{ url_for('xuat_bang_diem_csv', mssv=mssv) }}}}" class="nut-bam">Tải xuống file diem_{{{{ mssv }}}}.csv</a>
        <br><br>
        <a href="{{{{ url_for('chi_tiet_sinh_vien', mssv=mssv) }}}}" class="nut-quay-lai">← Quay lại trang chi tiết</a>
    </div>
</body>
</html>
"""

# ==========================================
# CÂU 6: GIAO DIỆN TÌM KIẾM AN TOÀN (CHỐNG XSS)
# ==========================================
GIAO_DIEN_CAU_6 = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tìm kiếm an toàn - Câu 6</title>
    {STYLE_CHUNG}
</head>
<body>
    <div class="hop-chua">
        <h1>TÌM KIẾM AN TOÀN - CHỐNG XSS (CÂU 6)</h1>
        
        <form action="{{{{ url_for('tim_kiem_sinh_vien') }}}}" method="GET" class="khung-tim-kiem">
            <input type="text" name="q" value="{{{{ tu_khoa }}}}" placeholder="Nhập tên hoặc MSSV cần tìm...">
            <button type="submit" class="nut-bam">Tìm kiếm</button>
        </form>

        {{% if da_tim %}}
            <p><b>Tìm thấy {{{{ ket_qua|length }}}} kết quả cho "{{{{ tu_khoa }}}}":</b></p>
            
            {{% if ket_qua %}}
            <table>
                <thead>
                    <tr>
                        <th>MSSV</th>
                        <th>Họ tên</th>
                        <th>Lớp</th>
                        <th>Chi tiết</th>
                    </tr>
                </thead>
                <tbody>
                    {{% for sv in ket_qua %}}
                    <tr>
                        <td>{{{{ sv.mssv }}}}</td>
                        <td>{{{{ sv.ho_ten }}}}</td>
                        <td>{{{{ sv.lop }}}}</td>
                        <td><a href="{{{{ url_for('chi_tiet_sinh_vien', mssv=sv.mssv) }}}}">Xem chi tiết</a></td>
                    </tr>
                    {{% endfor %}}
                </tbody>
            </table>
            {{% else %}}
            <p>Không tìm thấy sinh viên nào phù hợp.</p>
            {{% endif %}}
        {{% endif %}}

        <br>
        <a href="{{{{ url_for('trang_chu') }}}}" class="nut-quay-lai">← Quay lại Trang chủ</a>
    </div>
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

# ------------------------------------------
# ROUTE CÂU 1
# ------------------------------------------
@ung_dung.route('/')
def trang_chu():
    tong_sinh_vien = len(SINH_VIEN)
    cac_lop = set(sv['Lop'] for sv in SINH_VIEN.values())
    tong_so_lop = len(cac_lop)
    return render_template_string(GIAO_DIEN_CAU_1, tong_sinh_vien=tong_sinh_vien, tong_so_lop=tong_so_lop)

# ------------------------------------------
# ROUTE CÂU 2
# ------------------------------------------
@ung_dung.route('/students')
def danh_sach_sinh_vien():
    lop_duoc_chon = request.args.get('lop', '').strip()
    tat_ca_cac_lop = sorted(list(set(sv['Lop'] for sv in SINH_VIEN.values())))
    
    sinh_vien_da_loc = []
    for mssv, thong_tin in SINH_VIEN.items():
        if lop_duoc_chon and thong_tin['Lop'].lower() != lop_duoc_chon.lower():
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
        
    return render_template_string(GIAO_DIEN_CAU_2, danh_sach_sv=sinh_vien_da_loc, danh_sach_lop=tat_ca_cac_lop, lop_duoc_chon=lop_duoc_chon)

# ------------------------------------------
# ROUTE CÂU 3
# ------------------------------------------
@ung_dung.route('/students/<mssv>')
def chi_tiet_sinh_vien(mssv):
    if mssv not in SINH_VIEN:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}")
    
    sv = SINH_VIEN[mssv]
    dtb = tinh_diem_trung_binh(sv['scores'])
    loai = xep_loai_hoc_luc(dtb)
    
    thong_tin_sv = {
        'mssv': mssv,
        'ho_ten': sv['name'],
        'lop': sv['Lop'],
        'diem_tb': dtb if dtb is not None else '-',
        'xep_loai': loai,
        'bang_diem': sv['scores']
    }
    
    return render_template_string(GIAO_DIEN_CAU_3, thong_tin=thong_tin_sv)

# ------------------------------------------
# ROUTE CÂU 4
# ------------------------------------------
@ung_dung.route('/cau-4/<mssv>')
def trang_rut_gon_cau_4(mssv):
    if mssv not in SINH_VIEN:
        abort(404)
    return render_template_string(GIAO_DIEN_CAU_4, mssv=mssv)

@ung_dung.route('/sv/<mssv>')
def rut_gon_chi_tiet_sinh_vien(mssv):
    return redirect(url_for('chi_tiet_sinh_vien', mssv=mssv), code=301)

# ------------------------------------------
# ROUTE CÂU 5 (XUẤT FILE CSV & GIAO DIỆN)
# ------------------------------------------
@ung_dung.route('/cau-5/<mssv>')
def trang_xuat_csv_cau_5(mssv):
    if mssv not in SINH_VIEN:
        abort(404)
    return render_template_string(GIAO_DIEN_CAU_5, mssv=mssv, sv=SINH_VIEN[mssv])

@ung_dung.route('/students/<mssv>/export')
def xuat_bang_diem_csv(mssv):
    if mssv not in SINH_VIEN:
        abort(404, description=f"Không tìm thấy sinh viên với MSSV: {mssv}")
    
    sv = SINH_VIEN[mssv]
    bo_dem = io.StringIO()
    ghi_csv = csv.writer(bo_dem)
    
    ghi_csv.writerow(['hoc_phan', 'diem'])
    for mon, diem in sv['scores'].items():
        ghi_csv.writerow([mon, diem])
        
    phan_hoi = make_response(bo_dem.getvalue())
    phan_hoi.headers["Content-Type"] = "text/csv; charset=utf-8"
    phan_hoi.headers["Content-Disposition"] = f"attachment; filename=diem_{mssv}.csv"
    return phan_hoi

# ------------------------------------------
# ROUTE CÂU 6 (TÌM KIẾM AN TOÀN CHỐNG XSS)
# ------------------------------------------
@ung_dung.route('/search')
def tim_kiem_sinh_vien():
    tu_khoa = request.args.get('q', '')
    ket_qua = []
    da_tim = False

    if 'q' in request.args:
        da_tim = True
        tu_khoa_thuong = tu_khoa.lower().strip()
        if tu_khoa_thuong:
            for mssv, thong_tin in SINH_VIEN.items():
                if tu_khoa_thuong in thong_tin['name'].lower() or tu_khoa_thuong in mssv.lower():
                    ket_qua.append({
                        'mssv': mssv,
                        'ho_ten': thong_tin['name'],
                        'lop': thong_tin['Lop']
                    })

    return render_template_string(GIAO_DIEN_CAU_6, tu_khoa=tu_khoa, ket_qua=ket_qua, da_tim=da_tim)

# API JSON DỮ LIỆU GỐC
@ung_dung.route('/api/students')
def api_danh_sach_sinh_vien():
    return jsonify(SINH_VIEN)

if __name__ == '__main__':
    ung_dung.run(debug=True, port=8008)