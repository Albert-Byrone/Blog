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
    quotes = get_quotes()
    page = request.args.get('page',1,type =int)
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page,per_page = 3)
    return render_template('index.html',quote=quotes,blogs=blogs)

def save_pic(form_picture):
