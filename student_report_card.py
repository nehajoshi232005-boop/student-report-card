import pandas as pd

# Student data
data = {
    "Name": ["Amit", "Neha", "Priya", "Rahul", "Sita"],
    "Marks": [85, 25, 95, 40, 55]
}

df = pd.DataFrame(data)

# Pass/Fail condition
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 33 else "Fail")

# Assign Grades
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(grade)

print(df)
