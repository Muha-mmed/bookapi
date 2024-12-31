from typing import List
from pydantic import BaseModel

class Chapter(BaseModel):
    heading: str
    content: str
    

class BlogModel(BaseModel):
    title: str
    chapters: List[Chapter]
    author: str
    tag: list