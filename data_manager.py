import json
import os

file_path = "data.json"

# Parse and save to JSON file
def save_data(data):
    try:
        data = json.loads(data)
        print("JSON parse success")

        # Save
        # replace old notes
        with open(file_path, "w", encoding="utf-8") as f: 
            json.dump(data, f, indent=2)

        print("data.json saved successfully")

    except json.JSONDecodeError:
        print("JSON parse FAILED")

# load JSON
def load_data(): 
    if not os.path.exists(file_path):
        # st.error ("JSON file not found")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
# Data searching # AND search
def search_data(entries, query):
    results = []
    score = 0
    
    if not query: # if user input nothing, then show all of the entries
        return entries
    
    keywords = query.lower().split()

    for entry in entries:
        name = entry["name"].lower()
        role = entry["role"].lower()
        definition = entry["definition"].lower()
        context = entry["context"].lower()

        # Ranking
        for keyword in keywords:
            if keyword in name:
                score += 10           
            if keyword in role:
                score += 6
            if keyword in definition:
                score += 4                    
            if keyword in context:
                score += 2

        if all(
            keyword in name or 
            keyword in role or 
            keyword in definition or 
            keyword in context
            for keyword in keywords
        ):
            results.append((score, entry))

    results.sort(key=lambda x: x[0])

    return [entry for score, entry in results]

# Edit
def update_entry(index, updated_entry): 
    entries = load_data() # Load JSON
    if 0 <= index < len(entries):
        entries[index] = updated_entry  
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)
        return True
    return False

# Delete
def delete_entry(index):
    entries = load_data()
    if 0 <= index < len(entries):
        entries.pop(index)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)
        return True
    return False