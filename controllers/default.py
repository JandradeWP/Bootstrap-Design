# coding: utf8

"""
    Default Controller
    Author  :   Alvaro Lizama Molina <me@alvarolizama.net>

    Copyright (c) 2011, Alvaro Lizama Molina.
"""

##################################################
### Dashboard
##################################################
@auth.requires_login()
def index(): 
    return dict(message=T('Hello World'))


##################################################
### Download uploaded files
##################################################
@auth.requires_login()
def download():
    return response.download(request,db)


##################################################
### Auth
##################################################
def user():
    return dict(form=auth())  
