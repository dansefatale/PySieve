from distutils.core import setup, Extension
import os.path


# Look for the msieve lib and header 
# Currently only for Unix
libpaths = ['/usr/local/lib', '/usr/lib','/opt/local/lib']
includepaths = ['/usr/local/include', '/usr/include', '/opt/local/include']

libpath = []
for p in libpaths:
    if os.path.exists(os.path.join(p, 'libmsieve.a')):
        libpath.append(p)
    
    if os.path.exists(os.path.join(p, 'libgmp.a')):
        libpath.append(p)

# remove duplicates:
libpath = list(set(libpath))


includepath = []
for p in includepaths:
    if os.path.exists(os.path.join(p, 'msieve/msieve.h')):
        includepath.append( os.path.join(p, 'msieve'))
        break
    elif os.path.exists(os.path.join(p, 'msieve.h')):
        includepath.append(p)
        break



# setup
extension1 = Extension('_pysieve',
                    include_dirs = includepath,
                    libraries = ['msieve', 'gmp'],
                    library_dirs = libpath,
                    sources = ['pysieve/pysieve.c'])

setup (name = 'PySieve',
       version = '0.5.1',
       packages=['pysieve'],
       ext_modules = [extension1],
       author = 'Severin Bannert',
       author_email = 'severin.bannert@gmail.com',
       url = 'http://github.com/dansefatale/PySieve',
       description = 'Fast prime factorization using the msieve library',
       long_description = open('README.txt').read(),
       classifiers = ['Topic :: Scientific/Engineering :: Mathematics', 
                      'Intended Audience :: Science/Research', 
                      'Programming Language :: C'])


