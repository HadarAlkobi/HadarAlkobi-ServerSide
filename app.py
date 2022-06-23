from flask import Flask, redirect
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session
from app_users import users

app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


@app.route('/')
def main_page():
    return redirect('/Ex2_HomePage')


@app.route('/Ex2_HomePage')
def homepage():
    return render_template('Ex2_HomePage.html')


@app.route('/Ex2_ContactPage')
def contact():
    return render_template('Ex2_ContactPage.html')


@app.route('/assignment3_1')
def assignment3():
    red_wine = {'Type no.1': 'Cabernet Sauvignon', 'Type no.2': 'Merlot', 'Type no.3': 'Malbec', 'Type no.4': 'Shiraz'}
    white_wine = {'Type no.1': 'Sauvignon Blanc', 'Type no.2': 'Chardonnay', 'Type no.3': 'Riesling',
                  'Type no.4': 'Gewurztraminer'}
    food = ['Cheese Plate', 'Seasonal Fruits', 'Bread and Olives', 'Salad']
    return render_template('assignment3_1.html',
                           red_wine=red_wine,
                           white_wine=white_wine,
                           food=food)


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_page():
    users_results = {}
    registration_results = {}

    if 'search' in request.args:
        search_data = request.args['search']
        if search_data == '':
            users_results = users
        else:
            for user, data in users.items():
                if search_data == data["name"] or search_data == data["email"]:
                    users_results.update({
                        user: users[user]
                    })

    if request.method == 'POST' and len(request.form) > 0:
        user_name = request.form['userName']
        user_email = request.form['email']
        session['username'] = user_name
        session['login'] = True

        num_of_users = len(users) + 1
        new_user_key = 'user{user_number}'.format(user_number=num_of_users)

        users.update({
            new_user_key: {
                'name': user_name,
                'email': user_email
            }
        })

        print(users)

    return render_template('assignment3_2.html',
                           users_results=users_results,
                           registration_results=registration_results)


@app.route('/log_out', methods=['GET', 'POST'])
def logout_func():
    print(1)
    session['login'] = False
    session.clear()
    return redirect(url_for('assignment3_2_page'))


if __name__ == 'main':
    app.run(debug=True)
