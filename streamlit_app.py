import streamlit as st
import os
from pdf_reader import extract_text_from_pdf
from extractor import extract_sections
from pptx import Presentation
from mapper import map_to_slide_content
from ppt_generator import generate_final_ppt_with_analysis
from config import Config

os.makedirs("templates", exist_ok=True)
os.makedirs("output", exist_ok=True)

st.title("AI-powered Poster to PPT Generator")

uploaded_pdf = st.file_uploader("Upload Poster PDF", type=["pdf"])
uploaded_template = st.file_uploader("Upload PPT Template", type=["pptx"])

if uploaded_pdf and uploaded_template:
    pdf_path = "uploaded_poster.pdf"
    template_path = "templates/Poster_Slide_Generated.pptx"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())
    with open(template_path, "wb") as f:
        f.write(uploaded_template.getbuffer())

    st.success("Files uploaded successfully!")

    poster_text = extract_text_from_pdf(pdf_path)
    extracted_sections = extract_sections(poster_text)
    template = Presentation(template_path)
    slide_content = map_to_slide_content(extracted_sections, template)

    generate_final_ppt_with_analysis(slide_content)

    with open(Config.OUTPUT_PATH, "rb") as f:
        st.download_button("Download Generated PPT", f, file_name="final_generated.pptx")
