from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_random_quote():
    response = requests.get("https://api.quotable.io/random", verify=False)
    if response.status_code == 200:
        return response.json()  # Возвращает JSON-объект
    else:
        return {"content": "Не удалось получить цитату", "author": "Неизвестно"}


@app.route('/')
def home():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run(debug=True)