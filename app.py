import streamlit as st
import pandas as pd
import joblib

from skill_gap import analyze_skill_gap


# Load trained model
model = joblib.load("model.pkl")


# Page configuration
st.set_page_config(
    page_title="AI Career Prediction",
    page_icon="🎯",
    layout="wide"
)


# Title
st.title("🎯 AI-Based Career Prediction & Skill Gap Analyzer")

st.write(
    "Enter your current skills and project experience to get "
    "a suitable career recommendation and personalized skill-gap analysis."
)


# Skill input section
st.header("📊 Enter Your Skills")

col1, col2 = st.columns(2)

with col1:
    python = st.slider("Python Skill", 1, 10, 5)
    java = st.slider("Java Skill", 1, 10, 5)
    sql = st.slider("SQL Skill", 1, 10, 5)
    machine_learning = st.slider("Machine Learning Skill", 1, 10, 5)
    web_development = st.slider("Web Development Skill", 1, 10, 5)

with col2:
    cloud = st.slider("Cloud Skill", 1, 10, 5)
    cybersecurity = st.slider("Cybersecurity Skill", 1, 10, 5)
    communication = st.slider("Communication Skill", 1, 10, 5)
    aptitude = st.slider("Aptitude Skill", 1, 10, 5)
    projects = st.slider("Number of Projects", 0, 10, 2)


st.divider()


# Prediction button
if st.button("🎯 Predict My Career", use_container_width=True):

    # Create student data
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


    # Career prediction
    prediction = model.predict(student)[0]

    probabilities = model.predict_proba(student)[0]

    confidence = max(probabilities) * 100


    # Top 3 career recommendations
    career_probabilities = pd.DataFrame({
        "Career": model.classes_,
        "Probability": probabilities * 100
    })

    career_probabilities = career_probabilities.sort_values(
        by="Probability",
        ascending=False
    )


    # Display career prediction
    st.success(f"🎯 Recommended Career: {prediction}")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )


    # Display top 3 careers
    st.subheader("📊 Top Career Matches")

    st.bar_chart(
        career_probabilities.head(3).set_index("Career")
    )


    # Student skill data
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


    # Analyze skill gaps
    gaps = analyze_skill_gap(prediction, student_skills)


    # Skill gap section
    st.subheader("📚 Your Skill Gap Analysis")


    if not gaps:

        st.success(
            "🎉 Excellent! You meet all the recommended skill levels."
        )

    else:

        st.warning(
            "The following skills need improvement:"
        )


        for skill, details in sorted(
            gaps.items(),
            key=lambda x: x[1]["gap"],
            reverse=True
        ):

            st.write(
                f"**{skill.replace('_', ' ').title()}** — "
                f"Current: {details['current']} | "
                f"Required: {details['required']} | "
                f"Gap: {details['gap']}"
            )


        # Personalized learning plan
        st.subheader("🚀 Recommended Learning Plan")


        recommendations = {
            "python": "Practice Python programming, NumPy, Pandas and problem solving.",
            "java": "Improve Java OOP, collections and basic DSA.",
            "sql": "Practice SQL queries, joins, subqueries and database concepts.",
            "machine_learning": "Learn supervised learning, model evaluation and Scikit-learn.",
            "web_development": "Learn HTML, CSS, JavaScript and basic React.",
            "cloud": "Learn cloud fundamentals, deployment and basic AWS/Azure services.",
            "cybersecurity": "Learn networking, security fundamentals and common vulnerabilities.",
            "communication": "Practice technical communication, presentations and interviews.",
            "aptitude": "Practice quantitative aptitude, logical reasoning and verbal ability.",
            "projects": "Build more practical projects and upload them to GitHub."
        }


        for skill in gaps:

            st.info(
                f"📌 **{skill.replace('_', ' ').title()}**: "
                f"{recommendations[skill]}"
            )