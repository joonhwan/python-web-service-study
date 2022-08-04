from fastapi import APIRouter, Depends
from sqlmodel import Session
from jewel_app.db import get_session
from jewel_app.models.gem import Gem

router = APIRouter()

@router.get("/")
def get_gems(session: Session =  Depends(get_session)):
    gems = session.query(Gem).all()
    return gems

@router.get("/{gem_id}")
def get_gem(gem_id: int, session: Session = Depends(get_session)):
    gem = session.get(Gem, gem_id)
    return gem

