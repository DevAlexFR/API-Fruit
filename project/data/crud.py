from typing import List
from pydantic import BaseModel, Field

class Fruit(BaseModel):
    """
    Modelo de dados para frutas, contendo apenas um campo de nome.
    """
    name: str = Field(
        example="Maçã",
        description="O nome da fruta"
    )

database: List[Fruit] = []

def create_fruit(fruit: Fruit) -> Fruit:
    """
    Cria uma nova fruta e a adiciona à base de dados.
    """
    database.append(fruit) # Cria
    return fruit

def get_fruits() -> List[Fruit]:
    """
    Retorna todas as frutas presentes na base de dados.
    """
    return database # Le

def update_fruit(fruit_id: int, updated_fruit: Fruit) -> Fruit:
    """
    Atualiza os dados de uma fruta existente.
    """
    if 0 <= fruit_id < len(database):
        database[fruit_id] = updated_fruit # Atualiza
        return updated_fruit
    return None

def delete_fruit(fruit_id: int) -> dict:
    """
    Deleta uma fruta da base de dados.
    """
    if 0 <= fruit_id < len(database):
        deleted_fruit = database.pop(fruit_id) # Deleta
        return {"message": f"Fruta {deleted_fruit.name} deletada"}
    return {"error": "Fruta não encontrada"}
