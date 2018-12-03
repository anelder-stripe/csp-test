from flask import Flask, request, render_template
from flask_csp.csp import csp_header

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/custom_checkout')
@csp_header({
    'default_src':"'self' localhost:5000",
    'connect-src':"checkout.stripe.com",
    'script-src':"'self' 'unsafe-inline' checkout.stripe.com localhost:5000",
    'frame-src':"checkout.stripe.com",
    'img-src':"'self' *.stripe.com"
})
def custom_checkout():
    return render_template('custom_checkout.html')

@app.route('/simple_checkout')
@csp_header({
    'default_src':"'self' localhost:5000",
    'connect-src':"checkout.stripe.com",
    'script-src':"checkout.stripe.com",
    'style-src':"checkout.stripe.com",
    'frame-src':"checkout.stripe.com",
    'img-src':"'self' *.stripe.com"
})
def simple_checkout():
    return render_template('simple_checkout.html')

@app.route('/stripe_js_v3')
@csp_header({
    'default-src':"'self' localhost:5000",
    'script-src':"'self' 'unsafe-inline' js.stripe.com localhost:5000",
    'connect-src':"api.stripe.com",
    'frame-src':"js.stripe.com"
})
def stripe_js_v3():
    return render_template('stripe_js_v3.html')

@app.route('/csp_report', methods=['POST'])
def csp_report():
	with open('./csp_report', "a") as fh:
		fh.write(request.data+"\n")
	return 'done'
