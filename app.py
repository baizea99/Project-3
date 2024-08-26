import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model('model/emotion_detection.keras', custom_objects={'BertEmbeddingLayer': BertEmbeddingLayer})
st.title("My Streamlit App")
def encode_text(text, max_length=100):
    encoded_dict = tokenizer.encode_plus(
        text,
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=max_length,    # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True, # Construct attention masks.
        return_tensors='tf'      # Return tensorflow tensors.
    )
    return {'input_ids': encoded_dict['input_ids'], 'attention_mask': encoded_dict['attention_mask']}

# Example sentence
test_sentence = "The beautiful melody of this song made me dance"
encoded_test_sentence = encode_text(test_sentence)

def predict_emotion(encoded_text):
    probabilities = model.predict(encoded_text)
    # Assuming the model's output layer is softmax and you have a label encoder
    emotion = label_encoder.inverse_transform([probabilities.argmax()])[0]  # Get the most likely emotion
    return emotion

predicted_emotion = predict_emotion([encoded_test_sentence['input_ids'], encoded_test_sentence['attention_mask']])
print(f"The predicted emotion is: {predicted_emotion}")
