import json
from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.schemas.competition import CompetitionOut

router = APIRouter()

DATA_FILE = Path(__file__).parent.parent.parent.parent / "data" / "competitions.json"


def load_competitions():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 转换日期字符串为 datetime 对象
    for item in data:
        if item.get("deadline"):
            item["deadline"] = datetime.fromisoformat(item["deadline"])
    
    return data


@router.get("/competitions", response_model=list[CompetitionOut])
def read_competitions():
    competitions = load_competitions()
    now = datetime.utcnow()
    result = []
    
    # 按截止时间排序（None 放最后）
    competitions.sort(key=lambda x: (x["deadline"] is None, x["deadline"] or datetime.max))
    
    for comp in competitions:
        is_expired = comp["deadline"] is not None and comp["deadline"] < now
        result.append(
            CompetitionOut(
                id=comp["id"],
                name=comp["name"],
                deadline=comp.get("deadline"),
                field=comp.get("field"),
                difficulty=comp.get("difficulty"),
                level=comp.get("level"),
                description=comp.get("description"),
                suggestions=comp.get("suggestions"),
                links=comp.get("links"),
                is_expired=is_expired,
            )
        )
    return result


@router.get("/competitions/{competition_id}", response_model=CompetitionOut)
def read_competition(competition_id: int):
    competitions = load_competitions()
    comp = next((c for c in competitions if c["id"] == competition_id), None)
    
    if not comp:
        raise HTTPException(status_code=404, detail="Competition not found")
    
    is_expired = comp["deadline"] is not None and comp["deadline"] < datetime.utcnow()
    return CompetitionOut(
        id=comp["id"],
        name=comp["name"],
        deadline=comp.get("deadline"),
        field=comp.get("field"),
        difficulty=comp.get("difficulty"),
        level=comp.get("level"),
        description=comp.get("description"),
        suggestions=comp.get("suggestions"),
        links=comp.get("links"),
        is_expired=is_expired,
    )
