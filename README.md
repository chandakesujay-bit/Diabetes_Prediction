# 🩺 Diabetes Prediction System

A Machine Learning-based web application that predicts whether a patient is likely to have diabetes based on medical parameters. The application uses the **Random Forest Classification Algorithm** and is deployed as a web application using **Flask** with a responsive frontend built using **HTML, CSS, and Bootstrap**.

---

# 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help doctors and patients take preventive measures before complications occur.

This project uses the **Pima Indians Diabetes Dataset** from Kaggle to train a Machine Learning model that predicts whether a patient is diabetic or not based on various health parameters.

The trained model is integrated with a Flask web application, allowing users to enter patient information through a simple web interface and receive an instant prediction.

---

# 🎯 Objectives

- Predict whether a patient has diabetes.
- Apply Machine Learning to a real-world healthcare problem.
- Build a complete web application using Flask.
- Create a user-friendly interface for entering patient data.
- Demonstrate Machine Learning model deployment.

---

# ✨ Features

- Predict diabetes using Machine Learning
- Attractive and responsive user interface
- Fast prediction using a trained model
- Data preprocessing before prediction
- Flask backend integration
- Responsive design using Bootstrap
- Easy to understand project structure

---

# 🛠 Technologies Used

## Programming Language

- Python

## Frontend

- HTML5
- CSS3
- Bootstrap 5

## Backend

- Flask

## Machine Learning

- Scikit-learn

## Data Processing

- Pandas
- NumPy

## Model Storage

- Joblib

## Dataset

- Pima Indians Diabetes Dataset (Kaggle)

---

# 🧠 Machine Learning Algorithm

## Random Forest Classifier

This project uses the **Random Forest Classification Algorithm**.

Random Forest creates multiple decision trees during training and predicts the final result using majority voting.

### Advantages

- High Accuracy
- Less Overfitting
- Works well on medical datasets
- Handles nonlinear relationships
- Robust and reliable

---

# 📂 Dataset Information

Dataset Name:

**Pima Indians Diabetes Dataset**

Source:

Kaggle

Number of Records:

- 768

Number of Features:

- 8 Input Features
- 1 Output Feature

Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

Target

- Outcome

0 → Not Diabetic

1 → Diabetic

---

# ⚙ Machine Learning Workflow

```
Dataset
     │
     ▼
Load Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Replace Invalid Zero Values
     │
     ▼
Feature Selection
     │
     ▼
Standardization
     │
     ▼
Train-Test Split
     │
     ▼
Random Forest Training
     │
     ▼
Model Evaluation
     │
     ▼
Save Model (.pkl)
     │
     ▼
Flask Integration
     │
     ▼
Prediction
```

---

# 📊 Data Preprocessing

The following preprocessing steps were performed:

- Loaded dataset using Pandas
- Checked missing values
- Replaced invalid zero values with median values
- Selected input and output features
- Standardized data using StandardScaler
- Split dataset into training and testing sets

---

# 📈 Model Performance

Algorithm Used

- Random Forest Classifier

Training Data

- 80%

Testing Data

- 20%

Accuracy Achieved

- **75.97%**

---

# 📁 Project Structure

```
Diabetes-Prediction-System/

│

├── dataset/
│     └── diabetes.csv
│
├── model/
│     ├── diabetes_model.pkl
│     └── scaler.pkl
│
├── static/
│     └── css/
│           └── style.css
│
├── templates/
│     ├── index.html
│     └── result.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Diabetes-Prediction-System.git
```

Move into the project directory

```bash
cd Diabetes-Prediction-System
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Train the Machine Learning Model

```bash
python train_model.py
```

Run Flask Application

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

# 🧪 Sample Input

| Feature | Value |
|----------|------:|
| Pregnancies | 6 |
| Glucose | 148 |
| Blood Pressure | 72 |
| Skin Thickness | 35 |
| Insulin | 0 |
| BMI | 33.6 |
| Diabetes Pedigree Function | 0.627 |
| Age | 50 |

Expected Output

```
Patient is Diabetic
```

---

# 💻 Frontend

The frontend is developed using

- HTML5
- CSS3
- Bootstrap

Responsibilities

- Accept patient information
- Display prediction result
- Responsive design
- User-friendly interface

---

# ⚙ Backend

The backend is developed using

- Flask
- Python

Responsibilities

- Receive user input
- Load trained Machine Learning model
- Scale input values
- Predict diabetes
- Return prediction result

---

# 📦 Python Libraries Used

- pandas
- numpy
- scikit-learn
- flask
- joblib

---

# 📚 Future Improvements

- Login Authentication
- Patient Management System
- Prediction History
- PDF Report Generation
- Database Integration (SQLite/MySQL)
- Admin Dashboard
- Charts and Analytics
- Email Notifications
- Cloud Deployment
- Mobile Responsive Dashboard

---

# 📖 Learning Outcomes

Through this project, I learned:

- Data preprocessing
- Feature engineering
- Machine Learning model training
- Random Forest Classification
- Model evaluation
- Flask web development
- Frontend and backend integration
- Machine Learning model deployment

---

# 👨‍💻 Author

**Sujay**

Machine Learning & Web Development Project

---

# 📄 License

This project is developed for educational and learning purposes.
