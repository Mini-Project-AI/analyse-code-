# Project Name
Clean up project
## Description

This project involves scanning project directories to find and manage image and icon imports. It provides a web interface using Streamlit to configure search patterns and output formats, and it supports saving results in various formats including text, JSON, XML, and Excel.

## Packages

### Streamlit
A powerful and easy-to-use framework for creating interactive web applications in Python. It is used in this project to provide a user-friendly interface for configuring search patterns and output formats.

### Pandas

A highly regarded library for data manipulation and analysis. In this project, it is utilized to handle data operations and export results to Excel files. It provides efficient data structures and functions to manage and analyze large datasets.

### Ppenpyxl

A library for reading and writing Excel files in the .xlsx format. It serves as the engine for saving DataFrames to Excel files in this project. openpyxl supports advanced Excel features and is essential for handling Excel file operations.

### xmltodict
A utility for converting XML data into Python dictionaries. This library makes it easier to work with XML data by converting it into a more manageable dictionary format. Note that this dependency is optional and used if you plan to handle XML output formats.

## Installation

To set up the project, create a virtual environment and install the necessary dependencies using `requirements.txt`:

```sh
pip install -r requirements.txt
```

This `README.md` provides a thorough overview of each dependency and its role in the project, making it clear for anyone setting up or maintaining the project.