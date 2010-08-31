from distutils.core import setup, Extension

_pysieve = Extension('_pysieve',
                    include_dirs = ['/opt/local/include/msieve'],
                    libraries = ['msieve', 'gmp'],
                    library_dirs = ['/opt/local/lib/'],
                    sources = ['pysieve.c'])

setup (name = 'pysieve',
       version = '0.01a',
       description = 'Fast prime factorization using the msieve library',
       py_modules = ['pysieve'],
       ext_modules = [_pysieve])
