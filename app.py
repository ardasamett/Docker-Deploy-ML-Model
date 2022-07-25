from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('models/model.pkl', 'rb'))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    print(data["experience"])
    prediction = model.predict([[data["experience"]]])
    
    return jsonify(prediction[0][0])


if __name__ == "__main__":
    app.run(debug=True)