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
    with open(file_path, "r") as f:
        return json.load(f)
    
# Data searching
def search_data(entries, query):
    results = []
    
    if not query: # if user input nothing, then show all of the entries
        return entries
    else:
        for entry in entries:
            if (
                # Convert input and data into lower case, so comparable
                query.lower() in entry["name"].lower() or # prioritise
                query.lower() in entry["role"].lower()
            ):
                results.append(entry) # adding element to the end of the list
    return results