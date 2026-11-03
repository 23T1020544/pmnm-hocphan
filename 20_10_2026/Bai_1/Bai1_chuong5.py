from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#f3f6ff">
    <title>Máy tính cơ bản</title>
    <style>
        :root {
            color-scheme: light;
            font-family: "Segoe UI", Arial, sans-serif;
            color: #18233d;
            background: #f3f6ff;
            font-synthesis: none;
            text-rendering: optimizeLegibility;
        }

        * {
            box-sizing: border-box;
        }

        body {
            display: grid;
            min-height: 100vh;
            place-items: center;
            margin: 0;
            padding: 32px 16px;
            background:
                radial-gradient(ellipse at 12% 8%, #dce7ff 0, transparent 34%),
                radial-gradient(ellipse at 90% 90%, #e8e1ff 0, transparent 30%),
                #f7f8fc;
        }

        .calculator-form {
            width: min(100%, 520px);
            overflow: hidden;
            border: 1px solid #e7eaf2;
            border-radius: 24px;
            background: #fff;
            box-shadow: 0 24px 70px rgba(35, 48, 87, 0.13);
        }

        .header {
            padding: 32px 36px 28px;
            color: #fff;
            background: linear-gradient(120deg, #253e91, #5267d8 62%, #7869df);
        }

        .eyebrow {
            margin: 0 0 9px;
            color: #dbe3ff;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }

        h1 {
            margin: 0;
            font-size: clamp(1.7rem, 5vw, 2.1rem);
            letter-spacing: -0.04em;
        }

        .intro {
            margin: 10px 0 0;
            color: #e5e9ff;
            font-size: 0.94rem;
            line-height: 1.6;
        }

        .content {
            padding: 30px 36px 34px;
        }

        .section-title {
            margin: 0 0 22px;
            font-size: 1.05rem;
            letter-spacing: -0.02em;
        }

        .form-group {
            margin-bottom: 19px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #303b58;
            font-size: 0.9rem;
            font-weight: 650;
        }

        input[type="text"], select {
            width: 100%;
            min-height: 49px;
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

        select {
            cursor: pointer;
        }

        input[type="text"]:hover, select:hover {
            border-color: #b9c2e0;
        }

        input[type="text"]:focus, select:focus {
            border-color: #596cdb;
            background: #fff;
            box-shadow: 0 0 0 4px rgba(89, 108, 219, 0.13);
        }

        .error-message {
            margin-top: 7px;
            color: #c3334b;
            font-size: 0.84rem;
        }

        .result {
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
            min-height: 49px;
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

        button:focus-visible, .clear-link:focus-visible {
            outline: 3px solid #aab6ff;
            outline-offset: 3px;
        }

        .actions {
            display: flex;
            align-items: center;
            gap: 18px;
            margin-top: 4px;
        }

        .clear-link {
            color: #65708a;
            font-size: 0.9rem;
            font-weight: 600;
            text-decoration: none;
        }

        .clear-link:hover {
            color: #354bb4;
            text-decoration: underline;
        }

        .hint {
            margin: 21px 0 0;
            padding-top: 17px;
            border-top: 1px solid #edf0f6;
            color: #768099;
            font-size: 0.82rem;
            line-height: 1.6;
        }

        @media (max-width: 520px) {
            body {
                padding: 16px 10px;
            }

            .calculator-form {
                border-radius: 18px;
            }

            .header {
                padding: 26px 23px 23px;
            }

            .content {
                padding: 25px 23px 28px;
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

    <div class="calculator-form">
        <header class="header">
            <p class="eyebrow">Công cụ tính toán</p>
            <h1>Máy tính cơ bản</h1>
            <p class="intro">Thực hiện nhanh các phép tính cộng, trừ, nhân và chia.</p>
        </header>

        <main class="content">
            <h2 class="section-title">Nhập phép tính của bạn</h2>
            <form action="/" method="POST">
            
                <div class="form-group">
                    <label for="a">Số thứ nhất</label>
                    <input type="text" id="a" name="a" inputmode="decimal"
                           placeholder="Ví dụ: 12,5" value="{{ val_a }}"
                           {% if error_a %}aria-invalid="true" aria-describedby="error-a"{% endif %}>
                    {% if error_a %}
                        <div class="error-message" id="error-a">{{ error_a }}</div>
                    {% endif %}
                </div>

                <div class="form-group">
                    <label for="op">Phép toán</label>
                    <select id="op" name="op">
                        <option value="+" {% if selected_op == '+' %}selected{% endif %}>Cộng (+)</option>
                        <option value="-" {% if selected_op == '-' %}selected{% endif %}>Trừ (-)</option>
                        <option value="*" {% if selected_op == '*' %}selected{% endif %}>Nhân (×)</option>
                        <option value="/" {% if selected_op == '/' %}selected{% endif %}>Chia (÷)</option>
                        {% if selected_op not in ['+', '-', '*', '/'] %}
                            <option value="{{ selected_op }}" selected>{{ selected_op }}</option>
                        {% endif %}
                    </select>
                </div>

                <div class="form-group">
                    <label for="b">Số thứ hai</label>
                    <input type="text" id="b" name="b" inputmode="decimal"
                           placeholder="Ví dụ: 3" value="{{ val_b }}"
                           {% if error_b %}aria-invalid="true" aria-describedby="error-b"{% endif %}>
                    {% if error_b %}
                        <div class="error-message" id="error-b">{{ error_b }}</div>
                    {% endif %}
                </div>

                <div class="actions">
                    <button type="submit">Tính kết quả <span aria-hidden="true">→</span></button>
                    <a class="clear-link" href="/">Xóa dữ liệu</a>
                </div>
            </form>

            {% if result_str %}
                <div class="result" role="status" aria-live="polite">
                    Kết quả: {{ result_str }}
                </div>
            {% endif %}
            <p class="hint">Mẹo: Bạn có thể nhập số thập phân bằng dấu phẩy hoặc dấu chấm.</p>
        </main>
    </div>

</body>
</html>
"""

def parse_number(val):
    if val is None or val.strip() == "":
        return None, "Vui lòng nhập một số."
    
    val_clean = val.strip().replace(',', '.')
    
    try:
        num = float(val_clean)
        return num, None
    except ValueError:
        return None, "Vui lòng nhập một số."

@app.route('/', methods=['GET', 'POST'])
def calculator():
    val_a = ""
    val_b = ""
    selected_op = "+"
    
    error_a = None
    error_b = None
    result_str = None

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
            if selected_op == '+':
                res = num_a + num_b
            elif selected_op == '-':
                res = num_a - num_b
            elif selected_op == '*':
                res = num_a * num_b
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

    return render_template_string(
        HTML_TEMPLATE,
        val_a=val_a,
        val_b=val_b,
        selected_op=selected_op,
        error_a=error_a,
        error_b=error_b,
        result_str=result_str
    )

if __name__ == '__main__':
    app.run(debug=True)