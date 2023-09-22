from fastapi import APIRouter


# Instance of APIRouter
user = APIRouter(
    tags = ["user"],
    prefix = "/user",
    responses = {404: {"description": "Not found"}}
)


@user.get("/{id}")
def get_user(id: int) -> dict:
    return {"id": id, "name": "John Doe"}


@user.post("/")
def create_user(name: str) -> dict:
    return {"name": name}


@user.put("/{id}")
def update_user(id: int, name: str) -> dict:
    return {"id": id, "name": name}


@user.delete("/{id}")
def delete_user(id: int) -> dict:
    return {"id": id}