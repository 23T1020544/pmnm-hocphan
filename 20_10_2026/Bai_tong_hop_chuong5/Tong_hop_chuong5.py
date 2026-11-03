from flask import Flask, render_template, request

app = Flask(__name__)

# --- HÀM XỬ LÝ BÀI 1 & BÀI 2 ---
def parse_number(val):
    if val is None or val.strip() == "":
        return None, "Vui lòng nhập một số."
    val_clean = val.strip().replace(',', '.')
    try:
        return float(val_clean), None
    except ValueError:
        return None, "Vui lòng nhập một số."

def kiem_tra_va_chuyen_diem(gia_tri_nhap):
    if gia_tri_nhap is None or gia_tri_nhap.strip() == "":
        return None, "Vui lòng nhập một số."
    gia_tri_sach = gia_tri_nhap.strip().replace(',', '.')
    try:
        diem_so = float(gia_tri_sach)
        if diem_so < 0 or diem_so > 10:
            return None, "Điểm phải từ 0 đến 10."
        return diem_so, None
    except ValueError:
        return None, "Vui lòng nhập một số."

# --- HÀM XỬ LÝ BÀI 3 (BMI) ---
def validate_height(val):
    if val is None or val.strip() == "":
        return None, "Vui lòng nhập một số."
    val_clean = val.strip().replace(',', '.')
    try:
        num = float(val_clean)
        if num > 0 and num < 10:
            return None, "Giá trị phải từ 50 đến 250. (nhập mét thay vì cm)"
        if num < 50 or num > 250:
            return None, "Giá trị phải từ 50 đến 250."
        return num, None
    except ValueError:
        return None, "Vui lòng nhập một số."

def validate_weight(val):
    if val is None or val.strip() == "":
        return None, "Vui lòng nhập một số."
    val_clean = val.strip().replace(',', '.')
    try:
        num = float(val_clean)
        if num < 10 or num > 300:
            return None, "Giá trị phải từ 10 đến 300."
        return num, None
    except ValueError:
        return None, "Vui lòng nhập một số."


# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def calculator():
    val_a, val_b, selected_op = "", "", "+"
    error_a, error_b, result_str = None, None, None

    if request.method == 'POST':
        val_a = request.form.get('a', '')
        val_b = request.form.get('b', '')
        selected_op = request.form.get('op', '+')

        num_a, error_a = parse_number(val_a)
        num_b, error_b = parse_number(val_b)

        valid_ops = ['+', '-', '*', '/']
        if selected_op not in valid_ops:
            result_str = "Phép toán không hợp lệ."
            error_a = None
            error_b = None
        elif error_a is None and error_b is None:
            if selected_op == '+': res = num_a + num_b
            elif selected_op == '-': res = num_a - num_b
            elif selected_op == '*': res = num_a * num_b
            elif selected_op == '/':
                if num_b == 0:
                    error_b = "Không thể chia cho 0."
                else:
                    res = num_a / num_b

            if error_b is None:
                res_formatted = int(res) if res.is_integer() else res
                a_formatted = int(num_a) if num_a.is_integer() else num_a
                b_formatted = int(num_b) if num_b.is_integer() else num_b
                result_str = f"{a_formatted} {selected_op} {b_formatted} = {res_formatted}"

    return render_template(
        'may_tinh.html',
        val_a=val_a, val_b=val_b, selected_op=selected_op,
        error_a=error_a, error_b=error_b, result_str=result_str
    )

@app.route('/tinh-diem', methods=['GET', 'POST'])
def tinh_diem_hoc_phan():
    giat_tri_chuyen_can, giat_tri_giua_ky, giat_tri_cuoi_ky = "", "", ""
    loi_chuyen_can, loi_giua_ky, loi_cuoi_ky, chuoi_ket_qua = None, None, None, None

    if request.method == 'POST':
        giat_tri_chuyen_can = request.form.get('chuyen_can', '')
        giat_tri_giua_ky = request.form.get('giua_ky', '')
        giat_tri_cuoi_ky = request.form.get('cuoi_ky', '')

        diem_chuyen_can, loi_chuyen_can = kiem_tra_va_chuyen_diem(giat_tri_chuyen_can)
        diem_giua_ky, loi_giua_ky = kiem_tra_va_chuyen_diem(giat_tri_giua_ky)
        diem_cuoi_ky, loi_cuoi_ky = kiem_tra_va_chuyen_diem(giat_tri_cuoi_ky)

        if loi_chuyen_can is None and loi_giua_ky is None and loi_cuoi_ky is None:
            diem_tong_ket = round(diem_chuyen_can * 0.1 + diem_giua_ky * 0.3 + diem_cuoi_ky * 0.6, 1)
            
            if diem_cuoi_ky < 1.0:
                diem_chu = "F (điểm thi dưới 1)"
            elif diem_tong_ket >= 8.5:
                diem_chu = "A"
            elif diem_tong_ket >= 7.0:
                diem_chu = "B"
            elif diem_tong_ket >= 5.5:
                diem_chu = "C"
            elif diem_tong_ket >= 4.0:
                diem_chu = "D"
            else:
                diem_chu = "F"

            chuoi_ket_qua = f"{diem_tong_ket:.1f}  {diem_chu}"

    return render_template(
        'tinh_diem.html',
        giat_tri_chuyen_can=giat_tri_chuyen_can,
        giat_tri_giua_ky=giat_tri_giua_ky,
        giat_tri_cuoi_ky=giat_tri_cuoi_ky,
        loi_chuyen_can=loi_chuyen_can,
        loi_giua_ky=loi_giua_ky,
        loi_cuoi_ky=loi_cuoi_ky,
        chuoi_ket_qua=chuoi_ket_qua
    )

@app.route('/bmi', methods=['GET', 'POST'])
def tinh_bmi():
    val_cao, val_nang = "", ""
    error_cao, error_nang = None, None
    bmi_val, phan_loai, mau_ket_qua, can_nang_nen_co = None, None, None, None

    if request.method == 'POST':
        val_cao = request.form.get('cao', '')
        val_nang = request.form.get('nang', '')

        height_cm, error_cao = validate_height(val_cao)
        weight_kg, error_nang = validate_weight(val_nang)

        if error_cao is None and error_nang is None:
            height_m = height_cm / 100.0
            bmi = round(weight_kg / (height_m ** 2), 1)
            
            if bmi < 18.5:
                phan_loai = "Thiếu cân"
                mau_ket_qua = "vang"
            elif bmi < 23.0:
                phan_loai = "Bình thường"
                mau_ket_qua = "xanh"
            elif bmi < 25.0:
                phan_loai = "Thừa cân"
                mau_ket_qua = "vang"
            else:
                phan_loai = "Béo phì"
                mau_ket_qua = "do"

            min_weight = round(18.5 * (height_m ** 2), 1)
            max_weight = round(22.9 * (height_m ** 2), 1)
            
            bmi_val = f"{bmi:.1f}"
            can_nang_nen_co = f"{min_weight} - {max_weight} kg"

    return render_template(
        'bmi.html',
        val_cao=val_cao,
        val_nang=val_nang,
        error_cao=error_cao,
        error_nang=error_nang,
        bmi_val=bmi_val,
        phan_loai=phan_loai,
        mau_ket_qua=mau_ket_qua,
        can_nang_nen_co=can_nang_nen_co
    )

if __name__ == '__main__':
    app.run(debug=True)