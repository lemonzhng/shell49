from setuptools import setup
import sys

if sys.version_info < (3,4):
    print('shell49 requires Python 3.4 or newer.')
    sys.exit(1)

from shell49.version import __version__

# Platform dependinent dependencies:
#   OSX:   gnureadline
#   Win:   pyreadline
install_req=[
    'pyserial >= 2.0',
    'zeroconf >= 0.19'
]
if sys.platform == 'darwin':
    install_req.append('gnureadline')
if sys.platform == 'win32':
    install_req.append('pyreadline')

setup(
  name = 'shell49',
  packages = ['shell49', 'lib', 'lib/do'],
  version = __version__,
  description = 'Micropython remote shell',
  long_description = 'see https://github.com/bboser/shell49',
  license = 'MIT',
  author = 'Bernhard Boser',
  author_email = 'boser@berkeley.edu',
  url = 'https://github.com/bboser/shell49',
  keywords = ['micropython', 'shell', 'shell49'],
  classifiers = [
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Embedded Systems',
      'Topic :: System :: Shells',
      'Topic :: Terminals :: Serial',
      'Topic :: Utilities',
  ],
  install_requires=install_req,
  entry_points = {
      'console_scripts': [
          'shell49=shell49.command_line:main',
          'shell49edge=lib.main:main'
      ],
  },
)
