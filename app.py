# app.py

import streamlit as st
from views.import_finder_view import import_finder_exporter_view
from views.statistics_view import statistics_view

def main():
    st.sidebar.title("Navigation")
    view = st.sidebar.radio("Go to", ["Import Finder and Exporter", "Statistics"])

    if view == "Import Finder and Exporter":
        import_finder_exporter_view()
    elif view == "Statistics":
        statistics_view()

if __name__ == "__main__":
    main()
