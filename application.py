from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_page():
    """Application Form"""

    return render_template("application-form.html")


@app.route("/application-response")
def response_page():
    """Application Response"""

    applicant = request.args.get("firstname")

    return render_template("application-response.html",
                            applicant=applicant)

if __name__ == "__main__":
    app.run(debug=True)
