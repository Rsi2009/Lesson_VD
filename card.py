from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("card.html") # Внутри () пишем название html-файла в кавычках

if __name__ == "__main__":
    app.run()
