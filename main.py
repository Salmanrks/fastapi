from fastapi import FastAPI
from routes.route import todo_api_router

app = FastAPI()

app.include_router(todo_api_router)






    

