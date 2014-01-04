from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mapviewer = Blueprint('mapviewer', __name__,
                        template_folder='templates')

@mapviewer.route('/', defaults={'page': 'index'})
@mapviewer.route('/<page>')
def show(page):

    return "hello World!"