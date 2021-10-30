from flask import Flask, request, jsonify, g

app = Flask(__name__)
app.debug = True
app.users = {}
app.id_count = 1


@app.before_request
def before_request():
    print("before request!!")
    g.user_name = "justin"


@app.route("/")
def index() -> str:
    return "Hello " + getattr(g, "user_name", "user_name")


@app.route("/sign-up", methods=['POST'])
def sign_up():
    new_user = request.json
    new_user["id"] = app.id_count
    app.users[app.id_count] = new_user

    app.id_count += 1

    return jsonify(new_user)
