from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
URL = os.environ["API"]
posts = requests.get(URL).json()

app = Flask(__name__)

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
BOT_TOKEN = os.environ["TOKEN"]
BOT_ID = os.environ["ID"]

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    global num
    num += 1
    return render_template("contact.html", number=num)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

num = 0
@app.route("/contact", methods=["GET","POST"])
def data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        my_message = f"Name:{name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}"
        telegram_bot_sendtext(my_message)

        send_mail(name, email, phone, message)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_mail(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls() #Makes the connection secure
        connection.login(user=os.environ["EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL"],
                            to_addrs="jeongyoo03@gmail.com",
                            msg=f"Subject:Question About You\n\nName:{name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}")


def telegram_bot_sendtext(bot_message):
    global BOT_ID, BOT_TOKEN
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_ID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
