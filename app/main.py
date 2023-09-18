from fastapi import FastAPI, APIRouter, status

app = FastAPI()

router = APIRouter()

@router.get('/')
def get_notes():
    return "Retorna uma lista de itens de nota"

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note():
    return "Cria um item de nota"

@router.patch('/{noteId}')
def update_note(noteId: str):
    return f"Atualiza um item de nota com o ID {noteId}"

@router.get('/{noteId}')
def get_note(noteId: str):
    return f"Obtém um item de nota com o ID {noteId}"

@router.delete('/{noteId}')
def delete_note(noteId: str):
    return f"Deleta um item de nota com o ID {noteId}"

app.include_router(router, tags=['Notes'], prefix='/api/notes')

@app.get("/api/healthchecker")
def root():
    return {"message": "Bem-vindo ao FastAPI com SQLAlchemy"}
