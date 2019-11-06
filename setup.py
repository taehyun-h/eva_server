import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='eva',
      version='0.1',
      description='This application is server for eva',
      long_description=long_description(),
      url='https://github.com/taehyun-h/eva_server',
      author='taehyun-h',
      author_email='taehyun95@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False)
