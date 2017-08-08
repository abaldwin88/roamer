from distutils.core import setup
version = '0.1.1'
setup(
  name = 'roamer',
  packages = ['roamer'],
  version = version,
  description = 'Plain Text File Explorer',
  author = 'Alex Baldwin',
  author_email = 'abaldwintech+hub@gmail.com',
  url = 'https://github.com/abaldwin88/roamer',
  download_url = 'https://github.com/abaldwin88/roamer/archive/v%s.zip' % version,
  keywords = ['explorer', 'plain text', 'directory'], # arbitrary keywords
  classifiers = [],
  scripts=['bin/roamer'],
)
