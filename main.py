from fastapi import FastAPI

from api import users, sections, courses

app = FastAPI(
    title="Fast API crash course",
    description="Fast API with SQLAlchemy",
    version="0.0.1",
    contact={
        "name": "Paulo",
        "email": "paulopma@hotmail.com",
    },
    license_info={
        "name": "NASA"
    }
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)