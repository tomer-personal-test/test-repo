from flask import Flask, request, render_template_string

app = Flask(__name__)

# XSS vulnerabilities
@app.route('/hello')
def hello():
    name = request.args.get('name')
    # Vulnerable: unescaped user input
    return f'<h1>Hello {name}!</h1>'

@app.route('/comment')
def show_comment():
    comment = request.args.get('comment')
    # Vulnerable: direct HTML rendering
    html = f'<div class="comment">{comment}</div>'
    return render_template_string(html)

@app.route('/search')
def search():
    query = request.args.get('q')
    # Vulnerable: reflected XSS
    return f'<p>Search results for: {query}</p>'

# SSTI vulnerability
@app.route('/template')
def template():
    template_str = request.args.get('template')
    # Vulnerable: Server-Side Template Injection
    return render_template_string(template_str)
