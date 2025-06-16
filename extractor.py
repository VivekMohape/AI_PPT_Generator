import openai
import instructor
import streamlit as st
from schemas import PosterSummary

# ✅ Load your key securely from secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
MODEL = "gpt-4o"

# ✅ Initialize client with Instructor
client = instructor.from_openai(openai.OpenAI(api_key=OPENAI_API_KEY))

def extract_hierarchical_summary(raw_text: str) -> PosterSummary:
    system_prompt = (
        "You are an expert scientific poster summarizer. Read the poster and output JSON:\n"
        "{'title': '...', 'sections': [{'heading': '...', 'bullets': ['...', '...']}]}\n"
        "- Section headings max 15 words.\n"
        "- Sub-bullets max 25 words each.\n"
        "- Extract 10-20 sub-bullets across sections.\n"
        "- Sections: Objective, Methods, Results, Conclusions, Limitations, Funding."
    )
    
    response = client.chat.completions.create(
        model=MODEL,
        response_model=PosterSummary,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": raw_text}
        ],
        temperature=0.1
    )
    
    return response
