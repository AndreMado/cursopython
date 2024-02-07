import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def get_list():
    return [1,2,3,4,5]

@app.get("/andres", response_class = HTMLResponse)
def get_string():
    return """
    <h1> Hola mi nombre es andres y</h1>
    <p> ya me bañé</p>
    """


def run():
    store.get_categories()

if __name__=="__main__":
    run()