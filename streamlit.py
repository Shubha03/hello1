import streamlit as st  

# Set the title of the app  
st.set_page_config(page_title="My Streamlit App")  

# Add a title  
st.title("Welcome to My Streamlit App!")  

# Add a subheader  
st.subheader("This is a simple Streamlit app.")  

# Add some text  
st.write("This app demonstrates some basic Streamlit features.")  

# Add a slider  
value = st.slider("Select a value", 0, 100, 50)  
st.write(f"The selected value is: {value}")  

# Add a checkbox  
agree = st.checkbox("I agree to the terms and conditions")  
if agree:  
    st.write("You agreed to the terms and conditions.")  

# Add a button  
if st.button("Click me!"):  
    st.write("You clicked the button!")  

# Add a file uploader  
uploaded_file = st.file_uploader("Choose a file")  
if uploaded_file is not None:  
    st.write(f"You uploaded: {uploaded_file.name}")  

# Add a sidebar  
with st.sidebar:  
    st.header("Sidebar")  
    st.write("This is the sidebar.")  
    st.button("Sidebar Button")
