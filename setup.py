from distutils.core import setup, Extension

module1 = Extension('_pysieve',
                    include_dirs = ['/opt/local/include/msieve'],
                    libraries = ['msieve', 'gmp'],
                    library_dirs = ['/opt/local/lib/'],
                    sources = ['pysieve.c'])

setup (name = '_pysieve',
       version = '0.0',
       description = 'prime factors',
       ext_modules = [module1])
