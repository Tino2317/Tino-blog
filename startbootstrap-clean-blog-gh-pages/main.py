from flask import Flask, render_template, request
import requests
import smtplib
from blogs import Blog

blog_data = Blog()
app = Flask(__name__)

LOGIN_EMAIL = "cheezy660@gmail.com"
SEND_EMAIL = "tmugwazo10@gmail.com"
PASSWORD = "pldqhzxgokijmhnp"


@app.route('/')
def home_page():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html", data=data)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/blog/<int:num>')
def blog_type(num):
    if num == 1:
        data = blog_data.first_blog()
        return render_template("post.html", data=data)
    elif num == 2:
        data = blog_data.second_blog()
        return render_template("post.html", data=data)
    elif num == 3:
        data = blog_data.third_blog()
        return render_template("post.html", data=data)


@app.route('/contact', methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(LOGIN_EMAIL, PASSWORD)
        connection.sendmail(from_addr=LOGIN_EMAIL,
                            to_addrs=SEND_EMAIL,
                            msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)

