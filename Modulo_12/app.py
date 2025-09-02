from flask import Flask, jsonify, request
from calculadora import Calculadora

app = Flask(__name__)
calc = Calculadora()

@app.route('/soma', methods=['GET'])
def soma():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'resultado': calc.somar(a, b)})

@app.route('/divisao', methods=['GET'])
def divisao():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    try:
        resultado = calc.dividir(a, b)
        return jsonify({'resultado': resultado})
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
