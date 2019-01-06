from flask import Flask, render_template

from forms import CSVUploadForm

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = "dummy_key"


@app.route("/", methods=["GET", "POST"])
def index():
    form = CSVUploadForm()

    if form.validate_on_submit():
        return "Received file"
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()
