"""Summary
"""
import os
import unittest
import pickle

def check_file(file):
    """Summary
    
    Args:
        file (str): filename for model
    
    Raises:
        ValueError: Wrong Type
    """
    if isinstance(file,str):
        raise ValueError('Некорректные данные')


class PickleWorker:

    """Summary
    """
    
    def __init__(self,file):
        """Summary
        
        Args:
            file (str): filename for model
        """
        check_file(file)
        self.__file = file
        if not os.path.exists(file):
            self.write_to_file([])


    def read_from_file(self):
        """Summary
        
        Returns:
            obj: get model from file
        """
        with open(self.__file,'rb') as f:
            return pickle.loads(f.read())

    def write_to_file(self,data):
        """Summary
        
        Args:
            data (obj): model for writing
        
        Returns:
            obj: put model to file
        """
        with open(self.__file,'wb') as f:
            return f.write(pickle.dumps(data))


class Table:

    """Summary
    """
    
    def __init__(self,model,file):
        """Summary
        
        Args:
            model (obj): object of class Table
            file (str): file for saving
        """
        self.__model = model
        self.__FileWorker = PickleWorker(file)
            
    def save(self,model_object):
        """Summary
        
        Args:
            model_object (obj): 
        
        Raises:
            ValueError: wrong type
        """
        if type(model_object) != self.__model:
            raise ValueError('Некорректный тип')
        data = self.__FileWorker.read_from_file() 
        data.append(model_object)
        write_to_file(data,self.file)
        
    def list_all(self):
          """Summary
          
          Returns:
              list: list of objects
          """
          return self.__FileWorker.read_from_file() 

    def read(self,number):
        """Summary
        
        Args:
            number (int): model which you choose
        
        Returns:
            obj:  object that you choose from list
        """
        data = self.__FileWorker.read_from_file()
        return data[number]
    
    def update(self,number,new_params): 
        """Summary
        
        Args:
            number (int): model which you choose
            new_params (str): new fields for obj
        """
        data = self.__FileWorker.read_from_file()
        table_object = data[number]
        table_object.__dict__.update(new_params)
        self.__FileWorker.write_to_file(data)
        
    def delete(self,number):
        """Summary
        
        Args:
            number (int): model which you choose
        """
        data = self.__FileWorker.read_from_file()
        del data[number]
        self.__FileWorker.write_to_file(data)



class TestInitPickleWorker(unittest.TestCase):

    """Testing
    """
    
    def test_empty(self):
        """Summary
        """
        self.assertRaises(Exception, PickleWorker)

    def test_uncorrert1(self):
        """Summary
        """
        self.assertRaises(ValueError, PickleWorker,1)

    def test_uncorrert2(self):
        """Summary
        """
        self.assertRaises(ValueError, PickleWorker,[])

    def test_uncorrert3(self):
        """Summary
        """
        self.assertRaises(ValueError, PickleWorker,{})
    
if __name__ == '__main__':
    unittest.main()

    
