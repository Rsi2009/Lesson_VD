from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница с формой
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        # Передаем данные в шаблон для отображения
        return render_template('form.html', name=name, city=city, hobby=hobby, age=age)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)