import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

main = Blueprint("main", __name__)

# Mock data
blogs = [{"title": "公告1", "content": "這是一條公告"}, {"title": "公告2", "content": "你猜這是什麼？"}]

@main.route("/")
def index():
    return render_template("index.html", blogs=blogs)

@main.route("/update", methods=["GET", "POST"])
def update():
    password = os.getenv("UPDATE_PASSWORD", "admin123")
    if request.method == "POST":
        if request.form.get("password") != password:
            flash("密碼錯誤", "danger")
            print("wrong pwd")
        else:
            title = request.form.get("title")
            content = request.form.get("content")
            if title and content:
                blogs.append({"title": title, "content": content})
                flash("上傳成功", "success")
                print(blogs)

            return redirect(url_for("main.index"))
    return render_template("update.html")

@main.route("/archive")
def archive():
    return render_template("archive.html")
