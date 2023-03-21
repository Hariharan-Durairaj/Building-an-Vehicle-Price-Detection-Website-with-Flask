# Building an Vehicle Price Detection Website with Flask

## Introduction
In today's world, purchasing a vehicle has become a significant investment for many people. 
It is always a good idea to compare prices and features of various vehicles before making a purchase. 
However, it can be challenging to manually search for and compare prices of different vehicles. 
To simplify this process, we can develop a Vehicle Price Detection Website using Flask, a popular Python web framework.

IBM Cloud is a powerful platform that can be used to train and deploy machine learning models. 
By leveraging this platform, we can train a model to detect the prices of different vehicles based on their features. 
After the model is trained, we can deploy it in the IBM Cloud and expose it through an API. 
This API can then be used to access the model and get price predictions for different vehicles.

Using Flask, we build a web application that allows users to enter the features of a vehicle, such as make, model, year, mileage, and condition. 
The web application can then call the API hosted on IBM Cloud, passing the vehicle features as inputs, and retrieve the predicted price. 
The predicted price can then be displayed on the web application for the user to view.


## Dataset

The dataset was taken from kraggle. The csv file contains features like 

## Requirements
Python 3.x
Keras 2.7
Tensorflow 2.x
Watson Machine Learning Client
IBM Watson Machine Learning API Key
IBM Cloud Object Storage credentials
Flash

## Installation
To run the project, you can clone the repository to your local machine using the following command:


Copy code
```
https://github.com/Hariharan-Durairaj/Building-an-Vehicle-Price-Detection-Website-with-Flask.git
```

Then, install the required dependencies using the following command:

Copy code
```
pip install -r requirements.txt
```

Replace the api in app.py with a new IBM cloud api and deploy the model in IBM cloud

## Usage

app.py: Run the code to launch the website
To run the run.py use the below code in terminal
```
python -m flask run
```

To install flask, run the below code
```
python -m pip install flask
```

