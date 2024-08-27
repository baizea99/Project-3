______________
<h1 style="text-align: center;">CINEMATIC AI</h1>

![DALL·E 2024-08-22 20 10 20 - A sleek, modern product image showcasing an AI model named 'Cinematic AI ' The design features a dark background with a cinematic feel, incorporating](https://github.com/user-attachments/assets/e32063c4-542d-4062-bc64-e59aa71d8943)
___________

## Project Team Members:
* Angel Alcantara
* Aniel Rios
* Antoine Baize
* Jeff Destine
* Josephine Robideau 
* Kalvin Anglin

## Table of Contents
* [Abstract](#Abstract)
* [Data](#Data)
* [Methods](#Methods)
* [Limitations](#Limitations)
* [Conclusions](#Conclusions)
* [References](#References)


## Abstract
Our movie recommendation system harnesses the power of sentiment analysis to deliver a personalized cinematic experience. By deeply analyzing movie reviews, we uncover the underlying emotional patterns that drive viewer preferences and behaviors. This also allows us to understand what recommendations truly resonate with each user based off the input they give us on the search bar. Mapping these sentiments to film attributes allows users to match their current insights and explore new genres as our engine provides a seamless gateway to your next cinematic adventures. Our in-depth analysis empowers you to make well-informed viewing decisions in the future.

**Project Overview:**
* Business solution applies to the Entertainment Industry

* Text needed for Sentiment Analysis derived from the following data sources:
    * Movie Reviews

 **Types of Sentiment Analysis**
* Fine-Grained Sentiment Analysis: Polarity (positive +, negative -, neutral) and intensity of sentiment
* Aspect Based Sentiment Analysis: Specific aspects of a product or service
* Emotion Detection: Emotion categories such as happy, sad, angry, etc.

## Goals
- Provide an application that enhances the moviegoer's experience
- Expand and broaden their horizons for different iterations of genre    

## Data Collection & Interpretation
* Data fetching, Google Research, Kaggle, Yelp, Data World, TMDB, NYT,
* EDA. Imported CSV files, created dataframes, and utilized pandas and Python functions to search, select, and handle missing data. Identified key features for further analysis
* Emotional algorithm applied to classify sentences based on the 6 emotions (Joy, Sadness, Anger, Fear, Love, Surprise)

## Cleanup
* Data sanitized by removing whitespace and splitting sentences based on the delimiter, such as periods or commas, to accurately parse and analyze the text

## Exploration Process
### Recreate System
To achieve your objective,
> - User is prompted to select a movie
> - System locates movie reviews based on selection and analyzes the reviews based on sentiment
> - Emotion Detection Algorithm classifies the description of the movie based on emotion
> - Recommendations are provided based on the movie selection, providing users with a cinematic body of work to explore

### Tools Used
- ChatGPT / DALL-E 3 (This model is designed for natural language understanding and generation of text and images)
- GitHub (A platform primarily used for version control and collaboration on software development projects)
- Gamma (Generative AI Presentation Software)
- Artssy (Generative AI Art Software)
- Pandas (Used for manipulation of all arrays and matrices)
- Numpy (Used for scientific computing and provides support for arrays, mathematics, etc.)
- Matplotlib (Enables the creation of static, animated, and interactive visualizations and plots for data analysis and presentation)
- Sci-kit learn (Used for Machine Learning)
- Tensorflow (TensorFlow is an open-source machine learning framework)
- Transformers (Transformers are a type of deep learning model architecture primarily used in natural language processing (NLP) tasks)
- TF BERT Model (Pre-trained deep learning model designed by Google to understand the context of words)

## Issues Encountered/How They Were Mitigated
### Emotion Detection Model:
> - Did not yield accurate results when using a sentiment analysis forward method using VADER, switched to NLP
> - Low accuracy score using LSTM model. The model was switched to incorporate a pre-trained BERT model with a custom layer
> - Training time is at 20 min/epoch; through further experimentation with batch size, this was limited to 15 min/epoch
### Movie Recommendation:
> - Received memory error when training a KNN model with a large dataset; now uses custom function and cosine similarity scores to yield faster results
> - All small datasets to train the models were outdated by over 25 years; we had to use a larger dataset that was outdated by 15 years due to hardware limitations
### Miscellaneous:
> - Conflict when trying to merge two applications into one user-interface

## Data
We reviewed datasets that provided the most opportunity for a thorough exploration of our key questions:

* [Kaggle Emotions Dataset](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp?resource=download)
---

## Project Management
|  Phases | Details|
* Software Version Control. Repository created on GitHub. GitHub Projects are used to create and track tasks based on key questions; the Git branch is used to upload files from the local computer to a remote repository. Utilized "compare & pull requests" to compare branch changes before merging into the main branch correlation, comparison, summary statistics, sentiment analysis, and time series analysis
* Model Selection & Fine-Tuning. Utilized dictionaries, lists, loops, column slicing, string manipulation, and train-test split to prevent data leakage. Ensured high-quality structured data is visualized and fed into the models for text classification

---
## Methods 

**Machine Learning Classification Models**
* Logistic Regression
* Random Forest
* Support Vector Machine

**Deep Learning Classification Models**

* VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis tool specifically designed for social media text. It uses a combination of sentiment lexicon and grammatical rules to analyze the sentiment of text data. VADER is known for its simplicity and effectiveness in analyzing sentiment in short texts like tweets, reviews, and comments. It provides a sentiment score ranging from -1 (negative) to 1 (positive) for each text input, along with scores for neutrality and compound sentiment. VADER is widely used for social media monitoring, customer feedback analysis, and sentiment analysis tasks where context and tone are important.

* BERT (Bidirectional Encoder Representations from Transformers) is a transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google. BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of NLP tasks. BERT has been widely adopted in academia and industry for various NLP tasks such as sentiment analysis, question answering, and named entity recognition.

* LSTM (Long Short-Term Memory) is a type of recurrent neural network (RNN) architecture that is well-suited for sequence prediction problems. LSTM networks are capable of learning long-term dependencies in sequential data and are widely used in natural language processing (NLP) tasks such as sentiment analysis, speech recognition, and machine translation. LSTM networks have a unique architecture that includes memory cells, input gates, output gates, and forget gates to control the flow of information through the network. This allows LSTM networks to capture long-range dependencies and model complex sequential patterns in the data.

**Developing Techniques**:
* One-shot learning (Model is trained to recognize new classes or categories from only a single example)
* Zero-shot learning (Model is trained to recognize and classify objects or concepts it has never seen before by leveraging knowledge from related tasks)

## Platforms
* [StreamLit](!https://streamlit.io/) 

* [Docker](https://hub.docker.com/r/jupyter/datascience-notebook/)

---
## Results
* Metric scores from SVM for Sentiment Analysis:

![Screenshot 2024-08-26 at 8 02 24 PM](https://github.com/user-attachments/assets/3448bfb6-81c6-4b2a-8c82-ec578aff94a9)

___
## Future Considerations
> - Having a clear and concise project structure overview from the start
> - Establishing deadline protocols that give ample time for troubleshooting software
> - Ensuring every recipient has roles and responsibilities established
> - Tracking deadline executions via communication
> - Being cognizant of the age of data

## Conclusion
Sentiment Analysis allows users to classify movie reviews based on positive or negative emotions. 

## References
[A Review on Text-Based Emotion Detection - Techniques, Applications, Datasets, and Future Directions](https://arxiv.org/pdf/2205.03235)

[Cinematic-AI (1).pdf](https://github.com/user-attachments/files/16755947/Cinematic-AI.1.pdf)

