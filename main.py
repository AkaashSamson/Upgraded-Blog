from flask import Flask, render_template, request
import requests
import smtplib

my_email = "akaashsam22@gmail.com"
my_passkey = "jtljflkpcjcsizwb"

connection = smtplib.SMTP("smtp.gmail.com") # this line is used to connect to the smtp server
connection.starttls() # this line is used to secure the connection which means that the data is encrypted
connection.login(user=my_email, password=my_passkey) # this line is used to login to the email account


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
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
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