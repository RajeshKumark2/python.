# Flask URL shortener
from flask import Flask, redirect, request
import hashlib

app = Flask(__name__)
url_map = {}

@app.route('/shorten/<path:url>')
def shorten(url):
    short_code = hashlib.md5(url.encode()).hexdigest()[:6]
    url_map[short_code] = url
    return f"Short URL: {request.host_url}{short_code}"

@app.route('/<short_code>')
def redirect_url(short_code):
    return redirect(url_map.get(short_code, '/'))