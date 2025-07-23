from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_password():
    password = ''
    if request.method == 'POST':
        letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        numbers = list('0123456789')
        symbols = list('!#$%&()*+')

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = (
            [random.choice(letters) for _ in range(nr_letters)] +
            [random.choice(symbols) for _ in range(nr_symbols)] +
            [random.choice(numbers) for _ in range(nr_numbers)]
        )

        random.shuffle(password_list)
        password = ''.join(password_list)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Required for Render
    app.run(host='0.0.0.0', port=port)        # Required for Render
