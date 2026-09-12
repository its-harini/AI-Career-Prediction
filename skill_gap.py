# Career Skill Requirements

career_requirements = {
    "Machine Learning Engineer": {
        "python": 8,
        "sql": 7,
        "machine_learning": 8,
        "cloud": 5,
        "communication": 6,
        "aptitude": 6,
        "projects": 3
    },

    "Data Scientist": {
        "python": 8,
        "sql": 8,
        "machine_learning": 7,
        "cloud": 4,
        "communication": 6,
        "aptitude": 6,
        "projects": 3
    },

    "AI Engineer": {
        "python": 9,
        "sql": 6,
        "machine_learning": 8,
        "cloud": 5,
        "communication": 6,
        "aptitude": 6,
        "projects": 3
    },

    "Software Developer": {
        "python": 5,
        "java": 8,
        "sql": 6,
        "web_development": 6,
        "communication": 6,
        "aptitude": 7,
        "projects": 3
    },

    "Web Developer": {
        "python": 4,
        "java": 5,
        "sql": 5,
        "web_development": 8,
        "communication": 6,
        "aptitude": 6,
        "projects": 3
    },

    "Cloud Engineer": {
        "python": 5,
        "java": 5,
        "sql": 5,
        "cloud": 8,
        "cybersecurity": 5,
        "communication": 6,
        "aptitude": 6,
        "projects": 3
    },

    "Cybersecurity Analyst": {
        "python": 5,
        "java": 4,
        "sql": 5,
        "cloud": 6,
        "cybersecurity": 8,
        "communication": 6,
        "aptitude": 6,
        "projects": 3
    },

    "Data Analyst": {
        "python": 6,
        "sql": 8,
        "machine_learning": 5,
        "communication": 7,
        "aptitude": 7,
        "projects": 3
    }
}


def analyze_skill_gap(career, student_skills):
    requirements = career_requirements[career]

    gaps = {}

    for skill, required_score in requirements.items():
        current_score = student_skills.get(skill, 0)

        if current_score < required_score:
            gaps[skill] = {
                "current": current_score,
                "required": required_score,
                "gap": required_score - current_score
            }

    return gaps


def show_skill_gap(career, student_skills):
    gaps = analyze_skill_gap(career, student_skills)

    print("\n====================================")
    print("         SKILL GAP ANALYSIS")
    print("====================================")

    print(f"\nCareer: {career}")

    if not gaps:
        print("\nExcellent! You meet all the recommended skill levels.")
        return

    print("\nSkills to Improve:")

    for skill, details in sorted(
        gaps.items(),
        key=lambda x: x[1]["gap"],
        reverse=True
    ):
        print(
            f"- {skill}: "
            f"Current = {details['current']}, "
            f"Required = {details['required']}, "
            f"Gap = {details['gap']}"
        )