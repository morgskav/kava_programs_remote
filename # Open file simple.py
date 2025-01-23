#This version in in the branch "make_class"

# Open file simple
class GradesDataframe:
    pass

# Opens the grades.csv document in read mode.
with open("grades.csv", "r") as f:
    content = f.read()
    # sets the data frame dictionary
    df = {}
    # initiates the column headings list
    column_headings = []
    
    for line in content.splitlines():
        # cleans each item in the row and cleans the rows
        row = [i.strip('"\'') for i in line.strip().split(",")]
        if not column_headings:
            column_headings.extend(row)
            continue
        if not df:
            for i in range(len(row)):
                df[column_headings[i]] = [row[i]]
        for i in range(len(row)):
                df[column_headings[i]].append(row[i])


selected = ['First name', 'Last name', 'ID number', 'Quiz: Review of self-study quizzes weeks 1-4 (Graded quiz 1/2) (Percentage)', 'Quiz: Review of self-study quizzes weeks 5-14 (Graded quiz 2/2) (Percentage)', 'Quiz: Preparing for Exam with SEB (Percentage)', 'Quiz: Preparing for Exam with SEB (Letter)', 'Quiz: PrÃ¼fung Grammatik/Textanalyse 1 FS1 ENG (Real)', 'Quiz: PrÃ¼fung Grammatik/Textanalyse 1 FS1 ENG (Percentage)', 'Course total (Percentage)', 'Course total (Letter)']


grades_df = {}

for i in range(len(selected)):
    grades_df[selected[i]] = df[selected[i]]

#can access the data in the data frame by giving the heading as the dictionary key, and the slice the list output by the desired row number.
# can get the row numbers of the students names, but for individuality, need to actually work with the ID number.  
def lookup(ID):
    # get row index of ID
    selected = ['First name', 'Last name', 'ID number', 'Quiz: Review of self-study quizzes weeks 1-4 (Graded quiz 1/2) (Percentage)', 'Quiz: Review of self-study quizzes weeks 5-14 (Graded quiz 2/2) (Percentage)', 'Quiz: Preparing for Exam with SEB (Percentage)', 'Quiz: Preparing for Exam with SEB (Letter)', 'Quiz: PrÃ¼fung Grammatik/Textanalyse 1 FS1 ENG (Real)', 'Quiz: PrÃ¼fung Grammatik/Textanalyse 1 FS1 ENG (Percentage)', 'Course total (Percentage)', 'Course total (Letter)']
    row_index_ID = grades_df['ID number'].index(ID)
    data = [grades_df[i][row_index_ID] for i in selected]
    
    return " \n".join([": ".join([selected[i], data[i]]) for i in range(len(selected))])
    


print(lookup('C2D8487A-0F50-4921-9767-E3354486259F@zhaw.ch'))