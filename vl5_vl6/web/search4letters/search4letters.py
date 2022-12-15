from flask import Flask, render_template, request, jsonify

app = Flask(__name__)  # muss vor den Annotierungen stehen!


@app.route("/entry")
def entry_page() -> 'html':
    """Returns the entry page to the browser"""
    return render_template("entry.html",
                           the_title="Welcome to search4letters on the web!",
                           the_url="search4")


@app.route("/search4", methods=["POST"])
def search_for() -> 'html':
    """Returns the result of a call to "search4letters" to the browser"""
    return render_search_response()


def render_search_response(gen_json:bool=False) -> str:
    """Return either JSON or HTML search response"""
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    results = str(search4letters(phrase, letters))
    if gen_json:

        return jsonify(the_phrase=phrase,
                       the_letters=letters,
                       the_result=results)
    return render_template("results.html",
                           the_title="Here are your results",
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


def search4letters(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase))

if __name__ == "__main__":
    app.run(debug=True)
