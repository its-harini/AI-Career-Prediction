import pandas as pd
import random

random.seed(42)

careers = {
    "Machine Learning Engineer": {
        "python": (7, 10),
        "java": (1, 6),
        "sql": (6, 10),
        "machine_learning": (8, 10),
        "web_development": (1, 5),
        "cloud": (3, 8),
        "cybersecurity": (1, 5)
    },
    "Data Scientist": {
        "python": (7, 10),
        "java": (1, 5),
        "sql": (7, 10),
        "machine_learning": (6, 9),
        "web_development": (1, 5),
        "cloud": (2, 7),
        "cybersecurity": (1, 4)
    },
    "AI Engineer": {
        "python": (8, 10),
        "java": (1, 5),
        "sql": (5, 9),
        "machine_learning": (8, 10),
        "web_development": (1, 5),
        "cloud": (3, 8),
        "cybersecurity": (1, 5)
    },
    "Software Developer": {
        "python": (3, 8),
        "java": (7, 10),
        "sql": (5, 9),
        "machine_learning": (2, 6),
        "web_development": (3, 8),
        "cloud": (2, 6),
        "cybersecurity": (1, 5)
    },
    "Web Developer": {
        "python": (2, 6),
        "java": (2, 7),
        "sql": (4, 8),
        "machine_learning": (1, 5),
        "web_development": (8, 10),
        "cloud": (2, 6),
        "cybersecurity": (1, 5)
    },
    "Cloud Engineer": {
        "python": (2, 6),
        "java": (2, 7),
        "sql": (4, 8),
        "machine_learning": (2, 5),
        "web_development": (1, 5),
        "cloud": (8, 10),
        "cybersecurity": (3, 8)
    },
    "Cybersecurity Analyst": {
        "python": (2, 6),
        "java": (2, 6),
        "sql": (4, 8),
        "machine_learning": (1, 5),
        "web_development": (1, 5),
        "cloud": (3, 8),
        "cybersecurity": (8, 10)
    },
    "Data Analyst": {
        "python": (5, 9),
        "java": (1, 5),
        "sql": (8, 10),
        "machine_learning": (3, 7),
        "web_development": (1, 5),
        "cloud": (2, 6),
        "cybersecurity": (1, 4)
    }
}

rows = []

for career, skills in careers.items():

    for _ in range(100):

        row = {}

        for skill, value_range in skills.items():
            row[skill] = random.randint(
                value_range[0],
                value_range[1]
            )

        row["communication"] = random.randint(5, 10)
        row["aptitude"] = random.randint(5, 10)
        row["projects"] = random.randint(1, 6)
        row["career"] = career

        rows.append(row)

columns = [
    "python",
    "java",
    "sql",
    "machine_learning",
    "web_development",
    "cloud",
    "cybersecurity",
    "communication",
    "aptitude",
    "projects",
    "career"
]

df = pd.DataFrame(rows, columns=columns)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("dataset.csv", index=False)

print("New dataset created successfully!")
print("Total records:", len(df))
print("\nCareer distribution:")
print(df["career"].value_counts())