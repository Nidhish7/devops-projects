from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from uuid import UUID

from app.schemas.note import NoteCreate, NoteRead
from app.models.note import Note


async def create_note(db: AsyncSession, note: NoteCreate) -> Note:
    new_note = Note(
        title=note.title,
        content=note.content,
    )
    
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note

async def list_notes(db: AsyncSession):
    result = await db.execute(select(Note))
    return result.scalars().all()

async def delete_note(db: AsyncSession, note_id: UUID):
    await db.execute(delete(Note).where(Note.id == note_id))
    await db.commit()
    