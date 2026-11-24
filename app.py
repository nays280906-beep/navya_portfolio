from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=data.PROFILE,
        projects=data.PROJECTS,
        experience=data.EXPERIENCE,
        skills=data.SKILLS,
    )

if __name__ == "__main__":
    app.run(debug=True)