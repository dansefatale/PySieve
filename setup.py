from distutils.core import setup, Extension

_pysieve = Extension('_pysieve',
                    include_dirs = ['/opt/local/include/msieve'],
                    libraries = ['msieve', 'gmp'],
                    library_dirs = ['/opt/local/lib/'],
                    sources = ['pysieve.c'])

setup (name = 'pysieve',
       version = '0.0',
       description = 'prime factors',
       py_modules = ['pysieve'],
       ext_modules = [_pysieve])
