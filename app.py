# Python In-built packages
from pathlib import Path
import PIL
import streamlit as st
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="HAPPY RAINNY KANOMTHAI..",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

model_path = Path(settings.DETECTION_MODEL)
model = helper.load_model(model_path)

st.title("HAPPY RAINNY KANOMTHAI..")
image = st.file_uploader("Choose .jpg pic ...", type=["png", "jpg", "jpeg"])
if image:
    image = Image.open(image)
    st.image(image=image)

    st.write("")
    st.write("Detecting...")

    result = model(image)
    names = result[0].names
    probability = result[0].probs.data.numpy()
    prediction = np.argmax(probability)
    className = int(names[prediction])
    className = class_labels_names[className]
    st.write(className)
