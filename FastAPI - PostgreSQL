from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor      #gives column names and value
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

#Validation of body in postman
class Schema(BaseModel):
    title: str
    content: str
    published: bool = True          #default True

while True:
    try:
        connection = psycopg2.connect(host=os.getenv("HOST"),database=os.getenv("DATABASE"),
                                user=os.getenv("USER"),password=os.getenv("PASSWORD"), cursor_factory=RealDictCursor)
        cursor = connection.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print(f"Database connection failed. Error: {error}")


posts_list = [{"title":"pokemon","content":"then we fight","id":1}]


@app.get("/")
def home():
    return {"Hello":"World"}

@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)    #HTTPException for created
def create_post(post:Schema):               #post - the body being sent in postman that matches Schema class
    cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING *",
                   (post.title, post.content, post.published))  #values inserted into %s in order
    new_post = cursor.fetchone()
    connection.commit()
    return {"post": new_post}            #being returned to the postman Body

# def create_post(payload: dict = Body(...)):                 #Body - extracts all field from postman body and convert it to dict and stores in variable name payload

@app.get("/posts/{id}")                     #{id} - path parameter
def get_post(id:int):
    cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cursor.fetchall()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,          #handles both Response and status method
                            detail=f"post with id: {id} was not found")

        # response:Response - response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id: {id} was not found"}
    return {"data": post}

@app.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    connection.commit()
    return {"message": "post successfully deleted"}

@app.put("/posts/{id}")
def update_post(id:int, post:Schema):

        cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
                    (post.title, post.content, post.published, id))
        new_post = cursor.fetchone()
        connection.commit()
        if new_post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        return {"data":new_post}


    # for index, current_post in enumerate(posts_list):
    #     if current_post["id"] == id:
    #         posts_list[index] = post.dict()         # replace the old post with the post from the postman body
    #         return {"data": posts_list[index]}
