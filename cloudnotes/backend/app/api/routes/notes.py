from fastapi import APIRouter, Depends
from uuid import UUID
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.note import NoteCreate, NoteRead
from app.services.note_service import create_note, list_notes, delete_note
from app.db.session import get_db


router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model = NoteRead)
async def create(note: NoteCreate, db: AsyncSession = Depends(get_db)):
    return await create_note(db, note)

@router.get("", response_model=List[NoteRead])
async def get_all(db: AsyncSession = Depends(get_db)):
    return await list_notes(db)

@router.delete("/{note_id}")
async def delete(note_id: UUID, db: AsyncSession = Depends(get_db)):
    await delete_note(db, note_id)
    return {
        "status": "deleted"
    }