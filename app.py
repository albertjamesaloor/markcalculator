# Import the Streamlit library
import streamlit as st

# Define a list of subjects
subjects = ["Physics", "Maths", "Chemisrty", "Biology", "Computer Science","English"]

# Create a radio button for each subject
selected_subject = st.radio("Select your preferred subject:", subjects)

# Display the selected subject back to the user
st.write("The subject you selected is:", selected_subject)

# Define the main function
def main():

  # Create a form to enter marks
  marks = st.form("enter_marks")
  pt1_input = marks.number_input("Enter PT1 mark:", min_value=0, max_value=40, value=0)
  hf_input = marks.number_input("Enter HF mark:", min_value=0, max_value=80, value=0)
  pt2_input = marks.number_input("Enter PT2 mark:", min_value=0, max_value=40, value=0)

  # Add a submit button to the form
  submitted = marks.form_submit_button("Submit")

  # Display the entered marks if the form is submitted
  total_marks=0
  if submitted:
    total_marks = pt1_input*0.2 + hf_input*0.3 + pt2_input*0.2
    st.write(f"You entered:")
    st.write(f"PT1: {pt1_input}")
    st.write(f"HF: {hf_input}")
    st.write(f"PT2: {pt2_input}")
    if selected_subject in ["English","Maths","Hindi"]:
        if round(total_marks)>=27:
            st.write("You have already passed!")
        else:
            marks_to_score=(27-total_marks)*2
            st.write("You need to score ",round(marks_to_score),"marks in Session Ending Exam")
    else:
        if round(total_marks)>=23:
            st.write("You have already passed!")
        else:
            marks_to_score=(23-total_marks)*2
            st.write("You need to score ",round(marks_to_score),"marks in Session Ending Exam")

# Call the main function
if __name__ == "__main__":
  main()
