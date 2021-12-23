# Crypto return prediction

The goal of this project is to crete an efficient model that can predict the cryto currency return with a good accuracy (Evaluation metric - 85%)

Group members : Siddartha Marella (sm4940); Varun Jasti (vj2252)

Project overview:

The project uses the crypto data available at a kaggle competition : https://www.kaggle.com/c/g-research-crypto-forecasting 
The main apects of the project:

1. Evaluate the usefulness of other crypto currencies in predicting a crypto currency.
2. Twitter volumetric and sentiment analysis to evaluate its correlation to crypto price.
3. Model training on popular models like LSTM, linear and SGD regression.
4. H2O AutoML tool for model training for crypto prediction.
5. Portfolio Algorithm creation that helps in minimising the total risk.
6. Dash Web-app creation that gives an interactive platform to users. 

Code execution:

Crypto data is required to run this code, Please download the 'data' folder from: https://drive.google.com/drive/folders/1-bEo5SQv06pwumgXyzNJ4sbVypzuxbTd?usp=sharing (Accessible to all lion mail users)

These code is on colab which includes all the necessary installation commands.

The code visualization_app.ipynb can be run to access the interactive web app. The portfolio code is also persent in this file.

The code AutoML_2.ipynb has the requried code to run the H2O model setup for execution of Bitcoin and Ethereum prediction models.

The Code Linear and LSTM original,ipynb and SGD has the implementation of each of the models including the EDA done on the data.

sparkStreaming.py and twitterHTTPClient.py has the code for streaming the Twitter API.

processStreamedData.py has code for calling GCP BigQuery API to do the analysis needed from the spark streaming. 

Layout :

Project_report - contains all the report files including pics and tex files.
Code - All the required code.
