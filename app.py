'This Module is to run streamlit'
import streamlit as st
'This Package is to unpack model'
import pickle

# load model
model = pickle.load(open('project3-sentiment-analysis.pkl', 'rb'))

# create title
st.title('Sentiment Analysis Model')

review = st.text_input('Enter your text:')

submit = st.button('Predict')

if submit:
    prediction = model.predict([review])

    # print(prediction)
    # st.write(prediction)

    if prediction[0] == 'positive':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')