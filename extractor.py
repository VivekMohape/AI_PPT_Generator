import openai
import instructor
from config import Config
from schemas import PosterExtraction

client = instructor.from_openai(openai.OpenAI(api_key=Config.OPENAI_API_KEY))

system_prompt = """
You are an expert medical poster extractor.

Your task is to parse scientific posters and extract section-wise content, even if the poster doesn't explicitly label sections.

Always attempt to extract at minimum the following sections:
- Objective
- Methods
- Results
- Conclusion

If headings are missing, you MUST intelligently infer likely boundaries based on paragraph structure, typical poster format, or scientific conventions.

Also extract any additional sections you find (e.g. Background, Safety, Takeaways, Funding, Limitations).

Output strictly in this JSON format:

{
  "sections": [
    { "heading": "<section name>", "content": "<section content>" }
  ]
}

You MUST always include Objective, Methods, Results, and Conclusion (even if inferred, or empty if truly unavailable).
"""

def extract_sections(raw_text: str) -> PosterExtraction:
    response = client.chat.completions.create(
        model=Config.MODEL,
        response_model=PosterExtraction,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": raw_text}
        ],
        temperature=0.1
    )
    return response
