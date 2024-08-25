from flask import Flask, render_template
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

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<post_id>')
def post(post_id):
    id = int(post_id) - 1
    post = data[id]
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)