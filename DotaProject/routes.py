"""
Routes and views for the bottle application.
"""
# -*- coding: utf-8 -*-
from bottle import route, view, template
from datetime import datetime

@route('/')
@route('/home')
@view('index')

def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        #title='Contact',
        #message='����',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        #title='About',
        #message='Your application description page.',
        year=datetime.now().year
    )

@route('/mama')
@view('mama')
def about():
    """Renders the about page."""
    return dict(
        #title="Strength",
        #message='Your application description page.',
        year=datetime.now().year
    )

@route('/update')
@view('update')
def about():
    with open('file.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    with open('file2.txt', 'r', encoding='utf-8') as file2:
        text2 = file2.read()
    with open('file3.txt', 'r', encoding='utf-8') as file3:
        text3 = file3.read()
    with open('file4.txt', 'r', encoding='utf-8') as file4:
        text4 = file4.read()
    with open('file5.txt', 'r', encoding='utf-8') as file5:
        text5 = file5.read()
    with open('file6.txt', 'r', encoding='utf-8') as file6:
        text6 = file6.read()
    with open('file7.txt', 'r', encoding='utf-8') as file7:
        text7 = file7.read()
    with open('file8.txt', 'r', encoding='utf-8') as file8:
        text8 = file8.read()
    with open('file9.txt', 'r', encoding='utf-8') as file9:
        text9 = file9.read()
    return template('update', text=text,text2=text2,text3=text3,text4=text4,text5=text5,text6=text6,text7=text7,text8=text8,text9=text9, year=datetime.now().year)

 


 



