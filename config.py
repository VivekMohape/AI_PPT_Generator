import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TEMPLATE_PATH = "templates/Poster_Slide_Generated.pptx"
    OUTPUT_PATH = "output/final_generated.pptx"
    MODEL = "gpt-4o"
