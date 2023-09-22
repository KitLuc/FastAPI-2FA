from fastapi import APIRouter


# Instance of APIRouter
movie = APIRouter(
    tags = ["movie"],
    prefix = "/movie",
    responses = {404: {"description": "Not found"}}
)


@movie.get("/{id}")
def get_movie(id: int) -> dict:
    return {"id": id, "name": "John Doe"}


@movie.post("/")
def create_movie(name: str) -> dict:
    return {"name": name}


@movie.put("/{id}")
def update_movie(id: int, name: str) -> dict:
    return {"id": id, "name": name}


@movie.delete("/{id}")
def delete_movie(id: int) -> dict:
    return {"id": id}