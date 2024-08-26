import streamlit as st
import pickle
import pandas as pd

# load model
model = pickle.load(open('Project3-sentiment-analysis.pkl', 'rb'))

# create title
st.title('Sentiment Analysis Model')

review = st.text_input('Enter your review:')

submit = st.button('Predict')

if submit:
    prediction = model.predict([review])

    # print(prediction)
    # st.write(prediction)

    if prediction[0] == 'positive':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')
