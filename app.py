import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

st.title('Final Project')

friends = st.number_input('friends', 0, 60000)
verified = st.selectbox('Verified', ['True', 'False'])
sentiment = st.number_input('Sentiment', -1.00,0.00, 1.00)
longitude = st.slider('longitude', -6.00, 6.00)
latitude = st.number_input('Latitude', 0.00, 60.00)
country = st.selectbox('Country', ['GB'])
platform = st.selectbox('Platform', ['twitter'])
status_count = st.number_input('Status Count', 0.00, 60000.00)
tweet = st.write('Most objects')

input_data_dict = {
    "friends": friends,
    "verified": verified,
    "sentiment": sentiment,
    "longitude": longitude,
    "latitude": latitude,
    "country": country,
    "platform": platform,
    "status_count": status_count,
    "tweet": tweet
}

st.write(input_data_dict)

inpute_data = pd.DataFrame([input_data_dict])

st.write(inpute_data)

save_path = "artefacts"

save_model_predictor = TabularPredictor.load(save_path)

submit = st.button("SHOW PREDICTION")

if submit:
    Ourdata = save_model_predictor.predict(inpute_data)
    st.write(f"The predicted sentiment is: {Ourdata}")
