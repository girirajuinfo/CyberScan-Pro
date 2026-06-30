from flask import Flask, render_template, request
import requests
from scanner.headers import check_security_headers

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        website = request.form["website"]

        try:

            response = requests.get(website, timeout=5)
            header_results = check_security_headers(website)
            
            result = {
                "website": website,
                "status": response.status_code,
                "message": "Website is Online",
                "headers": header_results
            }

        except requests.exceptions.MissingSchema:

            result = {
                "website": website,
                "status": "Error",
                "message": "Invalid URL. Please include https://"
            }

        except requests.exceptions.ConnectionError:

            result = {
                "website": website,
                "status": "Error",
                "message": "Website could not be reached."
            }
            
        except requests.exceptions.Timeout:

            result = {
               "website": website,
                "status": "Error",
                "message": "Request timed out. Website is taking too long to respond."
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)