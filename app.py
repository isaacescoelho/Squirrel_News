from flask import Flask, render_template, request
import requests

app = Flask(__name__)

all_articles = requests.get("https://api.npoint.io/11ad36772c8ebffa8e28").json()

all_puzzles = {"sudoku": "data:image/png;base64,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"}

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

@app.route("/puzzles")
def puzzles():
    all_puzzles = {
        "sudoku": "https://images.unsplash.com/photo-1731692243942-26c035b5cf60?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8c3Vkb2t1fGVufDB8fDB8fHww"
    }
    return render_template('puzzles.html', all_puzzles=all_puzzles)

@app.route("/sudoku")
def puzzle():
    return render_template('sudoku.html')

if __name__ == '__main__':
    app.run(debug=True)