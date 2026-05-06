import streamlit as st
import pymupdf

st.title("PDF Text Extractor")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file is not None:

    # Open PDF
    doc = pymupdf.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    full_text = ""

    # Read all pages
    for i in doc:
        full_text += i.get_text()

    st.subheader("Extracted Text")

    st.text_area(
        "PDF Content",
        full_text,
        height=400
    )
