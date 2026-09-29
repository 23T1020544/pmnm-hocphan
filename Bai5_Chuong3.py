from flask import Flask, jsonify, url_for
from werkzeug.routing import BaseConverter, ValidationError

class ListConverter(BaseConverter):
    regex = r"-?\d+(?:,-?\d+)*"

    def to_python(self, value):
        try:
            return [int(x) for x in value.split(",")]
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        return ",".join(str(x) for x in value)

app = Flask(__name__)

app.url_map.converters['list'] = ListConverter

@app.route("/sum/<list:numbers>", endpoint="sum_numbers")
def sum_numbers(numbers):
    return jsonify({
        "numbers": numbers,
        "sum": sum(numbers)
    })

if __name__ == "__main__":
    with app.test_request_context():
        print("Test url_for:", url_for("sum_numbers", numbers=[4, 5, 6]))
        
    app.run(debug=True, port=8000)