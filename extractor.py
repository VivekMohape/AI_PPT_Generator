import openai
import instructor
from config import Config
from schemas import PosterExtraction

client = instructor.from_openai(openai.OpenAI(api_key=Config.OPENAI_API_KEY))

system_prompt = """
You are an expert poster extractor.

Extract the following core sections always:
- Objective
- Methods
- Results
- Conclusion

Additionally, extract any extra sections found in the poster (like Background, Safety, Limitations, Funding, Takeaways, etc).

Output strictly in this JSON format:
{
  "sections": [
    { "heading": "<section name>", "content": "<section content>" }
  ]
}

The section list should always include Objective, Methods, Results, Conclusion, even if their content is empty.
"""

def extract_sections(raw_text: str) -> PosterExtraction:
    response = client.chat.completions.create(
        model=Config.MODEL,
        response_model=PosterExtraction,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": raw_text}
        ],
        temperature=0.3
    )
    return response
