from flask import Flask, request, jsonify, g, make_response

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


@app.route("/test_wsgi")
def wsgi_test():
    def application(environ, start_response):
        print(environ)
        body = "The request method was %s" % environ["REQUEST_METHOD"]
        headers = [("Content-Type", "text/plain"),
                   ("Content-Length", str(len(body)))]
        start_response("200 OK", headers)

        return [body]

    return make_response(application)


@app.route("/rp")
def rp():
    q = request.args.get("q")
    return "q=%s" % str(q)
