from setuptools import setup

setup(name='csvfilecleaner',
      version='0.1',
      description='A very simple utility class for cleaning csv files',
      keywords='csv clean file',
      url='',
      author='Alessandro Calefati',
      author_email='caleale90@gmail.com',
      license='MIT',
      packages=['csvfilecleaner'],
      install_requires=[
          'copyfile'

      ],
      include_package_data=True,
      zip_safe=False)

