from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Fetched once at startup and cached in memory for the lifetime of the process
all_articles = requests.get("https://api.npoint.io/11ad36772c8ebffa8e28").json()


# --- News routes ---

@app.route('/')
def index():
    other_articles = sorted(all_articles["other-stories"], key=lambda x: x["id"])[::-1]
    return render_template(
        'index.html',
        main_article=all_articles["main-headline"],
        rest_of_articles=other_articles,
    )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/article/<article_id>')
def article(article_id):
    if article_id == "main":
        article_data = all_articles["main-headline"]
    elif int(article_id) > len(all_articles["other-stories"]):
        article_data = all_articles["main-headline"]
    else:
        article_data = next(
            (a for a in all_articles["other-stories"] if str(a["id"]) == article_id),
            None,
        )
    return render_template('article.html', article=article_data)


@app.route('/search')
def search():
    query = request.args.get('article_to_find').lower()
    all_stories = all_articles["other-stories"] + [all_articles["main-headline"]]
    query_articles = [story for story in all_stories if query in story["title"].lower()]
    return render_template('search.html', query=query, results=query_articles)


# --- Puzzle routes ---

# Maps puzzle names to representative Unsplash cover images used on the puzzles index page
PUZZLE_IMAGES = {
    "sudoku": "https://images.unsplash.com/photo-1731692243942-26c035b5cf60?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8c3Vkb2t1fGVufDB8fDB8fHww",
    "word search": "https://images.unsplash.com/photo-1552321046-a54642dc0cb8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8d29yZCUyMHNlYXJjaHxlbnwwfHwwfHx8MA%3D%3D",
    "the mini": "https://images.unsplash.com/photo-1626195205019-e39840c1df1c?q=80&w=2340&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "the crossword": "https://images.unsplash.com/photo-1731320965510-0c48cf81bd56?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Y3Jvc3N3b3JkfGVufDB8fDB8fHww",
    "quizzler": "https://plus.unsplash.com/premium_photo-1679957333039-285fb913aa2b?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cXVpenxlbnwwfHwwfHx8MA%3D%3D",
}


@app.route("/puzzles")
def puzzles():
    return render_template('puzzles/index.html', all_puzzles=PUZZLE_IMAGES)


@app.route("/sudoku")
def sudoku():
    return render_template('puzzles/sudoku.html')


@app.route("/word_search")
def word_search():
    return render_template('puzzles/word_search.html')


@app.route("/the_mini")
def the_mini():
    return render_template('puzzles/the_mini.html')


@app.route("/the_crossword")
def the_crossword():
    return render_template('puzzles/the_crossword.html')


@app.route("/quizzler")
def quizzler():
    return render_template('puzzles/quizzler.html')


if __name__ == '__main__':
    app.run()