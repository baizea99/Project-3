import streamlit as st
from transformers import pipeline

st.title(' Team Project Analyser')
st.write('Testing the idea of using huggingface. Not sure how though')
st.write(
    'Kudo to @antoine, @Kalvin, @angel, @aniel, and @josephine')

form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')