from flask import Flask, render_template, request
import requests
from blogs import Blog

blog_data = Blog()
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)

