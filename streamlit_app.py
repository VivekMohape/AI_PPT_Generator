import streamlit as st
from extractor import extract_hierarchical_summary
from ppt_generator import generate_hierarchical_ppt
from pdf_reader import extract_text_from_pdf
from schemas import PosterSummary

st.title("AI Poster to PPT Generator 🚀")

uploaded_pdf = st.file_uploader("Upload your Poster PDF", type=["pdf"])
uploaded_template = st.file_uploader("Upload your PPT Template", type=["pptx"])
uploaded_image = st.file_uploader("Upload Image for Slide 1", type=["jpg", "jpeg", "png"])

if uploaded_pdf and uploaded_template and uploaded_image:
    with open("poster.pdf", "wb") as f:
        f.write(uploaded_pdf.getbuffer())
    with open("template.pptx", "wb") as f:
        f.write(uploaded_template.getbuffer())
    with open("image.jpg", "wb") as f:
        f.write(uploaded_image.getbuffer())

    st.write("📄 Extracting text...")
    raw_text = extract_text_from_pdf("poster.pdf")
    
    st.write(" Extracting hierarchical summary...")
    summary = extract_hierarchical_summary(raw_text)

    st.write(" Generating PPT...")
    generate_hierarchical_ppt(summary, "template.pptx", "generated.pptx", "image.jpg")

    with open("generated.pptx", "rb") as f:
        st.download_button("📥 Download Generated PPT", f, file_name="generated.pptx")
