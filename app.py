import streamlit as st
from pipeline import generate_entries, search_entries

# UI
st.set_page_config(page_title="Project 001")
st.title("MVP4")

# generate entries
raw_note = st.text_input("Paste bio notes here")

if st.button("Generate"):
    entries_result = generate_entries(raw_note) 

# Search entries
query_input = st.text_input("Search entries") 
search_result = search_entries(query_input)
st.write(f"Found {len(search_result)} results") # f: insert varible into strings 

for entry in search_result: # Output result list
    with st.container():
        st.subheader(entry["name"])
        if entry.get("definition"):
            st.write(entry["definition"])
        st.write(entry["role"])
        st.write(entry["context"])
        st.divider()
