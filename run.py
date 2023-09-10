import numpy as np
import keras
from PIL import Image
import streamlit as st

def preprocess_image(image):
    # Resize to 28x28 and convert to grayscale
    image = image.resize((28, 28))
    image = image.convert('L')  # Convert to grayscale
    image = np.array(image)  # Convert to NumPy array
    image = image / 255.0  # Normalize pixel values to [0, 1]
    return image

model1 = keras.models.load_model('fashion_mnist_cnn_model.h5')
model2 = keras.models.load_model('fashion_mnist_cnn_model2.h5')
model3 = keras.models.load_model('fashion_mnist_cnn_model3.h5')

st.set_page_config(page_title='Fashion Item Classifier', page_icon='👕', layout='centered', initial_sidebar_state='auto')

st.title('Fashion Item Classifier')
accuracy1 = 0.9105
accuracy2 = 0.9087
accuracy3 = 0.9001

st.subheader('Model 1')
st.write('Accuracy acheived on test dataset', accuracy1)
st.subheader('Model 2')
st.write('Accuracy acheived on test dataset', accuracy2)
st.subheader('Model 3')
st.write('Accuracy acheived on test dataset', accuracy3)
class_names = [
    "👕 - T-shirt/top",
    "👖 - Trouser",
    "👚 - Pullover",
    "👗 - Dress",
    "🧥 - Coat",
    "👡 - Sandal",
    "👔 - Shirt",
    "👟 - Sneaker",
    "👜 - Bag",
    "🥾 - Ankle boot"
]

st.sidebar.title('Current types of clothing the model can identify')
for i in class_names:
    st.sidebar.write(i)
    
# Upload image through Streamlit's file uploader
uploaded_image = st.file_uploader("Upload an image of clothing...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess the image to 28x28 grayscale
    processed_image = preprocess_image(image)

    # Make predictions 1
    prediction1 = model1.predict(np.expand_dims(processed_image, axis=0))
    prediction2 = model2.predict(np.expand_dims(processed_image, axis=0))
    prediction3 = model3.predict(np.expand_dims(processed_image, axis=0))

    # Display the prediction result
    
    st.write("Prediction by model 1: ", class_names[np.argmax(prediction1)])
    st.write("Prediction by model 2: ", class_names[np.argmax(prediction2)])
    st.write("Prediction by model 3: ", class_names[np.argmax(prediction3)])
    