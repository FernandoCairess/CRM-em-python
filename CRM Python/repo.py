#repo se cmporta como backend
from pathlib import Path
import json,csv


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

def read_leads():
    return _load()

def export_csv():
    path_csv= DATA_DIR/ "leads.csv"
    leads = _load()


    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "company", "email","stage","created"])
            writer.writeheader()
            for lead in leads:
                writer.writerow(lead)
        return path_csv
    except PermissionError:
        return None