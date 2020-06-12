from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<int:user_id>')
def show_user_profile(user_id):
    return 'User %s' % user_id


if __name__ == '__main__':
    app.run(debug=True, use_reloaded=True)