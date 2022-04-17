from flask import Flask, request
import requests
import bs4
from speech_conversion import speech_to_text, text_to_speech

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def evaluate():
  #if request.method == "GET":
   # return render_template("index.html")
  if request.method == "GET":
    #name = request.json["name"]
    #file = request.json["file"]
    #print(name)

    name = 'Sam'
    filename = 'output.mp3'
    text = speech_to_text(filename)
    for punc in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
      text = text.replace(punc, '')

    if name in text:
      search_query = text[text.index(name) + len(name):]
      url = 'https://google.com/search?q=' + search_query
      result = requests.get(url)
      soup = bs4.BeautifulSoup(result.text, "html.parser")
      answer = soup.find("div", class_="BNeawe").text

      text_to_speech(answer)
      return '<p>' + answer + '</p>'
    else:
      return '<p>Your name was not called.</p>'

if __name__ == '__main__':
  app.debug = True
  app.run()