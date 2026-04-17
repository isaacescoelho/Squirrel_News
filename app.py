from flask import Flask, render_template, request
import requests

app = Flask(__name__)

all_articles = requests.get("https://api.npoint.io/11ad36772c8ebffa8e28").json()


@app.route('/')
def index():
    return render_template('index.html', main_article=all_articles["main-headline"], rest_of_articles=all_articles["other-stories"])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/article/<article_id>')
def article(article_id):
    if article_id != "main":
        article = next((a for a in all_articles["other-stories"] if str(a["id"]) == article_id), None)
    else:
        article = all_articles["main-headline"]

    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run()