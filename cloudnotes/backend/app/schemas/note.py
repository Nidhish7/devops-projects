from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    content: str
    
class NoteRead(BaseModel):
    id: UUID
    title: str
    content: str
    created_at: datetime