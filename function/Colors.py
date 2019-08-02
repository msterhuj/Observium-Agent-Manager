class Colors(object):

    def __init__(self, arg):
        super(Colors, self).__init__()
        self.arg = arg


    def red():
        return '\033[0;31m'


    def green():
        return '\033[0;32m'


    def yellow():
        return '\033[1;33m'


    def reset(arg):
        return '\033[0m'
