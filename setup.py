from distutils.core import setup, Extension

module1 = Extension('pysieve',
                    include_dirs = ['/opt/local/include/msieve'],
                    libraries = ['msieve', 'gmp'],
                    library_dirs = ['/opt/local/lib/'],
                    sources = ['pysieve.c'])

setup (name = 'pysieve',
       version = '0.0',
       description = 'prime factors',
       ext_modules = [module1])
