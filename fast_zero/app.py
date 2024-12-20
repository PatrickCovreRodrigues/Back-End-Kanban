import sys

from fastapi import FastAPI

print(sys.path)

from fastapi.middleware.cors import CORSMiddleware
from fast_zero.routers import activity, customers, project, todos

app = FastAPI()

app.include_router(todos.router)
app.include_router(customers.router)
app.include_router(activity.router)
app.include_router(project.router)

from fastapi import FastAPI
from .routers import todos, activity, project

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router, prefix="/todos", tags=["todos"])
app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(activity.router, prefix="/activitys", tags=["activitys"])
app.include_router(project.router, prefix="/projects", tags=["projects"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
