import json_repair

def normalize_json_str(text: str) -> str:
 
    return json_repair.loads(text)
