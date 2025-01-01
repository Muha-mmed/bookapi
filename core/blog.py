def DecodeBlog(doc) -> dict:
    return {
        "id": str(doc["_id"]),
        "title": doc["title"],
        "chapters": doc["chapters"],
        "author": doc["author"],
        "tag": doc["tag"],
        "date": doc["date"]
    }
    
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]