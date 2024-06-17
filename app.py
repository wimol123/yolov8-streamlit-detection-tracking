# Python In-built packages
from pathlib import Path
import PIL
import streamlit as st
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Object Detection using YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Object Detection And Tracking using YOLOv8")

model_path = Path(settings.DETECTION_MODEL)
model = helper.load_model(model_path)

