from flask import Flask
import os
template_dir = os.path.abspath('../error/templates')

app = Flask(__name__ , template_folder=template_dir)

from app import views