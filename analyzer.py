from schemas import AdjustmentRecommendation
from config import Config
import instructor
import openai

client = instructor.from_openai(openai.OpenAI(api_key=Config.OPENAI_API_KEY))

analyzer_prompt = """
You are a PPT design assistant. Given text content, placeholder dimensions, and character count, suggest if summarization or font shrinkage is required.

Output JSON as:
{
  "summarize": true/false,
  "shrink_font": true/false,
  "new_font_size": integer (null if shrink_font is false)
}
"""

def analyze_slide_content(text: str, box_width: float, box_height: float) -> AdjustmentRecommendation:
    response = client.chat.completions.create(
        model=Config.MODEL,
        response_model=AdjustmentRecommendation,
        messages=[
            {"role": "system", "content": analyzer_prompt},
            {"role": "user", "content": f"Content: {text}\nWidth: {box_width}\nHeight: {box_height}\nLength: {len(text)}"}
        ],
        temperature=0.0
    )
    return response
