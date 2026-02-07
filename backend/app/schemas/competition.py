from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class LinkItem(BaseModel):
    name: str
    url: str


class CompetitionBase(BaseModel):
    name: str
    deadline: Optional[datetime] = None
    field: Optional[str] = None
    difficulty: Optional[str] = None
    level: Optional[str] = None
    description: Optional[str] = None
    suggestions: Optional[List[str]] = None
    links: Optional[List[LinkItem]] = None


class CompetitionOut(CompetitionBase):
    id: int
    is_expired: bool

    class Config:
        from_attributes = True
