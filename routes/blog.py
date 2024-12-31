from fastapi import APIRouter,HTTPException
from model.blog import BlogModel
from config.config import blogCollection
import datetime
from core.blog import DecodeBlog,DecodeBlogs
from bson import ObjectId

blog_root = APIRouter()

@blog_root.post("/new/blog")
async def postBlog(blog:BlogModel):
    doc = blog.model_dump()
    current_date= datetime.date.today()
    doc['date'] = str(current_date)
    res = await blogCollection.insert_one(doc)
    doc_id = str(res.inserted_id)
    return {
        "id":doc_id,
        "message": "Blog Post Successfully created" 
        }
    
@blog_root.get("/blogs")
async def getBlog():
    res = blogCollection.find()
    docs = await res.to_list(length=None)  # Convert cursor to list
    decoded_data = DecodeBlogs(docs)
    return decoded_data
    

@blog_root.get("/blog/{_id}")
async def oneBlog(_id:str):
    if not ObjectId.is_valid(_id):
        raise HTTPException(status_code=400, detail="Invalid Blog ID")
    
    res = await blogCollection.find_one({"_id": ObjectId(_id)})
    if not res:
        raise HTTPException(status_code=404, detail="Blog not found")
    decoded_data = DecodeBlog(res)
    return{
        "data": decoded_data,
    }




@blog_root.patch("/blog/update/{_id}", response_model=BlogModel)
async def updateBlog(_id: str, newBlog: BlogModel):
    # Validate the ID
    if not ObjectId.is_valid(_id):
        raise HTTPException(status_code=400, detail="Invalid Blog ID")

    # Convert the BlogModel instance to a dictionary
    update_data = newBlog.model_dump(exclude_unset=True)  # Exclude fields that are not updated

    # Find and update the blog
    res = await blogCollection.find_one_and_update(
        {"_id": ObjectId(_id)},  # Query filter
        {"$set": update_data},   # Update operation
        return_document=True     # Return the updated document
    )

    if not res:
        raise HTTPException(status_code=404, detail="Blog not found")

    return res

@blog_root.delete("/delete/{_id}")
def deleteBlog(_id:str):
    blogCollection.find_one_and_delete(
        {"_id":ObjectId(_id)}
    )
    return {"message": "blog deleted successfully"}