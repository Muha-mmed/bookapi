def DecodeBlog(doc) -> dict:
    return {
        "id": str(doc["_id"]),
        "title": doc["title"],
        "content": doc["content"],
        "author": doc["author"],
        "tag": doc["tag"],
        "date": doc["date"]
    }
    
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]