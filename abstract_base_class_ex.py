from abc import ABC, abstractmethod
import json
import pickle


class FileSerdeHandler(ABC):

    def __init__(self,filename):
        self.filename=filename

    @abstractmethod
    def serialize(self,data):
        pass

    @abstractmethod
    def deserialize(self,data):
        pass

    def write(self,data):
        with open(self.filename,'wb') as f: # WB option will write as bytes expects byte stream instead of string which is needed in 'w'
            f.write(self.serialize(data))

    def read(self):
        with open(self.filename,'rb') as f:
            return self.deserialize(f.read())

class JSONFileSerdeHandler(FileSerdeHandler):

    # NO INIT SUPER WAS NEEDED IN THIS CASE SINCE WE ARE NOT ADDING ANY NEW PARAM in child
    # THUS IT WILL BEYDEFAULT NEED ONLY FILENAME WHICH IS NEEDED BY PARENT!

    #IMPLEMENTATION OF ABSTRACT METHODS FOR JSON FILES
    def serialize(self,data):
        return json.dumps(data).encode('utf-8') # .encode converts json string further to byte stream!

    def deserialize(self,data):
        return json.loads(data.decode('utf-8'))

class PickleFileSerdeHandler(FileSerdeHandler):

    #IMPLEMENTATION OF ABSTRACT METHODS FOR PICKLE FILES
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, data):
        return pickle.loads(data)


if __name__ == "__main__":
    # ABCs CANNOT BE Instantiated directly we need to implement abstract methods in sub classes first
    # file1 = FileSerdeHandler('abc.txt')
    #Traceback (most recent call last):
    #   File "/Users/sanchitgawde/PycharmProjects/Python_OOPS/abstract_base_class_ex.py", line 26, in <module>
    #     file1 = FileSerdeHandler('abc.txt')
    # TypeError: Can't instantiate abstract class FileSerdeHandler with abstract methods deserialize, serialize

    data = dict(name="Sanchit",age=24)
    json_file = JSONFileSerdeHandler('data.json')
    pickle_file = PickleFileSerdeHandler('data.pickle')
    json_file.write(data)
    print(json_file.read())
    pickle_file.write(data)
    print(pickle_file.read())