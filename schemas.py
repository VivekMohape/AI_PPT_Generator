from pydantic import BaseModel
from typing import List

class Section(BaseModel):
    heading: str
    bullets: List[str]

class PosterSummary(BaseModel):
    title: str
    sections: List[Section]
