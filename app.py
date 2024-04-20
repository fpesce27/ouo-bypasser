from flask import Flask, request, jsonify
from model import detect_bypass

app = Flask(__name__)

@app.route('/bypass')
def bypass():
    try:
        data = request.args.get('url')
        Shorten_provider = detect_bypass(data)
        url = Shorten_provider.bypass(data)

        return jsonify({'url': url}), 200
    except Exception as e:
        mensaje = 'An error ocurred'
        detalles = str(e)
        print(detalles)
        return jsonify({'error': mensaje, 'details': detalles}), 500

if __name__ == '__main__':
    app.run()