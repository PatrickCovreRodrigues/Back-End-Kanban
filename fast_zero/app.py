import sys

from fastapi import FastAPI

print(sys.path)

from fast_zero.routers import activity, customers, project, todos

app = FastAPI()

app.include_router(todos.router)
app.include_router(customers.router)
app.include_router(activity.router)
app.include_router(project.router)

from fastapi import FastAPI
from .routers import todos, activity, project

app = FastAPI()

app.include_router(todos.router, prefix="/todos", tags=["todos"])
app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(activity.router, prefix="/activitys", tags=["activitys"])
app.include_router(project.router, prefix="/projects", tags=["projects"])
