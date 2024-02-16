from logging import *

basicConfig( filename= 'add.log',
             level=10,
             filemode='w',
             format='{asctime}--{message}:{levelname}:{name}__{lineno}:{process}',
             datefmt='%d-%b-%y %H/%M/%S',
             style='{'

)
logging = getLogger('__name__')