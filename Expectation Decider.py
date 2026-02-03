# ================================
# EXPECTATION DECIDER – FULL PROJECT
# ================================

import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os

# -------------------------------
# 1) LOAD DATASET (YOUR T DRIVE PATH)
# -------------------------------
DATA_PATH = r"T:\RNW Course and Project\Math & statics\project 2\expectation_decider_dataset.csv"

print("Checking file path:", os.path.exists(DATA_PATH))

df = pd.read_csv(DATA_PATH)
print("\nDataset Loaded Successfully!")
print(df.head())
print("Total Students:", len(df))

# -------------------------------
# 2) BASIC COUNTS
# -------------------------------
total = len(df)

study_gt_10 = (df['study_hours'] > 10).sum()
att_gt_80 = (df['attendance'] > 80).sum()
both_study_att = ((df['study_hours'] > 10) & (df['attendance'] > 80)).sum()

group_yes = (df['group_discussion'] == 'Yes').sum()
group_no = (df['group_discussion'] == 'No').sum()

pass_count = (df['final_exam_pass'] == 'Pass').sum()
fail_count = (df['final_exam_pass'] == 'Fail').sum()

print("\n--- BASIC COUNTS ---")
print("Study >10 hours:", study_gt_10)
print("Attendance >80%:", att_gt_80)
print("Both Study & Attendance:", both_study_att)
print("Pass:", pass_count)
print("Fail:", fail_count)

# -------------------------------
# 3) EMPIRICAL & THEORETICAL PROBABILITY
# -------------------------------
p_pass = pass_count / total
print("\nEmpirical Probability P(Pass):", round(p_pass,4))

theoretical_all_pass = p_pass ** 3
print("Theoretical Probability (3 students all pass):", round(theoretical_all_pass,5))

# -------------------------------
# 4) BINOMIAL DISTRIBUTION
# -------------------------------
print("\n--- BINOMIAL DISTRIBUTION (n=3) ---")
n = 3
for k in range(4):
    prob = math.comb(n, k) * (p_pass**k) * ((1-p_pass)**(n-k))
    print(f"P(X={k}) = {round(prob,5)}")

mean = n * p_pass
variance = n * p_pass * (1-p_pass)
print("Mean:", round(mean,4))
print("Variance:", round(variance,4))

# -------------------------------
# 5) VENN DIAGRAM VALUES
# -------------------------------
only_study = study_gt_10 - both_study_att
only_att = att_gt_80 - both_study_att
neither = total - (only_study + only_att + both_study_att)

print("\n--- VENN DIAGRAM VALUES ---")
print("Only Study:", only_study)
print("Only Attendance:", only_att)
print("Both:", both_study_att)
print("Neither:", neither)

# -------------------------------
# 6) CONTINGENCY TABLE
# -------------------------------
contingency = pd.crosstab(df['group_discussion'], df['final_exam_pass'])
print("\n--- CONTINGENCY TABLE ---")
print(contingency)

joint = contingency.loc['Yes','Pass'] / total
conditional = contingency.loc['Yes','Pass'] / contingency.loc['Yes'].sum()

print("\nJoint P(Discussion Yes AND Pass):", round(joint,4))
print("Conditional P(Pass | Discussion Yes):", round(conditional,4))

# -------------------------------
# 7) BAR CHART – PASS VS FAIL
# -------------------------------
plt.figure()
df['final_exam_pass'].value_counts().plot(kind='bar')
plt.title("Pass vs Fail Students")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.show()

# -------------------------------
# 8) BAR CHART – GROUP DISCUSSION VS RESULT
# -------------------------------
contingency.plot(kind='bar')
plt.title("Group Discussion vs Result")
plt.xlabel("Group Discussion")
plt.ylabel("Number of Students")
plt.show()

# -------------------------------
# 9) STUDY HOURS VS RESULT
# -------------------------------
df['study_category'] = df['study_hours'] > 10
study_result = pd.crosstab(df['study_category'], df['final_exam_pass'])

study_result.plot(kind='bar')
plt.title("Study >10 Hours vs Result")
plt.xlabel("Study More Than 10 Hours")
plt.ylabel("Number of Students")
plt.show()

# -------------------------------
# 10) ATTENDANCE VS RESULT
# -------------------------------
df['attendance_category'] = df['attendance'] > 80
attendance_result = pd.crosstab(df['attendance_category'], df['final_exam_pass'])

attendance_result.plot(kind='bar')
plt.title("Attendance >80% vs Result")
plt.xlabel("High Attendance")
plt.ylabel("Number of Students")
plt.show()

# -------------------------------
# 11) PIE CHART – PASS PERCENTAGE
# -------------------------------
plt.figure()
df['final_exam_pass'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Pass Percentage")
plt.ylabel("")
plt.show()

# -------------------------------
# 12) VENN DIAGRAM
# -------------------------------
plt.figure()
venn2(subsets=(only_study, only_att, both_study_att),
      set_labels=('Study >10 hrs', 'Attendance >80%'))
plt.title("Venn Diagram: Study vs Attendance")
plt.show()

print("\n--- PROJECT COMPLETED SUCCESSFULLY ---")
