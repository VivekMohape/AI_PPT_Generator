from pydantic import BaseModel
from typing import List, Optional

class Section(BaseModel):
    heading: str
    content: str

class PosterExtraction(BaseModel):
    sections: List[Section]

class SlideContent(BaseModel):
    slide_type: str
    title: str
    content: dict

class AdjustmentRecommendation(BaseModel):
    summarize: bool
    shrink_font: bool
    new_font_size: Optional[int]
