from flask import Flask
import pandas

app = Flask(__name__)


@app.route('/')
def hello():
    return midweek_challenge()


def midweek_challenge():
    names = [
            'id', 'name',
            'year', 'rating',
            'votes', 'length',
            'genre'
            ]

    data = pandas.read_csv('imdb_top_10000.txt',
                           sep='\t',
                           names=names,
                           index_col=0
                           )

    question = []
    answer = []

    # Question One ##############################################

    q1 = "What was the highest scoring movie in 1996?"
    question.append(q1)

    # Returns film IDs and years
    # data['year']

    # Returns boolean result for whether data['year'] is 1996
    # data['year'] == 1996

    # # Returns (unsorted) full table of all films with year == 1996
    unsorted_year = data[data['year'] == 1996]

    # Prints a sorted list (by rating) highest on top
    sorted_year = unsorted_year.sort_values(by='rating', ascending=False)

    # Assigns the top result only to variable
    top_result = sorted_year[sorted_year['rating']
                             == sorted_year['rating'].max()]

    # Convert answer to string, without any indexing or column headings
    answer.append(top_result['name'].to_string(header=False, index=False))

    # Question Two ##############################################

    q2 = "In what year was the highest rated movie of all time made?"
    question.append(q2)

    # Sort the data by ratings, highest at the top, take the highest value
    sorted_by_rating = data.sort_values(by='rating', ascending=False)

    highest_rating = sorted_by_rating[sorted_by_rating['rating']
                                      == sorted_by_rating['rating'].max()]

    # We just need the year, but name contains year, and looks clearer to me.
    highest_rating_year = highest_rating['name']

    # Add to answer list, as a string, without header
    # Left index to clarify the two films
    answer.append(highest_rating_year.to_string(index=False, header=False))

    # Question Three ############################################

    q3 = "What five movies have the most votes ever?"
    question.append(q3)

    # Sort by votes, highest on top
    most_votes = data.sort_values(by='votes', ascending=False)

    # we need only the top 5 names
    five_movies = most_votes['name'].head(5)

    # Convert to string without index or header, and add to list.
    answer.append(five_movies.to_string(index=False, header=False))

    # Question Four #############################################

    q4 = "What year in the 1960s had the highest average movie rating?"
    question.append(q4)

    # get films from the sixties only
    sixties_only = data[(1959 < data['year'])
                        & (data['year'] < 1970)]

    # Group films by year, average the rating
    average_by_year = sixties_only.groupby('year')['rating'].mean()

    # Sort by average rating, take top result
    best_year = average_by_year.sort_values(ascending=False).head(1)

    # Year is the index value in this set
    year_and_rating = best_year.to_string(index=True, header=False)

    # Split the answer into a list
    year = year_and_rating.split(' ', 1)

    # First entry is year
    answer.append(year[0])

    # Outputs to the screen, not good for flask

    # for question_number in range(1, len(question)+1):
    #     print(f"\nQuestion Number : {question_number}")
    #     print(question.pop(0))
    #     print(answer.pop(0), '\n')

    # Returns a dict object for flask to display

    output_dict = {}
    output = []

    for question_number in range(1, len(question)+1):
        output.append(f"Question Number : {question_number}")
        output.append(question.pop(0))
        output.append(answer.pop(0))

    output_dict.setdefault('Midweek Challenge', output)

    return output_dict
