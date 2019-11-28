from setuptools import setup
import roamer
setup(
  name = 'roamer',
  packages = ['roamer'],
  version = roamer.__version__,
  description = 'Plain Text File Explorer',
  author = 'Alex Baldwin',
  author_email = 'abaldwintech+hub@gmail.com',
  url = 'https://github.com/abaldwin88/roamer',
  download_url = 'https://github.com/abaldwin88/roamer/archive/v%s.zip' % roamer.__version__,
  keywords = ['explorer', 'plain text', 'directory'], # arbitrary keywords
  classifiers = [],
  install_requires=['click>=7.0'],
  entry_points='''
        [console_scripts]
        roamer=roamer.main:start
  ''',
)
