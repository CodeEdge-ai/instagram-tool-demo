import json

def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_markdown(content, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
