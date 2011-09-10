# coding: utf8

"""
    Perseus users module
    Author  :   Alvaro Lizama Molina <me@alvarolizama.net>

    Copyright (c) 2011, Alvaro Lizama Molina.
"""
##################################################
### Users
##################################################

from gluon import *

##################################################
### Check user
##################################################
def check(db, email):
    query = db(db.auth_user.email == email)
    count = query.count()
    if count > 0:
        return True
    else:
        return False


##################################################
## Create user
##################################################
def create(db, **kwargs):

    password = db.auth_user.password.validate(kwargs['password'])[0]
    user_id = db.auth_user.insert(
                first_name=kwargs['first_name'],
                last_name=kwargs['last_name'],
                password=password,
                email=kwargs['email']
                )

    if 'role' in kwargs:
        db.auth_membership.insert(
                    user_id=user_id,
                    group_id=kwargs['role']
                    )

    return user_id


##################################################
## Update user
##################################################
def update(db, id, **kwargs):
    user = db(db.auth_user.id == id).select()


    user[0].update_record(
                first_name=kwargs['first_name'],
                last_name=kwargs['last_name'],
                email=kwargs['email']
                )

