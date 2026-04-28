from flask import Flask, render_template, request
import requests

app = Flask(__name__)

all_articles = requests.get("https://api.npoint.io/11ad36772c8ebffa8e28").json()

@app.route('/')
def index():
    other_articles = sorted(all_articles["other-stories"], key=lambda x: x["id"])[::-1]
    return render_template('index.html', main_article=all_articles["main-headline"], rest_of_articles=other_articles)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/article/<article_id>')
def article(article_id):
    if article_id != "main":
        if int(article_id) > len(all_articles["other-stories"]):
            article = all_articles["main-headline"]
        else:
            article = next((a for a in all_articles["other-stories"] if str(a["id"]) == article_id), None)
    else:
        article = all_articles["main-headline"]

    return render_template('article.html', article=article)


@app.route('/search')
def search():
    query = request.args.get('article_to_find').lower()
    all_stories = all_articles["other-stories"] + [all_articles["main-headline"]]
    query_articles = [story for story in all_stories if query in story["title"].lower()]

    return render_template('search.html', query=query, results=query_articles)


PUZZLE_IMAGES = {
    "sudoku": "https://images.unsplash.com/photo-1731692243942-26c035b5cf60?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8c3Vkb2t1fGVufDB8fDB8fHww",
    "word search": "https://images.unsplash.com/photo-1552321046-a54642dc0cb8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8d29yZCUyMHNlYXJjaHxlbnwwfHwwfHx8MA%3D%3D",
}


@app.route("/puzzles")
def puzzles():
    return render_template('puzzles.html', all_puzzles=PUZZLE_IMAGES)

@app.route("/sudoku")
def sudoku():
    return render_template('sudoku.html')

@app.route("/word_search")
def word_search():
    return render_template('word_search.html')

if __name__ == '__main__':
    app.run()