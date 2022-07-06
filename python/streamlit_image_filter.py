# Demo: https://youtube.com/shorts/q5QGgFschPs

import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title of an image filter app
st.title('Image Filter')

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    
    # Convert to numpy array
    image_np = np.array(image)

    # Show list of filters in radio button
    st.title('Select a filter')
    filter_name = st.radio('', ['None', 'Grayscale', 'Sepia', 'Invert', 'Blur', 'Gaussian Blur', 'Edge Detection', 'Pixelate'])

    # Show image with selected filter
    if filter_name == 'None':
        st.image(image_np, use_column_width=True)
    elif filter_name == 'Grayscale':
        st.image(cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY), use_column_width=True)
    elif filter_name == 'Sepia':
        st.image(cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV), use_column_width=True)
    elif filter_name == 'Invert':
        st.image(cv2.bitwise_not(image_np), use_column_width=True)
    elif filter_name == 'Blur':
        st.image(cv2.blur(image_np, (5, 5)), use_column_width=True)
    elif filter_name == 'Gaussian Blur':
        st.image(cv2.GaussianBlur(image_np, (5, 5), 0), use_column_width=True)
    elif filter_name == 'Edge Detection':
        st.image(cv2.Canny(image_np, 100, 200), use_column_width=True)
    elif filter_name == 'Pixelate':
        st.image(cv2.resize(image_np, (int(image_np.shape[1]/2), int(image_np.shape[0]/2))), use_column_width=True)
        