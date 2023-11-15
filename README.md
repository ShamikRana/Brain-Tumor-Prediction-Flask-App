# Brain-Tumor-Prediction-Flask-App
A Flask web application focused on detecting various types of brain tumors using Head MRI Scan images. The underlying model was built with a Convolutional Neural Network using the Xception architecture.

## Introduction
This project aims to provide a interface for predicting brain tumors based on MRI scan images. The deep learning model, trained on a Kaggle dataset, demonstrates an accuracy of 88.69% on the test data.

## Methods Used
- Data Visualization
- Data Preprocessing
- Deep Learning (CNN)
- Model Deployent using Flask

## Tools and Technologies Used
- Python
- Numpy, Pandas, Matplotlib, OpenCV
- Scikit Learn, Tensorflow, Keras
- Flask, HTML

## Model Training Description
- Data fetched from [Kaggle Dataset](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
- Images converted into arrays using OpenCV and numpy
- Dataset divided into 90:10 train-test ratio
- Normalized data and applied data augmentation
- Imported Xception model architecture and freeze its layers
- Utilized the Xception model architecture, fine-tuning with additional dense layers
- Model saved in H5 format for use in the Flask app

  ![Dataset Sample Images](https://raw.githubusercontent.com/ShamikRana/Brain-Tumor-Prediction-Flask-App/master/images/download.png)

## Convolutional Neural Network Characteristics
- Image Input Shape: (150,150,3)
- Xception architecture layers
- Dense layers: 512 (ReLU), 256 (ReLU), 4 (Softmax)
- Optimizer: 'SGD', Loss: 'categorical_crossentropy'
- Metrics: ['accuracy'], Epochs: 50
- Last Epoch Validation Accuracy: 88.69%

![Accuracy and Loss Graph](https://raw.githubusercontent.com/ShamikRana/Brain-Tumor-Prediction-Flask-App/master/images/accuracy%20and%20loss.png)

## Findings
- The model achieved an accuracy of 88.69% on the test data
- Confusion matrix provides insights into classification performance
![Confusion Matrix](https://raw.githubusercontent.com/ShamikRana/Brain-Tumor-Prediction-Flask-App/master/images/confution%20matrix.png)

## Web Application Creation Description
- Created a Python file "prediction.py" for the prediction function
- Imported the prediction function into the Flask file "app.py"
- HTML pages in ./templates: "home.html" and "predict.html"
- Uploaded files will be saved in ./static/images for prediction
- Predicted class and confidence will be displayed on the predict.html page
### home.html
![Home Page](https://raw.githubusercontent.com/ShamikRana/Brain-Tumor-Prediction-Flask-App/master/images/home.png)
### predict.html
![Prediction Page](https://raw.githubusercontent.com/ShamikRana/Brain-Tumor-Prediction-Flask-App/master/images/predict.png)

## How to Use
- Fork this repository to have your own copy.
- Clone your copy on your local system.
- Install necessary packages into your virtual environment using the command "pip install -r requirements.txt."
