# Data Explorer  

A simple data exploration project built with **Streamlit**.  
This app lets you upload a **CSV** or **JSON** file, preview the dataset, and view basic information.  

## Project Structure 
<img width="274" height="395" alt="image" src="https://github.com/user-attachments/assets/7ca6d3f8-1c0b-43b1-9fbd-87c9ed553796" />

## Features  
- Upload **CSV** or **JSON** files  
- Preview the **first 10 rows**   
- View dataset information:  
  - Shape (rows × columns)  
  - Column names  
  - Data types  
  - Missing values count  
- Sidebar with project details  
- Extra features:  
  - Custom CSS styling  
  - Logo support (`assets/logo.png`)  
  - Interactive widgets (checkboxes, multiselect, slider)  
  - Download processed CSV  


## Setup Instructions  

1. **Create and activate virtual environment** 
     python -m venv venv
     .\venv\Scripts\activate

2. **Install dependencies**  
     pip install -r requirements.txt
   
3. **Run the Streamlit app**
    streamlit run streamlit_app.py
   
4. **Open browser**
    http://localhost:8501


