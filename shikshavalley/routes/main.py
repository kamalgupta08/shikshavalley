from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/news')
def news():
    return render_template('news.html')

@main.route('/downloads')
def downloads():
    return render_template('downloads.html')

@main.route('/principal')
def principal():
    return render_template('principal.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')