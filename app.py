from flask import Flask, request, jsonify
import joblib
import os
import cv2
from model import get_predicted_roll_numbers

app = Flask(__name__)

knn_model = joblib.load('knn_model.joblib')


@app.route('/predict_roll_numbers',methods=['POST','GET'])
def predict_roll_numbers_api():
    test_image_path = request.json['test_image_path']
    roll_numbers = get_predicted_roll_numbers(knn_model,test_image_path)
    roll_numbers = [roll_number.tolist() for roll_number in roll_numbers]
    return jsonify({'roll_numbers':roll_numbers})


if __name__ == '__main__':
    app.run(debug = True)

