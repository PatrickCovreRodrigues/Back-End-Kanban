import sys

from fastapi import FastAPI

print(sys.path)

from fast_zero.routers import activity, customers, project, todos

app = FastAPI()

app.include_router(todos.router)
app.include_router(customers.router)
app.include_router(activity.router)
app.include_router(project.router)
