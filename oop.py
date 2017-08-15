class ClassName(Object):
    ''' A class ClassName that inherits from class Object '''

    a_class_attribute = 10

    def __init__(self, *args):
        ''' Constructor '''
        self.attr1 = args[0]
        self.attr2 = args[1:]
        self._weak_hidden_attr = args[2]		# Can be accessed by using instace._weak_hidden_attr
        self.__strong_hidden_attr = args[3]		# Can be accessed by using _ClassName__strong_hidden_attr
        # super().__init__(args)

    def __repr__(self):
        ''' A basic description of a class object '''
        return 'Object of class {}; with these parameters {}'.format(self.__name__, self.__dir__)

    def __str__(self):
        ''' String representation of object (Called with print() or when typecasted to String) '''
        return '[{0}, {1}]'.format(self.attr1, self.arg2)

    @classmethod
    def new_object(cls, arg):
        ''' Called by using Class, rather than class instance; Can act as a second Constructor '''
        return cls(arg, arg)

    @staticmethod
    def some_method(arg1):
        ''' Static, belong to class; no self/cls argument '''
        if arg1 == 'this':
            return 'this'
        else:
            return 'that'

    @property
    def is_this_allowed(self):
        ''' Used to make an attribute 'Read-Only' '''
        return True

    @property
    def weak_hidden_arg(self):
        ''' Another use is to provide access to weakly hidden attribute; acts as getter '''
        return self._weak_hidden_arg

    @weak_hidden_arg.setter
    def weak_hidden_arg(self, value):
        ''' This method acts as the setter '''
        some_threshold = 10
        if value < some_threshold:
            self._weak_hidden_arg = value
        else:
            # raise ValueError('Value above threshold')
            return

    def normal_method(self):
        ''' A normal method '''
        print('Doing Something')

    def __len__(self):
        ''' Magic method for len() '''
        return len(self.__dict__)

    def __iter__(self):
        ''' Magic method to return an iterator for class instance;
            Can also define __next__ method to decide which attributes to yield
        '''
        for i in self.attr2:
            yield i


'''
A number of magic methods:
__add__: to overload '+' for class instances; also __radd__
__iadd__: to overload '+='
__sub__: '-', __mul__: '*', __truediv__: '/', __floordiv__: '//'
__lt__, __le__, __eq__, __ne__, __gt__, __ge__: <, <=, ==, !=, >, >=

__getitem__, __setitem__, __delitem__, __contains__

'''
