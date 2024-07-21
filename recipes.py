from flask import Flask, render_template

recipes = Flask(__name__)

@recipes.route("/")
def home():
    return render_template("index.html") # Главная страница
@recipes.route("/blogs/")
def blogs():
    return render_template("blog.html") # Страница блога

@recipes.route("/contact/")
def contact():
    return render_template("contacts.html") # Страница с контактами


if __name__ == "__main__":
    recipes.run()
