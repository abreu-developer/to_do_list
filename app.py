from flask import Flask

# __name__ ==  main
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello_world!!!"

@app.route("/about")
def about():
    return "pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)#so para desenvolvimento local