from generate import generate_data
from data_manager import save_data, load_data, search_data

# raw note --> entries
def generate_entries(text_input, API_KEY):
    text_output = generate_data(text_input, API_KEY)
    save_data(text_output)
    entries = load_data()
    return entries

# query --> searching result
def search_entries(query):
    entries = load_data()
    return search_data(entries, query)
