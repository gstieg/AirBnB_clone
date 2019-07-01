#!/usr/bin/python3
'''
user class that inherits from  BaseModels class
'''
from models.base_model import BaseModel

class User(BaseModel):
    '''
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
