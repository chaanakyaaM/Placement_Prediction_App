# 🎓 Placement Prediction App

An interactive **Streamlit web app** that predicts whether a student is likely to be **placed** based on academic, technical, and skill-based factors.  
The app uses a pre-trained **machine learning model (`model.pkl`)** to generate predictions and probabilities.

---
## 🚀 Features

- 📥 **Model Loading**: Automatically loads a trained ML model (`model.pkl`)  
- 📝 **User-Friendly Form**: Enter academic and skill details easily  
- 🔮 **Placement Prediction**: Displays prediction (**Placed / Not Placed**) with probability  
- 📊 **Input Summary**: Shows all entered values for transparency  
- 📈 **Interactive UI**: Progress bar & success/error messages make results engaging  

---
## ⚙️ Tech Stack

- [Streamlit](https://streamlit.io/) → Web app framework  
- [NumPy](https://numpy.org/) → Numerical computations  
- [Pickle](https://docs.python.org/3/library/pickle.html) → Model serialization   


---
## 🖥️ How It Works

1. User enters details like **IQ, CGPA, GPA, Projects, Communication skills, etc.**  
2. Inputs are converted into a structured NumPy array  
3. Pre-trained ML model (`model.pkl`) is loaded  
4. The app predicts placement outcome and probability  
5. Results are displayed with a progress bar and formatted messages  

---
## 🛠️ Installation & Setup

1. Clone this repository:
```bash
   git clone https://github.com/chaanakyaaM/Placement_Prediction_App
   cd placement_prediction_app
   uv init
```
This creates a virtual environment

2. Install dependencies:

```
uv pip install -r requirements.txt
```

3. Activate the virtual environment

```
.venv/scripts/activate
```

4. Run the app:

```
streamlit run app.py
```
---
## ✨ Credits
Created with ❤️ by [chaanakyaa M](https://github.com/chaanakyaaM)
