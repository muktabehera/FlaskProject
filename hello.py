from flask import Flask
# from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/check")
def check():
    return "check, World!"

@app.route("/hello/<fname>/<lname>")
def hello_name(fname,lname):
    # return "hello name, World!"

    # return f"hello {name}, how are you?"

    #return "hello %s, how are you?" %name
    # return render_template()
     return f"hello {fname} {lname}"


@app.route("/sum/<num1>/<num2>")
def sum(num1,num2):
    # return "hello name, World!"

    # return f"hello {name}, how are you?"

    #return "hello %s, how are you?" %name
    # return render_template()
    sum = int(num1) +  int(num2)
    return f"sum = {sum}"

if __name__ == '__main__':
    app.run(debug=True)