from flask import render_template,url_for,request,flash,redirect,abort
from app.main  import main
from app.models import User,Blog,Comment,Subscriber
from .. import db
from app.requests import get_quotes
from .forms import UpdateProf,CreateBlog
from flask_login import login_required,current_user
import secrets
import os
from PIL import Image

@main.route('/')
def index():
    title= 'Testing file'
    return render_template('index.html',title=title)
