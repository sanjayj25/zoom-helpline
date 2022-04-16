from flask import Flask, request
import requests
import bs4

app = Flask(__name__)

@app.route("/", methods=["GET"])
def evaluate():
  if request.method == "GET":
    search_query = request.args.get("search_query")
    url = 'https://google.com/search?q=' + search_query
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, "html.parser")
    answer = soup.find("div", class_="BNeawe").text
    return str(soup)

if __name__ == '__main__':
  app.debug = True
  app.run()