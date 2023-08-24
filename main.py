from flask import Flask, render_template, redirect, url_for, request, flash, send_file
from flask_bootstrap import Bootstrap
from forms import Contact
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact = Contact()
    if request.method == "POST" and contact.validate_on_submit():
        name = contact.name.data
        email = contact.email.data
        phone = contact.phone.data
        message = contact.message.data

        gmail = "zia.aseh@gmail.com"
        app_password = os.environ.get("app_password")
        msg = f"Subject:Client\n\nI am {name} | My Email is {email} and My Phone num is: {phone} \nMessage: {message} :"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=gmail,
                password=app_password
            )
            connection.sendmail(
                from_addr=gmail,
                to_addrs=gmail,
                msg=msg
            )
            flash("Message Send Successfully!")
            return redirect(url_for("contact"))
    return render_template("contact.html", contact=contact)


@app.route("/downlaod_cv")
def download_pdf():
    file_path = "static/pdf-cv/ziauddin-resume.pdf"
    return send_file(file_path, as_attachment=True)


@app.route("/view_cv")
def view_pdf():
    file_path = "static/pdf-cv/ziauddin-resume.pdf"
    return send_file(file_path)


if __name__ == '__main__':
    app.run(debug=True)