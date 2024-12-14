import uvicorn
from fastapi import FastAPI
from typing import List
# from data.crud import *
from project.data.crud import *

app = FastAPI(
    title="Apple Fruit 🍎",
    description="Esta API permite criar, ler, atualizar e deletar frutas.",
    version="1.0.0"
)

from fastapi.responses import HTMLResponse

@app.get("/", summary="Rota principal", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Fruit🍎</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #FFEEB3, #FFC0CB);
                color: #333;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                background-color: #FFFFFF;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                padding: 40px;
                max-width: 600px;
                width: 90%;
                text-align: center;
            }
            .title {
                font-size: 2.5em;
                color: #FF6347;
                margin-bottom: 20px;
            }
            .description {
                font-size: 1.2em;
                color: #666;
                margin-bottom: 20px;
            }
            a {
                color: #007BFF;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="title">Bem-vindo à API de Frutas 🍎</h1>
            <p class="description">Esta API permite criar, listar, atualizar e deletar frutas.</p>
            <p class="description">Consulte a documentação <a href="/docs">docs da API</a> ou <a href="/redoc">redoc da API</a> para mais informações.</p>
        </div>
    </body>
    </html>

    """

@app.post("/fruit/", response_model=Fruit, summary="Cria uma fruta", response_description="A fruta criada.")
def create_fruit_endpoint(fruit: Fruit):
    return create_fruit(fruit)

@app.get("/fruits/", response_model=List[Fruit], summary="Obtém todas as frutas", response_description="Lista de todas as frutas.")
def get_fruits_endpoint():
    return get_fruits()

@app.put("/fruits/{fruit_id}", response_model=Fruit, summary="Atualiza uma fruta", response_description="A fruta atualizada.")
def update_fruit_endpoint(fruit_id: int, updated_fruit: Fruit):
    result = update_fruit(fruit_id, updated_fruit)
    if result:
        return result
    return {"error": "Fruta não encontrada"}

@app.delete("/fruits/{fruit_id}", summary="Deleta uma fruta", response_description="Mensagem de sucesso ou erro.")
def delete_fruit_endpoint(fruit_id: int):
    return delete_fruit(fruit_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
