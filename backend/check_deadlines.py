#!/usr/bin/env python3
"""
独立脚本：检查即将截止的竞赛
运行方式：python backend/scripts/check_deadlines.py
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

# 定位数据文件（相对于脚本位置向上两级到 backend 目录）
DATA_FILE = Path(__file__).parent.parent / "data" / "competitions.json"

def load_competitions():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    competitions = load_competitions()
    now = datetime.now()
    upcoming = []
    expired = []

    for comp in competitions:
        deadline_str = comp.get("deadline")
        if not deadline_str:
            continue
        deadline = datetime.fromisoformat(deadline_str.replace("Z", "+00:00"))
        days_left = (deadline - now).days

        if days_left < 0:
            expired.append((comp["name"], abs(days_left)))
        elif days_left <= 3:
            upcoming.append((comp["name"], deadline, days_left))

    print("\n===== 竞赛截止提醒 =====")
    if upcoming:
        print("\n⚠️ 即将截止（3天内）：")
        for name, deadline, days in upcoming:
            print(f"  • {name} - 剩余 {days} 天，截止于 {deadline.strftime('%Y-%m-%d %H:%M')}")
    else:
        print("\n✅ 暂无 3 天内截止的竞赛")

    if expired:
        print("\n📅 已过期竞赛：")
        for name, days_ago in expired[:5]:  # 最多显示5个
            print(f"  • {name} - 已过期 {days_ago} 天")
    print("=" * 30)

if __name__ == "__main__":
    main()
