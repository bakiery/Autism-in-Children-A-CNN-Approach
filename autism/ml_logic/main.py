import base64
import requests
import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

# Step 1: Load the trained CNN model
cnn_model = load_model('path_to_trained_cnn_model.h5')

# Step 2: Define functions for performing facial assessment
def preprocess_image(image):
    # Preprocess the image (resize, normalize, etc.)
    # Add your preprocessing steps here
    processed_image = ...

    return processed_image

def perform_facial_assessment(image):
    # Preprocess the image
    processed_image = preprocess_image(image)

    # Perform facial assessment using the trained CNN model
    cnn_prediction = cnn_model.predict(processed_image)

    # Display the prediction result and probability
    st.subheader('Detection Result:')
    autistic_probability = cnn_prediction[0][0] * 100
    not_autistic_probability = 100 - autistic_probability

    st.success(f'Likelihood of being autistic: {autistic_probability:.2f}%')
    st.info(f'Likelihood of not being autistic: {not_autistic_probability:.2f}%')

    if autistic_probability > 50:
        st.info('Classification: Autistic')
    else:
        st.info('Classification: Not Autistic')


# Step 3: Create the Streamlit app
def main():
    st.set_page_config(
        page_title="Facial Assessment Tool",
        page_icon="🧩",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.title('Facial Assessment Tool')

    # Check if the 'styles.css' file exists
    if not os.path.isfile('styles.css'):
        st.warning("The 'styles.css' file is missing. Please make sure it exists in the same directory as this script.")
    else:
        # Add the custom CSS styles
        with open('styles.css') as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    # Display the introduction and instructions
    st.markdown('''
        ## Facial Assessment Tool
        Upload an image of a child to assess the likelihood of autism based on facial morphology.
        ''')

    # Upload image
    uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Read image file
        image = Image.open(uploaded_file)

        # Perform facial assessment using the trained model
        perform_facial_assessment(image)

    # Citation
    st.markdown('''
        This tool is based on research papers conducted by Naomi Scott, Alex Lee Jones, Robin Stewart Samuel Kramer, Robert Ward, Mohammad-Parsa Hosseini, Madison Beary, Alex Hadsell,
        Ryan Messersmith, Hamid Soltanian-Zadeh, K.K. Mujeeb Rahman and M. Monica Subashini. You can find the studies at the following links:

        - [Bangor University Study](https://ward-lab.bangor.ac.uk/pubs/Scott_Ward_14_AQ.pdf)
        - [Deep Learning for Autism Diagnosis and Facial Analysis in Children](https://www.frontiersin.org/articles/10.3389/fncom.2021.789998/full)
        - [Identification of Autism in Children Using Static Facial Features and Deep Neural Networks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8773918/)

        Please note that this tool is provided for informational purposes only and is not a diagnostic tool. It assesses the likelihood of autism based on facial morphology, but a formal diagnosis should be made by a qualified healthcare professional.
        ''')

# Step 4: Run the Streamlit app
if __name__ == '__main__':
    main()
