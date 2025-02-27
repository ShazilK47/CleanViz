
# import streamlit as st
# import pandas as pd
# import os 
# import io 
# from io import BytesIO #Allow us to convert files into Binary

# # set up our App
# st.set_page_config(page_title="DataFlow", layout='wide') #set up page title: apears on the top
 
# st.title("CleanViz")
# st.write("Transform your files between CSV and Excel formats with build-in data claning and visualization!")

# uploaded_files = st.file_uploader("Upload your files(CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)  #to upload files

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()


#         if file_ext == ".csv":
#             df = pd.read_csv(file) #data frame 
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file) 
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue

#         # Display info about the file
#         st.write(f"**File Name:** {file.name}")
#         st.write(f"**File Size:** {file.size}/1024")

#         # Display first 5 rows of the dataframe
#         st.write("Preview the Head of the Dataframe")
#         st.dataframe(df.head())  #head => returns the first 5 rows of data

#         # Options for data cleaning
#         st.subheader("Data Cleaning Options")
#         if st.checkbox(f"Clean Data for {file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates from {file.name}"):
#                     df.drop_duplicates(inplace=True)
#                     st.write("Duplicates Removed!")

#             with col2:
#                 if st.button(f"Fill Missing Values for {file.name}"):
#                     numeric_cols = df.select_dtypes(include=['number']).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.write("Missing values have been Filed")



#         # Choose Specific Columns to keep or convert
#         st.subheader("Select Columns to Convert")
#         columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
#         df = df[columns]


#         #Create some Visualization
#         st.subheader("Data Visualization")
#         if st.checkbox(f"Show Visualization for {file.name}"):
#             st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

#         # Convert the File : CSV to Excel or vice versa
#         st.subheader("Conversion Options")
#         conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
#         if st.button(f"Convert {file.name}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".csv")
#                 mime_type = "text/csv"

#             elif conversion_type == "Excel":
#                 df.to_excel(buffer, index=False)
#                 file_name = file.name.replace(file_ext, "xlsx")
#                 mime_type = "applicaton/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             buffer.seek(0)

#             # Download Button
#             st.download_button(
#                 label=f"Download {file.name} as {conversion_type}",
#                 data=buffer,
#                 file_name = file_name,
#                 mime = mime_type
#             )
#             st.success("All files processed!")



import streamlit as st
import pandas as pd
import os 
import io 
from io import BytesIO  # Allow us to convert files into Binary

st.set_page_config(page_title="CleanViz", layout='wide', initial_sidebar_state="expanded")  


# App Title
st.title("🚀 CleanViz - Data Cleaner & Converter")
st.markdown("Transform your files between **CSV** and **Excel** formats with built-in **data cleaning** and **visualization**!")

# File Upload
st.markdown("### 📤 Upload Files")
uploaded_files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)  

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        with st.spinner(f"Processing {file.name}..."):
            if file_ext == ".csv":
                df = pd.read_csv(file) 
            elif file_ext == ".xlsx":
                df = pd.read_excel(file) 
            else:
                st.error(f"❌ Unsupported file type: {file_ext}")
                continue

        # Display file info
        st.write(f"📂 **File Name:** {file.name}")
        st.write(f"📏 **File Size:** {file.size / 1024:.2f} KB")

        # Preview data
        st.markdown("### 👀 Preview Data")
        st.dataframe(df.head())
        
        # Data Cleaning Options
        st.markdown("### 🛠 Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🧹 Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates Removed!")

            with col2:
                if st.button(f"📊 Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing values have been filled!")

        # Column Selection
        st.markdown("### 🎯 Select Columns to Keep")
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization
        st.markdown("### 📈 Data Visualization")
        if st.checkbox(f"📊 Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        # File Conversion
        st.markdown("### 🔄 File Conversion")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"🔄 Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇️ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )
            st.success("✅ File Ready for Download!")