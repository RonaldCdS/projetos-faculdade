from pydantic import BaseModel
from typing import Optional


class Livro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    genero: str
    disponivel: bool = True 