from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal
from auth import hash_password, verify_password, create_token
from notes import router as notes_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes_router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}


@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user:
        return {"error": "User not found"}

    if not verify_password(user.password, db_user.password):
        return {"error": "Wrong password"}

    token = create_token({"user_id": db_user.id})

    return {"access_token": token}