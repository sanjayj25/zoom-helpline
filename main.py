from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def evaluate():
  if request.method == "GET":
    return '<p>Hello World!</p>'

if __name__ == '__main__':
  app.debug = True
  app.run()