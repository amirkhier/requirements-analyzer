import logging

#configuration
logging.basicConfig(level=logging.INFO , filename="log.log", filemode = 'w',format="%(asctime)s - %(levelname)s - %(message)s")



# levels of logging
# logging.debug("debug") # first
# logging.info("info") # second
# logging.warning("warning") # third
# logging.error("error") # fourth
# logging.critical("critical") # fifth

# Let's get started :
# Lets' try
x = 2
# in configuration if you define the level debug , you can run also the rest of levels such as info,warning,error,critical
#this happnens because the debug is the first level
logging.debug(f"The value X is {x}")
# but if you define in levels info ,btw the info is second level , logging.info(f"The value X is {x}") only works and not debug
logging.info(f"The value X is {x}")


# Logging Exception:
try:
  1/0
except ZeroDivisionError as e:
  # exc_info is an argument not as parameter
  # if you remove exc_info you only see the output in log file 
  # with exc_info you see like :
  # Traceback (most recent call last):
  # File "C:\Users\user\basic_agent\loggingTutorial.py", line 27, in <module>
  #   1/0
    # ~^~
  logging.error("ZeroDivisionError")
  # you can use instead logging.error("ZeroDivisionError",exc_info=True)
  #you can use instead this :
  logging.exception("ZeroDivisionError")
  logging.exception("test")







