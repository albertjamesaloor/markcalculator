# Import the Streamlit library
import streamlit as st
# Define a list of subjects
subjects = ["Physics", "Maths", "Chemistry", "Biology", "Hindi", "Computer Science","English"]
# Create a dropdown menu for each subject
selected_subject = st.selectbox('Select a subject', subjects)
# Display the selected subject back to the user
st.write("The subject you selected is:", selected_subject)
# Create a slider
percentage = st.slider('Percentage:', 33, 100)
st.write(f'You selected: {percentage}%')
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
  EMH=80*percentage/100
  OTH=70*percentage/100
  if submitted:
    total_marks = pt1_input*0.2 + hf_input*0.3 + pt2_input*0.2
    st.write(f"You entered:")
    st.write(f"PT1: {pt1_input}")
    st.write(f"HF: {hf_input}")
    st.write(f"PT2: {pt2_input}")
    if selected_subject in ["English","Maths","Hindi"]:
        st.write("You have currently secured", round(total_marks), "out of 80")
        if round(total_marks)>=EMH:
          if percentage==33:
            st.write("You have already passed!")
          else:
            st.write("You have crossed ", percentage, "%")
        else:
          marks_to_score=(EMH-total_marks)*2
          if marks_to_score<=80:
            if percentage==33:
              st.write("You need to score ",round(marks_to_score),"marks in Session Ending Exam to pass")
            else:
              st.write("You need to score ",round(marks_to_score),"marks in Session Ending Exam to cross",percentage, "%")
          else:
            st.write("Sorry... it is not possible, realise your past mistakes and don't let them repeat.\n Strive for a lesser score")
    else:
          st.write("You have currently secured", round(total_marks), "out of 70")
          if round(total_marks)>=OTH:
            if percentage==33:
              st.write("You have already passed!")
            else:
              st.write("You have crossed ", percentage, "%")
          else:
            marks_to_score=(OTH-total_marks)*2
            if marks_to_score<=70:
              if percentage==33:
                st.write("You need to score ",round(marks_to_score),"marks in Session Ending Exam to pass")
              else:
                st.write("You need to score ",round(marks_to_score),"marks in Session Ending Exam to cross",percentage, "%")
            else:
              st.write("Sorry... it is not possible, realise your past mistakes and don't let them repeat.\n Strive for a lesser score")
# Call the main function
if __name__ == "__main__":
  main()
st.write("Note: percentage weightage used is PT1 - 10%, HF - 30%, PT2 - 10%, SEE - 50%")
