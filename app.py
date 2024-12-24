# Import the Streamlit library
import streamlit as st


name = st.text_input("Enter your first name:", placeholder="Type here...")

# Define the main function
def main():
    while name != "":
        if name.capitalize() not in ["Adithyan", "Alan", "Aravind", "Alex", "Bhavya", "Raza", "Nivedita"]:
            st.write(name,", you don't need to go.")
        else:
            st.write(name,", attend biology class.")

  

# Call the main function
if __name__ == "__main__":
  main()

#st.write("Note: percentage weightage used is PT1 - 10%, HF - 30%, PT2 - 10%, SEE - 50%")
