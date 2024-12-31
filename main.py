from fastapi import FastAPI
from routes.blog import blog_root

app = FastAPI()

app.include_router(blog_root)