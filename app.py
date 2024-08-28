import streamlit as st
import json
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os
import glob
#python imaging library, to display PNG files
from PIL import Image

#initialize session state variables
def initialize():
    if 'num_fields' not in st.session_state:
        st.session_state.num_fields = 1
    if 'symbols' not in st.session_state:
        st.session_state.symbols = ['']

# Delete files from previous run
def pre_cleanup():
    # clean up existing image files
    files = glob.glob('/images/*')
    for f in files:
        os.remove(f)
    # clean up existing data files
    files = glob.glob('/data/*')
    for f in files:
        os.remove(f)
    # clean up symbols and pickle filenames files:
    if os.path.isfile("symbols.json"):
        os.remove("symbols.json")
    if os.path.isfile("pk_filenames.json"):
        os.remove("pk_filenames.json")

#function to allow entry of another stock symbol    
def add_symbol():
    st.session_state.num_fields +=1
    st.session_state.symbols.append('')

#function to handle submission of form
def handle_form_submission():
    #get symbols from session state
    entered_symbols = [symbol for symbol in st.session_state.symbols if symbol]
    #store the symbols in a file, to pass to jupyter notebooks
    with open('symbols.json','w') as f:
        json.dump(entered_symbols,f)
    #invoke the controller notebook
    with st.spinner(text="Please wait - gathering and processing data"):
        execute_notebook('controller.ipynb')
    display_results()

#function to invoke a jupyter notebook    
def execute_notebook(notebook_name):
    #load notebook
    with open(notebook_name) as f:
        notebook = nbformat.read(f,as_version=4)
    # create execute proprocessor instance
    ep = ExecutePreprocessor(time=600,kernal_name='python3')
    # execute notebook
    ep.preprocess(notebook,{'metadata':{'path':'./'}})

# Upon completion of form submission processing, display resulting images
def display_results():
    # Define the path to images folder
    folder_path = 'images'

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out only PNG files
    png_files = [file for file in files if file.lower().endswith('.png')]

    st.subheader("Results")
    # Display each PNG file
    for file_name in png_files:
        # Construct full file path
        file_path = os.path.join(folder_path, file_name)
        # Diplay image on form
        image = Image.open(file_path)
        st.image(image, use_column_width=True)
    

# Main processing
initialize()
pre_cleanup()

# create form    
with st.form(key='portfolio_form'):
     st.subheader("Portfolio Optimizer 2.0")
     st.write("Enter desired stock symbols (at least 2, up to 10):")
     col1, col2, col3, col4 = st.columns(4)
     for i in range(st.session_state.num_fields):
         with col1:
            st.session_state.symbols[i] = st.text_input(f'Stock Symbol {i+1}',value=st.session_state.symbols[i], key=f'symbol_{i}').upper()
            # make symbols upper case
            # st.session_state.symbols[i] = current_value.upper()
     add_button = st.form_submit_button('Add Symbol')
     submit_button  = st.form_submit_button('Optimize!')
     
     #if user indicated they wanted to add another stock symbol:
     if add_button:
        add_symbol()
        st.rerun()  # Rerun the script to reflect the changes

     #if user is done entering symbols, and now wants to optimize the portfolio
     if submit_button:
        handle_form_submission()



    