from flask import Flask, render_template, url_for, request, jsonify
# from flask_wtf import FlaskForm
# from wtforms import BooleanField


app = Flask(__name__)
app.secret_key = ""

text = 'The Biden administration plans to require most foreign visitors to be vaccinated.Biden Plans New Policy Requiring That All Foreign Travelers to U.S. Be VaccinatedThe Biden administration is developing plans to require all foreign travelers to the United States to be vaccinated against Covid-19, with limited exceptions, according to an administration official with knowledge of the developing policy.Officials say the new policy is being readied in the event that the United States eases its travel rules, which isn’t expected soon.'


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")

# keyword_extractor(text, top_n, diversity, mmr)


@app.route('/extract_keywords', methods=['POST', 'GET'])
def extract_keywords():
    from extract_keywords import keyword_extractor
    mmr = request.args.get('mmr', type=bool)
    diversity = request.args.get('diversity', 0.2, type=float)
    top_n = request.args.get('top_n', 6, type=int)
    return jsonify(result=keyword_extractor(text, top_n, diversity, mmr), )


@app.route("/first_article", methods=["POST", "GET"])
def first_article():

    return render_template("first_article.html", title="Article")


if __name__ == "__main__":
    app.run(debug=True)
