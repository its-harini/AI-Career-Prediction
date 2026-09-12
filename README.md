# 🎯 AI-Based Career Prediction and Personalized Skill Gap Analyzer

An AI-powered career guidance system that uses Machine Learning to predict suitable career paths based on a student's technical skills, communication ability, aptitude, and project experience.

The system also identifies skill gaps and provides personalized learning recommendations for the predicted career.
## 🌐 Live Demo

Try the application here:

https://ai-career-prediction-8zmtj2jvzwvizndsuggxb9.streamlit.app/
## 🚀 Features

* 🤖 Machine Learning based career prediction
* 🎯 Predicts suitable career paths
* 📊 Displays top 3 career matches
* 📚 Personalized skill gap analysis
* 🚀 Learning recommendations based on missing skills
* 📈 Model evaluation using accuracy and confusion matrix
* 🔍 Feature importance analysis
* 🖥️ Interactive Streamlit web application

## 💼 Career Categories

The system predicts among 8 career paths:

1. Software Developer
2. Web Developer
3. Data Analyst
4. Data Scientist
5. Machine Learning Engineer
6. AI Engineer
7. Cloud Engineer
8. Cybersecurity Analyst

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* Matplotlib
* Streamlit
* Joblib

## 🧠 Machine Learning Approach

The project uses a **Random Forest Classifier** to predict the most suitable career based on the student's skill profile.

### Input Features

* Python
* Java
* SQL
* Machine Learning
* Web Development
* Cloud
* Cybersecurity
* Communication
* Aptitude
* Number of Projects

The dataset contains **800 synthetically generated student profiles**, with 100 profiles for each career category.

The dataset is intended for educational and demonstration purposes.

## 📊 Model Performance

The Random Forest model achieved:

**Test Accuracy: 84.58%**

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Feature Importance

> Note: The dataset is synthetically generated, so this accuracy should not be interpreted as real-world career prediction performance.

## 📚 Skill Gap Analysis

After predicting a career, the system compares the student's current skills with predefined recommended skill levels for that career.

For example:

```text
Career: Machine Learning Engineer

SQL
Current: 4
Required: 7
Gap: 3

Projects
Current: 2
Required: 3
Gap: 1
```

The system then provides learning recommendations for the identified gaps.

## 🖥️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd AI-Career-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
AI-Career-Prediction/
│
├── app.py
├── dataset.csv
├── generate_dataset.py
├── check_dataset.py
├── train_model.py
├── evaluate_model.py
├── skill_gap.py
├── predict.py
├── model.pkl
├── requirements.txt
└── README.md
```

## 🔮 Future Enhancements

* Use real-world student skill datasets
* Add user authentication
* Add career roadmap generation
* Integrate job market trends
* Add course recommendations
* Add resume analysis
* Deploy the application online
* Improve model performance using additional algorithms

## 👩‍💻 Author

**Harini Santhakumar**

B.Tech Information Technology

Interested in Machine Learning, Software Development and AI-based applications.
