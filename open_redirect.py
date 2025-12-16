from flask import Flask, request, redirect

app = Flask(__name__)

# Open redirect vulnerabilities
@app.route('/redirect')
def redirect_url():
    target = request.args.get('url')
    # Vulnerable: unvalidated redirect
    return redirect(target)

@app.route('/goto')
def goto():
    next_page = request.args.get('next')
    # Vulnerable: open redirect
    return redirect(next_page, code=302)

@app.route('/return')
def return_url():
    return_to = request.args.get('return_to')
    # Vulnerable: no validation
    return redirect(return_to)

@app.route('/forward')
def forward():
    destination = request.form.get('destination')
    # Vulnerable: POST-based open redirect
    return redirect(destination)
