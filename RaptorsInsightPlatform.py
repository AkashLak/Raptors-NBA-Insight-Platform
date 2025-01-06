#Importing streamlit library to create interactive web app
import streamlit as st
import joblib
import numpy as np

#Loading previously created model from joblib file and storing in model variable
model = joblib.load('raptorspredictor.joblib')

#Creating title for webpage and then a description
st.title('🏀 Raptors Insight Platform: Predict the Team\'s Future Performance!')

st.write("Welcome to the Raptors Insight Platform! 📊 This platform will allow you to predict how the Raptors will perform in any upcoming season based on key metrics like wins and losses. Enter the data and see how the algorithm forecasts the team's future success. 🚀")

#User can choose to enter total number of wins in season, and the default value is set to 0, while the adjusting size can increase/decrease by 1
feature_1 = st.number_input('Enter the total number of wins in the season (e.g., 40)', value=0.0, step=1.0)
feature_2 = st.number_input('Enter the total number of losses in the season (e.g., 30)', value=0.0, step=1.0)

#Converts input values into numpy array, where its reshaped to have 1 row and numerous columns (feature based). This allows for a 2D format
input_data = np.array([feature_1, feature_2]).reshape(1, -1)

#Button called predict where if user clicks then if statemnet executes
if st.button('Predict Season Outcome'):
    #Creates loading message that informs users prediction process is ongoing
    with st.spinner('Analyzing the data and making a prediction...'):
        #Model uses input data to make prediction based on trained model, and stores the prediction as a result
        prediction = model.predict(input_data)
    
    #markdown displays bold headings showing the predicted ranking, and then brief description, rounded to nearest integer
    st.markdown(f"### 🏆 **Predicted Ranking for the Raptors This Season**")
    st.markdown(f"**Prediction**: 🎯 Rank: **{round(prediction[0])}** in the Regular Season")
    #Provides detailed messages about prediction and informs based on historical data/model
    st.write(f"Based on the data you provided (Wins: **{feature_1}**, Losses: **{feature_2}**), the model predicts that the Raptors will finish with a ranking of **{prediction[0]:.0f}** this season. 🏅")
    
    st.write("This prediction takes into account historical team performance and statistical models to forecast the season's outcome. Let's hope the Raptors soar high! 🚀")