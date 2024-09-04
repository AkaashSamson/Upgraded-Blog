from flask import Flask, render_template, request
import requests

response = requests.get('https://api.npoint.io/611d72b4a5dc1bf578bd')
data = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template('contact.html', msg_sent=True)
    else:
        return render_template('contact.html', msg_sent=False)

@app.route('/post/<post_id>')
def post(post_id):
    id = int(post_id) - 1
    post = data[id]
    return render_template('post.html', post=post)

# @app.route('/form-submit', methods=['POST'])
# def form_submit():
#     data = request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phone"])
#     print(data["message"])
#     return "<h1>Successfully sent your message</h1>"


if __name__ == '__main__':
    app.run(debug=True)