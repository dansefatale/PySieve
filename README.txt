==========================================
Pysieve -- fast prime factoring for python
==========================================

Pysieve is a simple wrapper of the msieve prime factorization library.
It basically gives you a fast factor command and some utilities.

For now it is only tested on OSX with python 2.6 and msieve146 but it
should work on Linux as well.  It assumes that the msieve library is
installed in a standard location (i.e /usr/local/lib, /usr/lib or on
OSX with macports /opt/local/lib)

Functions in the package
========================

* factor(n): returns a list of the prime factors of n

* dfactor(n): returns a list of distinct prime factors of n (no
  duplicates)

* facExponents(n): returns a list of tuples, each containing a prime
  factor of n and its exponent

TODO 
==== 
* _pysieve is installed as seperate package. I somehow can't
	define it to be a subpackage of pysieve (like pysieve._pysieve)


Credits
=======

The msieve library can be downloaded at
http://sourceforge.net/projects/msieve/

