from flask import Flask

app = Flask(__name__)

@app.route("/square/<n>")
def square(n):
    try:
        val = int(n)
        return f"Bình phương của {val} là: {val**2}"
    except ValueError:
        return "Vui lòng nhập một số nguyên!", 400