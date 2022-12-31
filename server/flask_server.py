from flask import Flask, request, jsonify
import utill

app = Flask(__name__)

@app.route('/get_emotions')
def get_emotions():
    response = jsonify({
        'Emotions': utill.get_emotionss()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/prediction', methods=['POST'])
def prediction():
    text = request.form['text']
    response = jsonify({
        'prediction': utill.prediction(text)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("starting the flask server")
    utill.load_saved_model()
    app.run()