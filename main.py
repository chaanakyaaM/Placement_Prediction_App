import pickle
import streamlit as st
import numpy as np

@st.cache_resource
def load_model(path='model.pkl'):
    try:
        with open(path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def predict_placement(model, data):
    prediction = model.predict(data)
    probability = model.predict_proba(data)
    return prediction[0], probability[0]

st.set_page_config(page_title="Placement Prediction App", layout="centered")
st.title("🎓 Placement Prediction App")

st.write("""This app predicts whether a student is likely to be **placed** based on several academic and skill-based factors.""")
st.write("Please enter the required details below to get the prediction.")

with st.form("placement_form"):
    st.subheader("📋 Student Information")

    col1, col2 = st.columns(2)
    with col1:
        IQ = st.number_input('IQ', min_value=0, max_value=200, value=100)
        Prev_Sem_Result = st.number_input('Previous Semester Result (GPA)', min_value=0.0, max_value=10.0, value=5.0)
        Extra_Curricular_Score = st.number_input('Extra-Curricular Score (0-10)', min_value=0, max_value=10, value=5)
        Internship_Experience = st.radio('Internship Experience', ['No', 'Yes'])

    with col2:
        CGPA = st.number_input('CGPA', min_value=0.0, max_value=10.0, value=6.0)
        Academic_Performance = st.number_input('Academic Performance (0-10)', min_value=0, max_value=10, value=5)
        Communication_Skills = st.number_input('Communication Skills (0-10)', min_value=0, max_value=10, value=5)
        Projects_Completed = st.number_input('Projects Completed', min_value=0, max_value=10, value=3)

    submit = st.form_submit_button("🔍 Predict Placement")

if submit:
    # Encode radio input
    Internship_Experience_encoded = 1 if Internship_Experience == 'Yes' else 0

    # Create input array
    input_data = np.array([[IQ, Prev_Sem_Result, CGPA, Academic_Performance,
                            Internship_Experience_encoded, Extra_Curricular_Score,
                            Communication_Skills, Projects_Completed]])

    # Load model and predict
    model = load_model()
    if model:
        prediction, probability = predict_placement(model, input_data)

        if prediction == 1:
            st.progress(min(int(probability[1]*100), 100))
            st.success(f"✅ Prediction: **Placed**")
            st.write(f"There is a **{probability[1]*100:.2f}%** chance of being placed.")
        else:
            st.progress(min(int(probability[0]*100), 100))
            st.error(f"❌ Prediction: **Not Placed**")
            st.write(f"There is only a **{probability[0]*100:.2f}%** chance of being placed.")

        # input summary
    st.write("### 📊 Input Summary")
    st.write({
        "IQ": IQ,
        "Previous Semester Result": Prev_Sem_Result,
        "CGPA": CGPA,
        "Academic Performance": Academic_Performance,
        "Internship Experience": Internship_Experience,
        "Extra-Curricular Score": Extra_Curricular_Score,
        "Communication Skills": Communication_Skills,
        "Projects Completed": Projects_Completed
    })
