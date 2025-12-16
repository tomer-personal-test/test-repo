from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/template/render')
def render():
    template = request.args.get('template')
    # SSTI
    return render_template_string(template)

@app.route('/template/greet')
def greet():
    name = request.args.get('name')
    # XSS
    return f'<h1>Hello {name}!</h1>'
