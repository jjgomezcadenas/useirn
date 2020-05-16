from setuptools import setup
from Cython.Build import cythonize
from os import path
from subprocess import check_output
import numpy
numpy_include = path.join(path.dirname(numpy.__file__), 'core/include')



setup(name         = 'useirn',
      version      = '0.1',
      description  = 'useir numerical solvers',
      url          = 'https://github.com/jjgomezcadenas/useirn',
      author       = 'useir collaboration',
      author_email = 'jjgomezcadenas@gmail.com',
      license      = 'BEER_ware',
      packages     = ['useir'],
      ext_modules  = cythonize('useir/*.pyx'),
      include_dirs = [numpy_include],
)
