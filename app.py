import streamlit as st
from ultralytics import YOLOv10


def main():
    model_path = "model/best.pt"
    st.title("Safety Helmet Detection Based on YOLOv10")
    file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if file is not None:
        st.image(file, "Uploaded image")
        model = YOLOv10(model=model_path)
        result = model(file)[0]
        st.image(result, 'Processed image')


if __name__ == "__main__":
    main()
