from flask import Flask

app = FLask(__name__)

@app.route("/")
def home():
  return "CIAO"

fi __name__ == "__main__":
app.run(host=0.0.0.0", port=5000, debug=True)
