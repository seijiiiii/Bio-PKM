import streamlit as st
from pipeline import generate_entries, search_entries
from utils import highlight

# UI
st.set_page_config(page_title="Project 001")
st.title("MVP4")

# generate entries
raw_note = st.text_input("Paste bio notes here")

if st.button("Generate"):
    api_key = st.secrets["API_KEY"]
    # print (api_key)
    entries_result = generate_entries(raw_note, api_key) 

st.divider()

# Search entries
query_input = st.text_input("Search entries") 
search_result = search_entries(query_input)
st.write(f"Found {len(search_result)} results")

for entry in search_result: # Output result list + highlight words
    with st.container():
        st.markdown(
            f"<h3>{highlight(entry['name'], query_input)}</h3>",
            unsafe_allow_html=True
        )
        if entry.get("definition"): # not every entries have definition
            st.markdown(highlight(entry["definition"], query_input), unsafe_allow_html=True)
        st.markdown(highlight(entry["role"], query_input), unsafe_allow_html=True)
        st.markdown(highlight(entry["context"], query_input), unsafe_allow_html=True)
        
        st.divider()
  
