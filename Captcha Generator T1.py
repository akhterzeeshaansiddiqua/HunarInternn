from flask import Flask, render_template_string
import random
import string

app = Flask(__name__)

def generate_captcha(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route('/')
def home():
    captcha = generate_captcha()
if __name__ == '__main__':
    app.run(port=8080)
