from flask import Flask, render_template_string, request

app = Flask(__name__)

GIAO_DIEN_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#f3f6ff">
    <title>Tính điểm học phần</title>
    <style>
        :root {
            color-scheme: light;
            font-family: "Segoe UI", Arial, sans-serif;
            color: #17213b;
            background: #f3f6ff;
            font-synthesis: none;
            text-rendering: optimizeLegibility;
        }

        * {
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            margin: 0;
            padding: 48px 20px;
            background:
                radial-gradient(ellipse at 12% 8%, #dce7ff 0, transparent 34%),
                radial-gradient(ellipse at 90% 90%, #e8e1ff 0, transparent 30%),
                #f7f8fc;
        }

        .khung-tinh-diem {
            width: min(100%, 920px);
            margin: 0 auto;
            overflow: hidden;
            border: 1px solid #e7eaf2;
            border-radius: 24px;
            background: #fff;
            box-shadow: 0 24px 70px rgba(35, 48, 87, 0.12);
        }

        .dau-trang {
            padding: 38px 44px 32px;
            color: #fff;
            background: linear-gradient(120deg, #253e91, #5267d8 60%, #7869df);
        }

        .nhan-nho {
            margin: 0 0 10px;
            color: #dbe3ff;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }

        h1 {
            margin: 0;
            font-size: clamp(1.8rem, 4vw, 2.5rem);
            letter-spacing: -0.04em;
        }

        .mo-ta {
            max-width: 560px;
            margin: 12px 0 0;
            color: #e5e9ff;
            line-height: 1.65;
        }

        .noi-dung {
            display: grid;
            grid-template-columns: minmax(0, 1.4fr) minmax(220px, 0.8fr);
            gap: 36px;
            padding: 36px 44px 42px;
        }

        .tieu-de-khu-vuc {
            margin: 0 0 22px;
            font-size: 1.1rem;
            letter-spacing: -0.02em;
        }

        .nhom-nhap-lieu {
            margin-bottom: 18px;
        }

        label {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 8px;
            color: #303b58;
            font-size: 0.92rem;
            font-weight: 650;
        }

        .ti-le {
            color: #6674bd;
            font-size: 0.82rem;
            font-weight: 700;
        }

        input[type="text"] {
            width: 100%;
            min-height: 48px;
            padding: 12px 14px;
            border: 1px solid #dfe3ee;
            border-radius: 11px;
            outline: none;
            background: #fbfcff;
            color: #17213b;
            font: inherit;
            transition: border-color 160ms ease, box-shadow 160ms ease, background 160ms ease;
        }

        input[type="text"]::placeholder {
            color: #a0a8bb;
        }

        input[type="text"]:hover {
            border-color: #b9c2e0;
        }

        input[type="text"]:focus {
            border-color: #596cdb;
            background: #fff;
            box-shadow: 0 0 0 4px rgba(89, 108, 219, 0.13);
        }

        .thong-bao-loi {
            margin-top: 7px;
            color: #c3334b;
            font-size: 0.84rem;
        }

        .ket-qua {
            margin-top: 22px;
            padding: 18px 20px;
            border: 1px solid #cbd5ff;
            border-radius: 14px;
            background: linear-gradient(135deg, #f2f5ff, #f8f5ff);
            color: #293b92;
            font-size: 1.15rem;
            font-weight: 750;
            line-height: 1.5;
        }

        button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 9px;
            min-height: 48px;
            margin-top: 3px;
            padding: 0 22px;
            border: none;
            border-radius: 11px;
            background: #4359c7;
            color: #fff;
            font: inherit;
            font-weight: 700;
            box-shadow: 0 8px 18px rgba(67, 89, 199, 0.22);
            cursor: pointer;
            transition: transform 160ms ease, background 160ms ease, box-shadow 160ms ease;
        }

        button:hover {
            transform: translateY(-1px);
            background: #354bb4;
            box-shadow: 0 11px 22px rgba(67, 89, 199, 0.28);
        }

        button:focus-visible {
            outline: 3px solid #aab6ff;
            outline-offset: 3px;
        }

        .thong-tin {
            align-self: start;
            padding: 22px;
            border: 1px solid #e7eaf2;
            border-radius: 16px;
            background: #f9faff;
        }

        .thong-tin h2 {
            margin: 0 0 16px;
            font-size: 0.96rem;
        }

        .trong-so {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            padding: 12px 0;
            border-bottom: 1px solid #e8eaf2;
            color: #59637b;
            font-size: 0.88rem;
        }

        .trong-so:last-of-type {
            border-bottom: 0;
        }

        .trong-so strong {
            color: #303d78;
        }

        .ghi-chu {
            margin: 18px 0 0;
            padding-top: 15px;
            border-top: 1px solid #e8eaf2;
            color: #768099;
            font-size: 0.8rem;
            line-height: 1.6;
        }

        @media (max-width: 680px) {
            body {
                padding: 20px 12px;
            }

            .khung-tinh-diem {
                border-radius: 18px;
            }

            .dau-trang {
                padding: 29px 24px 26px;
            }

            .noi-dung {
                grid-template-columns: 1fr;
                gap: 26px;
                padding: 28px 24px 30px;
            }

            .thong-tin {
                padding: 18px;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                transition-duration: 0.01ms !important;
            }
        }
    </style>
</head>
<body>

    <div class="khung-tinh-diem">
        <header class="dau-trang">
            <p class="nhan-nho">Công cụ học tập</p>
            <h1>Tính điểm học phần</h1>
            <p class="mo-ta">Nhập điểm từng thành phần để xem điểm tổng kết và xếp loại học phần của bạn.</p>
        </header>

        <main class="noi-dung">
            <section aria-labelledby="tieu-de-nhap-diem">
                <h2 class="tieu-de-khu-vuc" id="tieu-de-nhap-diem">Điểm thành phần</h2>
                <form action="/" method="POST">
                    <div class="nhom-nhap-lieu">
                        <label for="chuyen_can">
                            <span>Điểm chuyên cần</span>
                            <span class="ti-le">10%</span>
                        </label>
                        <input type="text" id="chuyen_can" name="chuyen_can" inputmode="decimal"
                               placeholder="Ví dụ: 8,5" value="{{ giat_tri_chuyen_can }}"
                               {% if loi_chuyen_can %}aria-invalid="true" aria-describedby="loi-chuyen-can"{% endif %}>
                        {% if loi_chuyen_can %}
                            <div class="thong-bao-loi" id="loi-chuyen-can">{{ loi_chuyen_can }}</div>
                        {% endif %}
                    </div>

                    <div class="nhom-nhap-lieu">
                        <label for="giua_ky">
                            <span>Điểm giữa kỳ</span>
                            <span class="ti-le">30%</span>
                        </label>
                        <input type="text" id="giua_ky" name="giua_ky" inputmode="decimal"
                               placeholder="Ví dụ: 7,5" value="{{ giat_tri_giua_ky }}"
                               {% if loi_giua_ky %}aria-invalid="true" aria-describedby="loi-giua-ky"{% endif %}>
                        {% if loi_giua_ky %}
                            <div class="thong-bao-loi" id="loi-giua-ky">{{ loi_giua_ky }}</div>
                        {% endif %}
                    </div>

                    <div class="nhom-nhap-lieu">
                        <label for="cuoi_ky">
                            <span>Điểm cuối kỳ</span>
                            <span class="ti-le">60%</span>
                        </label>
                        <input type="text" id="cuoi_ky" name="cuoi_ky" inputmode="decimal"
                               placeholder="Ví dụ: 9" value="{{ giat_tri_cuoi_ky }}"
                               {% if loi_cuoi_ky %}aria-invalid="true" aria-describedby="loi-cuoi-ky"{% endif %}>
                        {% if loi_cuoi_ky %}
                            <div class="thong-bao-loi" id="loi-cuoi-ky">{{ loi_cuoi_ky }}</div>
                        {% endif %}
                    </div>

                    <button type="submit">Tính điểm <span aria-hidden="true">→</span></button>
                </form>

                {% if chuoi_ket_qua %}
                    <div class="ket-qua" role="status" aria-live="polite">
                        Kết quả: {{ chuoi_ket_qua }}
                    </div>
                {% endif %}
            </section>

            <aside class="thong-tin" aria-labelledby="tieu-de-trong-so">
                <h2 id="tieu-de-trong-so">Cách tính điểm</h2>
                <div class="trong-so"><span>Chuyên cần</span><strong>10%</strong></div>
                <div class="trong-so"><span>Giữa kỳ</span><strong>30%</strong></div>
                <div class="trong-so"><span>Cuối kỳ</span><strong>60%</strong></div>
                <p class="ghi-chu">Thang điểm từ 0 đến 10. Có thể nhập số thập phân bằng dấu phẩy hoặc dấu chấm.</p>
            </aside>
        </main>
    </div>

</body>
</html>
"""

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

@app.route('/', methods=['GET', 'POST'])
def tinh_diem_hoc_phan():
    giat_tri_chuyen_can = ""
    giat_tri_giua_ky = ""
    giat_tri_cuoi_ky = ""
    
    loi_chuyen_can = None
    loi_giua_ky = None
    loi_cuoi_ky = None
    chuoi_ket_qua = None

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

    return render_template_string(
        GIAO_DIEN_HTML,
        giat_tri_chuyen_can=giat_tri_chuyen_can,
        giat_tri_giua_ky=giat_tri_giua_ky,
        giat_tri_cuoi_ky=giat_tri_cuoi_ky,
        loi_chuyen_can=loi_chuyen_can,
        loi_giua_ky=loi_giua_ky,
        loi_cuoi_ky=loi_cuoi_ky,
        chuoi_ket_qua=chuoi_ket_qua
    )

if __name__ == '__main__':
    app.run(debug=True)