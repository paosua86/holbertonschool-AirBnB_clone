#!/usr/bin/python3
""" BaseModel """


from datetime import datetime
import uuid
import models


class BaseModel():
    """ BaseModel Class for future classes"""

    def __init__(self, *args, **kwargs):
        """ Initialize objects """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                    (value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation """
        dic = dict(self.__dict__)
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, dic)

    def save(self):
        """ Update and save object """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return directory """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = datetime.isoformat(dic['created_at'])
        dic['updated_at'] = datetime.isoformat(dic['updated_at'])
        return dic
