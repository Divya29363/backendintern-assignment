from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/notes")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    new_note = models.Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()


@router.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    db.delete(note)
    db.commit()
    return {"message": "Deleted"}