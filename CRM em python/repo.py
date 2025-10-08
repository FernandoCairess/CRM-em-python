#repo se cmporta como backend
from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok= True)
DB_PATH = DATA_DIR / "leads.json"

def _load():
    if not DB_PATH.exists():
        return []

    try:
        return  json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def _save(leads):
    DB_PATH.write_text(
    json.dumps(leads, ensure_ascii=False, indent=2),
    encoding="utf-8"
    )

def create_lead(lead_dict):
    leads_loaded = _load() #primeira vez ele fica vazio[]
    leads_loaded.append(lead_dict)
    _save(leads_loaded)
