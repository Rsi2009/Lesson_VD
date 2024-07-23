from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {
       "Link": "Рецепт блюда"
    }
    return render_template("home.html", **context) # Главная страница
@app.route("/blogs/")
def blogs():
    context = {
        "Link": "Блог"
    }
    return render_template("about.html", **context)


if __name__ == "__main__":
    app.run()
