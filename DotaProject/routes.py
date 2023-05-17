"""
Routes and views for the bottle application.
"""
# -*- coding: utf-8 -*-
from re import I
from bottle import route, view, template, request, redirect
from datetime import datetime
from module1 import load_reviews_from_file, save_review_to_file

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

@route('/update', method='GET')
@route('/update', method='POST')
@view('update')
def update():
    with open('file.txt', 'r', encoding='utf-8') as file: #Выгрузка текста из файлов
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

    reviews = load_reviews_from_file()

    if request.method == 'POST': #добавление информации отзывов
        nickname = request.forms.get('nickname')
        review = request.forms.get('review')
        phone = request.forms.get('phone')
        new_review = {'nickname': nickname, 'review': review, 'phone': phone}
        save_review_to_file(new_review)
        reviews.append(new_review)
        
       

    return template('update', text=text, text2=text2, text3=text3, text4=text4, text5=text5, text6=text6, text7=text7, text8=text8, text9=text9, reviews=reviews, year=datetime.now().year)

#@route('/add_review', method='POST')
#def add_review():
#    nickname = request.forms.get('nickname')
#    review = request.forms.get('review')
#    phone = request.forms.get('phone')
#    new_review = {'nickname': nickname, 'review': review, 'phone': phone}
#    save_review_to_file(new_review)
#    # Redirect to the update page to avoid form resubmission on page refresh
#    redirect('/update')




##@route('/update')
##@view('update')
##def update():
##    with open('reviews.txt', 'r', encoding='utf-8') as file10:
##        text10 = file10.read()
##    reviews = load_reviews_from_file()
##    return template('update', text10=text10, reviews=reviews, year=datetime.now().year)

##@route('/add_review', method='POST')
##def add_review():
##    nickname = request.forms.get('nickname')
##    review = request.forms.get('review')
##    phone = request.forms.get('phone')
##    new_review = {'nickname': nickname, 'review': review, 'phone': phone}
##    save_review_to_file(new_review)
##    return template('update', year=datetime.now().year)

 


 



