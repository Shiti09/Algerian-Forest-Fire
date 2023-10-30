import pickle
from flask import Flask, request, app, jsonify, url_for, render_template, redirect
import numpy as np
import pandas as pd
from loggerMain import FirePredictLogger
import pymongo
import io
import os
import time
from werkzeug.serving import make_server

app = Flask(__name__)
model= pickle.load(open('R_model.pkl', 'rb'))
modelC= pickle.load(open('C_model.pkl', 'rb'))

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["data1"]
collection = db["data1"]

@app.route('/')
def home():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Index initialization successfull")
        #return 'Hello World'
        return render_template('index.html')
    except Exception as e:
        log.exception(" Something went wrong on initiation process")

"""@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("predict_api for Postman initialization successfull")
        data = request.json['data']
        print(data)
        new_data = [list(data.values())]
        output = int(modelC.predict(new_data)[0])
        log.info("Predication for predict_api successfull with value")
        print(data)
        print(new_data)
        return jsonify(output)
    except Exception as e:
        log.exception(" Something went wrong on predict_api for Postman process")"""

@app.route('/singlereg', methods=['GET', 'POST'])
def Single_Regression():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Single regression initialization successfull")
     
        return render_template('singlereg.html')
    except Exception as e:
        log.exception(" Something went wrong on Single regression initiation process")

@app.route('/classi', methods=['GET', 'POST'])
def Single_Classification():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Single classification initialization successfull")
     
        return render_template('classi.html')
    except Exception as e:
        log.exception(" Something went wrong on Single classification initiation process")

@app.route('/Cpredict', methods=['POST'])
def Sclassi_prediction():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Single classification prediction initialization successfull")
        data = [float(x) for x in request.form.values()]
        final_features = [np.array(data)]
        print(data)
        print(final_features)
        output = int(modelC.predict(final_features)[0])
        log.info("Predication for Sclassi_prediction successfull with value")
        print(output)
        if output == 0:
            return render_template('nofire.html')
        else:
            return render_template('fire.html')
    except Exception as e:
        log.exception(" Something went wrong on Single classification prediction initiation process")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Single regression prediction initialization successfull")
        data = [float(x) for x in request.form.values()]
        final_features = [np.array(data)]
        print(data)
        
        output = model.predict(final_features)[0]
        log.info("Prediction for predict-single regression successfull with value")
        print(output)
        
        return render_template('singlereg.html', prediction_text = "Predicted Temperature is  {:.2f} ".format(output))
    except Exception as e:
        log.exception(" Something went wrong on Single regression prediction initiation process")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Regression Batch prediction upload initialization successfull")

        if request.method == 'POST':
            if 'file' not in request.files:
                return redirect(request.url)

            file = request.files['file']

            if file.filename == '':
                return redirect(request.url)

            if file:
                # Read the CSV data from the uploaded file
                csv_data = file.read().decode('utf-8')
                df = pd.read_csv(io.StringIO(csv_data))

                # Make predictions using your model
                predictions = model.predict(df)  # Assumes df contains the input features for predictions
                log.info("Prediction for upload-batch regression successfull with value")

                # You can store the predictions or do further processing here

                # Render a page displaying the predictions
                zipped_data = list(zip(df.values.tolist(), predictions))
                return render_template('predictions.html', zipped_data=zipped_data, predictions=predictions)
        return render_template('upload_csv.html')
    except Exception as e:
        log.exception(" Something went wrong on Regression Batch prediction upload  initiation process")        

@app.route('/predictions', methods=['GET'])
def display_predictions():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Regression Batch prediction output initialization successfull")
        # Fetch data from MongoDB
        data = list(collection.find({}))
        
        # Make predictions using the model
        predictions = [model.predict([d['features']])[0] for d in data]
        log.info("Prediction for predictions-batch regression successfull with value")
        return render_template('predictions.html', data = data, predictions=predictions)
    except Exception as e:
        log.exception(" Something went wrong on Regression Batch prediction output  initiation process") 

@app.route('/uploadC', methods=['GET', 'POST'])
def uploadC_file():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Classification Batch prediction upload initialization successfull")

        if request.method == 'POST':
            if 'file' not in request.files:
                return redirect(request.url)

            file = request.files['file']

            if file.filename == '':
                return redirect(request.url)

            if file:
                # Read the CSV data from the uploaded file
                csv_data = file.read().decode('utf-8')
                df = pd.read_csv(io.StringIO(csv_data))

                # Make predictions using your model
                predictions = modelC.predict(df)  # Assumes df contains the input features for predictions
                log.info("Prediction for uploadC-batch classification successfull with value")
                # You can store the predictions or do further processing here

                # Render a page displaying the predictions
                zipped_data = list(zip(df.values.tolist(), predictions))
                return render_template('predictionsC.html', zipped_data=zipped_data, predictions=predictions)
        return render_template('uploadC_csv.html')
    except Exception as e:
        log.exception(" Something went wrong on Batch Classification prediction upload  initiation process") 

@app.route('/predictionsC', methods=['GET'])
def displayC_predictions():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("Classification Batch prediction output initialization successfull")

        # Fetch data from MongoDB
        data = list(collection.find({}))
        
        # Make predictions using the model
        predictions = [modelC.predict([d['features']])[0] for d in data]
        log.info("Prediction for predictionsC-batch classification successfull with value")
        return render_template('predictionsC.html', data = data, predictions=predictions)
    except Exception as e:
        log.exception(" Something went wrong on Classification Batch prediction upload  initiation process") 


if __name__ == "__main__":
    app.run(debug = True)

