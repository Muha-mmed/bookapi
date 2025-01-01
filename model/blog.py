from pydantic import BaseModel

class Chapter(BaseModel):
    heading: str
    content: str
    

class BlogModel(BaseModel):
    title: str
    chapters: list[Chapter]
    author: str
    tag: list