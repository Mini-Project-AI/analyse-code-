import streamlit as st
import os
import re
import plotly.graph_objs as go
from utils.extract_zip import extract_zip

# Define patterns for different types of imports
PATTERNS = {
    'svg': re.compile(r'import\s+(\w+)\s+from\s+\'([^\']+\.svg)\''),
    'image': re.compile(r'import\s+(\w+)\s+from\s+\'([^\']+\.png|jpg|jpeg)\''),
    'icon': re.compile(r'import\s+(\w+)\s+from\s+\'@mui/icons-material/(\w+)\'')
}

def statistics_view():
    st.title('Statistics View')

    # Upload file input
    uploaded_file = st.file_uploader("Upload a ZIP file containing the project", type="zip")

    # User input for pattern type
    pattern_type = st.selectbox('Select import pattern type:', list(PATTERNS.keys()))

    if uploaded_file is not None:
        try:
            # Extract the uploaded zip file
            project_dir = extract_zip(uploaded_file)

            if not os.path.isdir(project_dir):
                st.error("The extracted project directory does not exist.")
                return

            pattern = PATTERNS.get(pattern_type)
            if not pattern:
                st.error("Invalid pattern type selected.")
                return

            icon_imports = {}
            icon_usage = {}

            # Walk through the project directory and find icon imports and usage
            for root, dirs, files in os.walk(project_dir):
                for file in files:
                    if file.endswith('.ts') or file.endswith('.tsx'):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                imports = pattern.findall(content)
                                usages = re.findall(r'<(\w+)\s', content)
                                
                                for match in imports:
                                    if pattern_type == 'svg':
                                        _, icon = match
                                    else:
                                        icon = os.path.basename(match[1])

                                    if icon in icon_imports:
                                        icon_imports[icon] += 1
                                    else:
                                        icon_imports[icon] = 1

                                for icon in usages:
                                    if icon in icon_usage:
                                        icon_usage[icon] += 1
                                    else:
                                        icon_usage[icon] = 1
                        except Exception as e:
                            st.error(f"Error reading file {file_path}: {e}")

            total_occurrences = sum(icon_imports.values())
            if total_occurrences == 0:
                st.error("No occurrences found.")
                return

            # Prepare data for pie charts
            types_repeated_more_than_1 = {k: v for k, v in icon_imports.items() if v > 1}
            types_repeated_more_than_2 = {k: v for k, v in icon_imports.items() if v > 2}

            pie_data = {
                'Repeated More Than 1 Time': types_repeated_more_than_1,
                'Repeated More Than 2 Times': types_repeated_more_than_2
            }

            with st.expander('Statistics by Occurrences'):
                for title, data in pie_data.items():
                    if data:
                        labels = list(data.keys())
                        values = [count for count in data.values()]
                        percentages = [value / total_occurrences * 100 for value in values]

                        pie_fig = go.Figure(data=[go.Pie(labels=labels, values=values, 
                                                         textinfo='label+percent', 
                                                         hole=0.3)])
                        pie_fig.update_layout(title=f'{title} - Global Percentage')

                        st.write(f"Global percentage for {title}:")
                        st.plotly_chart(pie_fig)

            # Display the statistics
            st.subheader(f'{pattern_type} Import Statistics')
            with st.expander('File Import Statistics'):
                st.write(f"Total distinct {pattern_type} imported: {len(icon_imports)}")
                st.write(icon_imports)

            with st.expander('File Includes'):
                for file, imports in icon_imports.items():
                    st.write(f"{file}: {imports} occurrences")

            # Prepare data for bar chart
            bar_labels = list(icon_imports.keys())
            bar_values = list(icon_imports.values())

            if bar_labels:
                bar_fig = go.Figure(data=[go.Bar(x=bar_labels, y=bar_values)])
                with st.expander('Import Bar Chart'):
                    st.plotly_chart(bar_fig)

        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")

    else:
        st.info("Please upload a ZIP file to analyze.")
