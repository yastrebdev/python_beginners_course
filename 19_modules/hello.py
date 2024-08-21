# import messages as msg
# from messages import hello, bye
import importlib
main = importlib.import_module('00_numbers.main')
from messages import *

# msg.hello()
# msg.bye()

hello()
bye()

# help('modules')

main.test()