import pandas as pd

names = ['id', 'name', 'year', 'rating', 'votes', 'length', 'genre']
data = pd.read_csv('imdb_top_10000.txt', sep='\t', names=names, index_col=0)

question = []
answer = []


# Question One ##############################################

question.append("What was the highest scoring movie in 1996?")

# Returns film ids and years
# data['year']

# Returns boolean result for whether data['year'] is 1996
# data['year'] == 1996

# # Returns (unsorted) full table of all films with year == 1996
unsorted_year = data[data['year'] == 1996]

# Prints a sorted list (by rating) highest on top
sorted_year = unsorted_year.sort_values(by='rating', ascending=False)

# Assigns the top result only to variable
top_result = sorted_year.head(1)

# Convert answer to string, without any indexing or column headings
answer.append(top_result['name'].to_string(header=False, index=False))


# Question Two ##############################################

question.append("In what year was the highest rated movie of all time made?")

# Sort the data by ratings, highest at the top, take the highest value
highest_rating = data.sort_values(by='rating', ascending=False).head(1)

# Get the value for year
highest_rating_year = highest_rating['year']
highest_rating_year.to_string(index=False, header=False)

# Add to answer list, as a string, without index or header
answer.append(highest_rating_year.to_string(index=False, header=False))


# Question Three ############################################

question.append("What five movies have the most votes ever?")
answer.append(" ")


# Question Four #############################################

question.append("What year in the 1960s had the highest average movie rating?")
answer.append(" ")

for question_number in range(1, len(question)+1):
    print(f"Question Number : {question_number}")
    print(question.pop(0))
    print(answer.pop(0), '\n')
