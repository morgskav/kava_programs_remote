#check_lines

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file grades 1
file_path = r"C:\Users\kava\OneDrive - ZHAW\24HS GrTxA1\Exam 2024\grades1.csv"
grades1_df = pd.read_csv(file_path)

columns = [
    'First name',
    'Last name' ,
    'ID number',
    'Course total (Letter)' 
]


grades_1 = grades1_df.sort_values(by='Last name', ascending=True)
grades_1_rel = grades_1[columns]
#print(grades_1_rel)

# Load the CSV file grades 2
file_path = r"C:\Users\kava\OneDrive - ZHAW\24HS GrTxA1\Exam 2024\grades2.csv"
grades2_df = pd.read_csv(file_path)


grades_2 = grades2_df.sort_values(by='Last name', ascending=True)
grades_2_rel = grades_2[columns]
print(grades_2_rel)

hash_grades = {}

# add grades 1 to hash_grades
for n, m, p in zip(grades_1_rel['Last name'], grades_1_rel['ID number'], grades_1_rel['Course total (Letter)']):
        hash_grades[(n, m)] = [p]
    

#Add grade 2 to hash grades
for n, m, p in zip(grades_2_rel['Last name'], grades_2_rel['ID number'], grades_2_rel['Course total (Letter)']):
        hash_grades[(n, m)].append(p)

for name in hash_grades.items():
    if name[1][0] != name[1][1]:
        print(name)
    
    
