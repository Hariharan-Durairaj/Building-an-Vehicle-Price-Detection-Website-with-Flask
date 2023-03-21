import pickle
import requests
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
# model1 = pickle.load(open("MODEL.pkl",'rb'))

@app.route("/",methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/Predict", methods=['POST'])
def Predict():
    abtest  = int(request.form['abtest'])
    vehicleType = int(request.form['vehicleType'])
    yearOfRegistration  = int(request.form['yearOfRegistration'])
    gearbox = int(request.form['gearbox'])
    powerPS  = int(request.form['powerPS'])
    model  = int(request.form['model'])
    kilometer  = int(request.form['kilometer'])
    monthOfRegistration = int(request.form['monthOfRegistration'])
    fuelType    = int(request.form['fuelType'])
    brand  = int(request.form['brand'])
    notRepairedDamage   = int(request.form['notRepairedDamage'])
    postalCode  = int(request.form['postalCode'])
    pre = [[abtest, vehicleType, yearOfRegistration, gearbox, powerPS, model, kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage ,postalCode]]
    #prediction = model1.predict(pre)

    fields=[["abtest", "vehicleType", "yearOfRegistration", "gearbox", "powerPS", "model", "monthOfRegistration", "fuelType", "brand", "notRepairedDamage" ,"postalCode"]]
    values=[[abtest, vehicleType, yearOfRegistration, gearbox, powerPS, model,kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage ,postalCode]]
    
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = [Enter api key]
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field":[["abtest", "vehicleType", "yearOfRegistration", "gearbox", "powerPS", "model","kilometer", "monthOfRegistration", "fuelType", "brand", "notRepairedDamage" ,"postalCode"]], "values":[[2,2,2,2,2,2,2,2,2,2,2,2]]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b80cbc74-c8c2-48eb-bd8f-9b6e63cdc26e/predictions?version=2022-11-19', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions=response_scoring.json()
    print(predictions)
    return render_template('predict.html', data=predictions['predictions'][0]['values'][0][0])


if __name__=="__main__":
    app.run(debug=True)
