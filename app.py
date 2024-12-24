# Import the Streamlit library
import streamlit as st
# Define a list of subjects
"""subjects = ["Physics", "Maths", "Chemistry", "Biology", "Hindi", "Computer Science","English"]

# Create a dropdown menu for each subject
selected_subject = st.selectbox('Select a subject', subjects)
# Display the selected subject back to the user
st.write("The subject you selected is:", selected_subject)

# Create a slider
percentage = st.slider('Percentage:', 33, 100)

st.write(f'You selected: {percentage}%')"""

name = st.text_input("Enter your first name:", placeholder="Type here...")

# Define the main function
def main():
    if name not in ["Adithyan", "Alan", "Aravind", "Alex", "Bhavya", "Raza", "Nivedita"]:
        st.write(name,", you don't need to go.")
    else:
        st.write(name,", attend biology class.")

  

# Call the main function
if __name__ == "__main__":
  main()

#st.write("Note: percentage weightage used is PT1 - 10%, HF - 30%, PT2 - 10%, SEE - 50%")
