try:
	from project.settings.base import *
	from project.settings.secrets import *
except ImportError:
    pass

DEBUG = False


