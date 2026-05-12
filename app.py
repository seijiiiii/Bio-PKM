import streamlit as st
from pipeline import generate_entries, search_entries
from data_manager import load_data, update_entry, delete_entry
from utils import highlight

st.set_page_config(page_title="Project 001")
st.title("Interaction 2")

if "editing_index" not in st.session_state:
    st.session_state.editing_index = None

tab_generate, tab_search = st.tabs(["Generate", "Library"])

def render_entry(entry, query, real_index):
    st.markdown(
        f"<h3>{highlight(entry['name'], query)}</h3>",
        unsafe_allow_html=True
    )
    if entry.get("definition"):
        st.markdown(highlight(entry["definition"], query), unsafe_allow_html=True)
    st.markdown(highlight(entry.get("role", ""), query), unsafe_allow_html=True)
    st.markdown(highlight(entry.get("context", ""), query), unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col1:
        if st.button("Edit", key=f"edit_{real_index}"):
            st.session_state.editing_index = real_index
            st.rerun()
    with col2:
        if st.button("Delete", key=f"delete_{real_index}"):
            delete_entry(real_index)
            st.rerun()


def render_edit_form(entry, real_index): # Render after pressing Edit button
    new_name = st.text_input("Name", value=entry["name"], key=f"name_{real_index}")
    new_definition = st.text_area("Definition", value=entry.get("definition", ""), key=f"def_{real_index}", height=100)
    new_role = st.text_area("Role", value=entry.get("role", ""), key=f"role_{real_index}", height=120)
    new_context = st.text_area("Context", value=entry.get("context", ""), key=f"ctx_{real_index}", height=80)

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Save", key=f"save_{real_index}"):
            update_entry(real_index, {
                "name": new_name,
                "definition": new_definition,
                "role": new_role,
                "context": new_context,
            })
            st.session_state.editing_index = None
            st.rerun()
    with col2:
        if st.button("Cancel", key=f"cancel_{real_index}"):
            st.session_state.editing_index = None
            st.rerun()


with tab_generate: # generate entries
    raw_note = st.text_area("Paste your notes here", height=200)

    if st.button("Generate"):
        api_key = st.secrets["API_KEY"]
        entries_result = generate_entries(raw_note, api_key) 


with tab_search: # Search entries
    query_input = st.text_input("Search entries")
    search_result = search_entries(query_input)
    all_entries = load_data()
    st.write(f"Found {len(search_result)} results")

    for entry in search_result:
        real_index = next(
            (i for i, e in enumerate(all_entries) if e["name"] == entry["name"]),
            None
        )
        with st.container():
            if st.session_state.editing_index == real_index:
                render_edit_form(entry, real_index)
            else:
                render_entry(entry, query_input, real_index)
            st.divider()
