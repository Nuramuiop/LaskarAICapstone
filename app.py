import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import os

st.set_page_config(
    page_title="Co-Clas: Coffee Bean Grading System",
    page_icon="☕",
    layout="centered"
)

@st.cache_resource
def load_classification_model():
    """Load the trained model once and cache it"""
    model_path = 'model_1.h5'
    if not os.path.exists(model_path):
        st.error(f"Model file '{model_path}' not found. Please make sure it's in the correct directory.")
        st.stop()
    return load_model(model_path)

def predict_image(img, model):
    """Process image and make prediction"""
    # Resize and preprocess image
    img = img.resize((256, 256))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    
    return predicted_class, predictions[0]

def main():
    st.title("Co-Clas: AI-Powered Coffee Bean Grading System")
    
    st.markdown("""
    ### Sistem Klasifikasi Kualitas Biji Kopi Berbasis AI
    
    Upload gambar biji kopi untuk mendeteksi kualitasnya secara otomatis.
    """)
    
    # Load model
    with st.spinner("Memuat model klasifikasi..."):
        model = load_classification_model()
    
    # Class labels
    class_labels = ['Dark', 'Green', 'Light', 'Medium']
    
    # Image upload
    uploaded_file = st.file_uploader("Upload gambar biji kopi", type=["jpg", "jpeg", "png"])
    
    col1, col2 = st.columns(2)
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        col1.image(image, caption="Gambar yang diunggah", use_column_width=True)
        
        # Make prediction on button click
        if st.button("Analisis Kualitas"):
            with st.spinner("Menganalisis gambar..."):
                predicted_class, confidence_scores = predict_image(image, model)
                predicted_label = class_labels[predicted_class]
                
                # Display results
                col2.success(f"Hasil Klasifikasi: **{predicted_label}**")
                col2.write("Tingkat Kepercayaan:")
                
                # Show confidence for each class
                for i, (label, score) in enumerate(zip(class_labels, confidence_scores)):
                    col2.progress(float(score))
                    col2.write(f"{label}: {score:.2%}")
                
                st.markdown("### Deskripsi Kualitas")
                
                descriptions = {
                    'Dark': "Biji kopi dengan tingkat kematangan tinggi. Biasanya memiliki rasa yang kuat dan sedikit pahit.",
                    'Green': "Biji kopi yang belum matang sempurna. Masih memiliki karakteristik hijau dan asam.",
                    'Light': "Biji kopi dengan tingkat sangrai ringan. Mempertahankan karakteristik asli dari biji kopi.",
                    'Medium': "Biji kopi dengan tingkat sangrai sedang. Keseimbangan antara rasa asam dan pahit."
                }
                
                st.write(descriptions[predicted_label])
    
    st.markdown("---")
    st.markdown("© 27 Mei 2025 Co-Clas")

if __name__ == "__main__":
    main()
