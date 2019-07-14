#!/usr/bin/python3

import uuid
import models
from datetime import datetime
''' Base model class that defines all common attributes/methods
for other classes'''


class BaseModel():
    def __init__(self, *args, **kwargs):
        '''intializing values'''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)  # stores new instance
        else:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        '''returns string representation'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''saves the current time of creation'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of the instance'''
        x = self.__dict__.copy()
        x['__class__'] = self.__class__.__name__
        x['created_at'] = self.created_at.isoformat()
        x['updated_at'] = self.updated_at.isoformat()
        return x
