import argparse
from fastapi import FastAPI

# Imports routes
from routes.user import user
from routes.movie import movie

description = """
                # Examen supplémentaire
                # 
                # ## Description
                # Esté proyecto es un examen suplementario para el curso de Herramientas de Programacion III**.
                # 
                # ## Author
                # -   **Name**: Anderson
                # -   **LastName**: Gomez Tobon
                # ## Date: 2023-10-09
              """


# Agrupación de argumentos del script
parser = argparse.ArgumentParser(description='')
parser.add_argument('-doc', action='store_true', help='Habilita la documentación Swagger')
parser.add_argument('-redoc', action='store_true', help='Habilita la documentación ReDoc')
args = parser.parse_args()


docs_url:str = '/app/doc' if args.doc else None
redoc_url:str = '/app/redoc' if args.redoc else None


app = FastAPI(
    title = "Examen suplemantario",
    description = description,
    version = "0.0.1",
    docs_url = docs_url,
    redoc_url = redoc_url,
    openapi_url = "/app/v1/"
)


@app.get("/")
def root() -> dict:
    if docs_url != None or redoc_url != None:
        return {"message": "Hello World!", "documentation": docs_url, "redoc": redoc_url}


# Include route files
app.include_router(user)
app.include_router(movie)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5050, reload=True)