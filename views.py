from flask import Blueprint,render_template,request,jsonify,redirect,url_for


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template('index.html')

@views.route("/login")
def login():
    username = "username"
    return render_template('login.html', username = username)






# @views.route("/<name>/home")
# def homepage(name):
#     string = "Welcome to " + str(name) + "'s homepage."
#     return render_template('index.html', username = string)

# # request: ?name=shelly
# @views.route("/home")
# def home_request():
#     # if I request for name
#     name = request.args.get('name')
#     string = "Welcome to " + str(name) + "'s homepage."
#     return render_template('index.html', username = string)

# @views.route("/json")
# def get_json():
#     return jsonify({'name': 'Eric'})

# # return json
# @views.route("/data")
# def get_data():
#     data = request.json
#     return jsonify(data)

# @views.route("/go-to-home")
# def go_to_home():
#     return redirect(url_for("views.get_json"))

# # template test
# @views.route("/template")
# def template_test():
#     return render_template('login.html')