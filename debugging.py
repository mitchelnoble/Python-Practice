#Python Debugging

#Stack Trace: when an exception occurs, shows the file, line number, and call stack

#Logging: a module that helps to record errors and program state

import logging
logging.basicConfig(level=logging.ERROR)
logging.error("An error occured.")

#Debuggers: a tool called "pdb" (Python Debugger) allows stepping through code to inspect variables

import pdb; pdb.set_trace()

