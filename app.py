import os
from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates, RatesNotAvailableError

app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/convert', methods=['POST'])
def convert():
    c = CurrencyRates()
    first_currency = request.form['c1'].upper()
    second_currency = request.form['c2'].upper()
    
    try:
        amount = float(request.form['amt'])
    except ValueError:
        # Handles invalid amount input
        return render_template('error.html', error_message="Invalid amount entered.")

    try:
        rate = round(c.convert(first_currency, second_currency, amount), 2)
    except RatesNotAvailableError:
        # Handles the situation where rates are not available
        return render_template('error.html', error_message="Currency rates source not ready.")
    except Exception as e:
        # Handles any other exception that might occur
        return render_template('error.html', error_message=str(e))

    # Continue if no exceptions are raised
    return render_template(
        'convert.html',
        rate=rate, amount=amount,
        first_currency=first_currency,
        second_currency=second_currency)



