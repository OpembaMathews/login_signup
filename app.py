from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route('/')
def home():
   pass
   return render_template ('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    pass
    return render_template ('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    pass
    return render_template ('signup.html')

if __name__ == '__main__':
    app.run(debug = True)