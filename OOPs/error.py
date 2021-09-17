import sys
import logging

logging.basicConfig(filename = "error_log.log",level = logging.ERROR)
try:
    a+b
except Exception as e:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
    print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno))
    

def error_handling():
    return '{}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno)

try:
    a+b
except:
    logging.error(error_handling())