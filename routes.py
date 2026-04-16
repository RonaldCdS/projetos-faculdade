from fastapi import APIRouter, HTTPException
from database import livros_collection
from schemas import Livro
from bson import ObjectId

router = APIRouter()

@router.post("/livros")
def criar_livro(livro: Livro):
    novo_livro = livro.model_dump() 
    resultado = livros_collection.insert_one(novo_livro)
    return {"id": str(resultado.inserted_id), "status": "Criado"}


@router.get("/livros")
def listar_livros():
    livros = []
    for doc in livros_collection.find():
        doc["_id"] = str(doc["_id"]) 
        livros.append(doc)
    return livros


@router.put("/livros/{id_livro}")
def atualizar_livro(id_livro: str, livro_atualizado: Livro):
    resultado = livros_collection.update_one(
        {"_id": ObjectId(id_livro)}, 
        {"$set": livro_atualizado.model_dump()}
    )
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="livro no encontrado")
    return {"status": "Atualizado!"}


@router.delete("/livros/{id_livro}")
def deletar_livro(id_livro: str):
    resultado = livros_collection.delete_one({"_id": ObjectId(id_livro)})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="livro n encontrado")
    return {"status": "Apagado!"}