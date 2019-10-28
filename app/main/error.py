from flask import render_template
from . import main

@main.errorhandler(404)
def four_Ow_four(error):
    '''
    function there render error 404 page
    '''
    render_template('error.html'),404