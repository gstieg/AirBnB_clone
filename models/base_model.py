#!/usr/bin/python3

import uuid
import models
from datetime import datetime
''' Base model class that defines all common attributes/methods
for other classes'''


class BaseModel():
    ''''''


    def __init__(self, *args, **kwargs):
        '''intializing values'''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
<<<<<<< HEAD
            models.storage.new(self)  # stores new instance
=======
<<<<<<< HEAD
            models.storage.new(self) #stores new instance
=======
            models.storage.new(self)  # stores new instance
>>>>>>> 9c6c762ac0b807d64026ceec308a75cd885238e5
>>>>>>> c438ae256c33bfdf7d9d305ebe433e8407b8e50d
        else:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        '''returns string representation'''
<<<<<<< HEAD
        name_of_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_of_class, self.id, self.__dict__)
=======
<<<<<<< HEAD
        return "[{}] ({}) {}".format

    def __init__(self):
        '''intializing values'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''returns string representation'''
        return "[{}] ({}) {}".format

        (self.__class__.__name__, self.id, self.__dict__)
=======
        name_of_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_of_class, self.id, self.__dict__)
>>>>>>> 9c6c762ac0b807d64026ceec308a75cd885238e5
>>>>>>> c438ae256c33bfdf7d9d305ebe433e8407b8e50d

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
