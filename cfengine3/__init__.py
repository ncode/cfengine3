__version__ = '0.0.2'
VERSION = tuple(map(int, __version__.split('.')))
__all__ = ['cfengine3']
__author__ = 'Juliano Martinez <juliano@martinez.io>'

class protocol(object):

    __valid_actions__ = {'define': '+', 'undefine': '-'}

    def classes(self, name, action):
        if not action in self.__valid_actions__:
            raise LookupError('Action must be define or undefine')
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        print "%s%s" % (self.__valid_actions__[action], name)

    def scalar(self, name, value):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not isinstance(value, str):
            raise TypeError('Value must be a string')
        print "=%s=%s" % (name, value)

    def list(self, name, value):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not isinstance(value, list):
            raise TypeError('Value must be a list')
        print '@%s= { "%s" }' % (name, '", "'.join(value))
