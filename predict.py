import joblib
import pandas as pd
from skill_gap import show_skill_gap
# Load trained model
model = joblib.load("model.pkl")

print("====================================")
print("   AI CAREER PREDICTION SYSTEM")
print("====================================")

# Get student skills
python = int(input("Python skill (1-10): "))
java = int(input("Java skill (1-10): "))
sql = int(input("SQL skill (1-10): "))
machine_learning = int(input("Machine Learning skill (1-10): "))
web_development = int(input("Web Development skill (1-10): "))
cloud = int(input("Cloud skill (1-10): "))
cybersecurity = int(input("Cybersecurity skill (1-10): "))
communication = int(input("Communication skill (1-10): "))
aptitude = int(input("Aptitude skill (1-10): "))
projects = int(input("Number of projects (0-10): "))

# Create input data
student = pd.DataFrame([[
    python,
    java,
    sql,
    machine_learning,
    web_development,
    cloud,
    cybersecurity,
    communication,
    aptitude,
    projects
]], columns=[
    "python",
    "java",
    "sql",
    "machine_learning",
    "web_development",
    "cloud",
    "cybersecurity",
    "communication",
    "aptitude",
    "projects"
])

# Predict career
prediction = model.predict(student)[0]

# Get prediction probabilities
probabilities = model.predict_proba(student)[0]
confidence = max(probabilities) * 100

print("\n====================================")
print("        CAREER PREDICTION")
print("====================================")

print(f"Recommended Career: {prediction}")
print(f"Prediction Confidence: {confidence:.2f}%")
student_skills = {
    "python": python,
    "java": java,
    "sql": sql,
    "machine_learning": machine_learning,
    "web_development": web_development,
    "cloud": cloud,
    "cybersecurity": cybersecurity,
    "communication": communication,
    "aptitude": aptitude,
    "projects": projects
}

show_skill_gap(prediction, student_skills)