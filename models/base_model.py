#!/usr/bin/python3
import uuid
from datetime import datetime
''' Base model class that defines all common attributes/methods
for other classes'''


class BaseModel():
    ''''''

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        '''intializing values'''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key is not '__class__':
                    setattr(self, key, value)

    def __str__(self):
        '''returns string representation'''
        return "[{}] ({}) {}".format\
=======
    def __init__(self):
        '''intializing values'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''returns string representation'''
        return "[{}] ({}) {}".format/
>>>>>>> 15c8c41b499efce2f2733fd547aa6fd0e594323d
        (self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''saves the current time of creation'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of the instance'''
        x = self.__dict__.copy()
        x['__class__'] = self.__class__.__name__
        x['created_at'] = self.created_at.isoformat()
        x['updated_at'] = self.updated_at.isoformat()
        return x