from setuptools import setup, find_packages

setup(name='otus-qa',
    version='0.1',
    url='https://github.com/Sokolov85/otus-qa-course',
    license='MIT',
    author='Sergey Sokolov',
    author_email='ssokolov85@gmail.com',
    description='Otus qa python code',
    packages=find_packages(exclude=['Docker', 'Jenkins']),
    long_description=open('README.md').read(),
    setup_requires=['pytest>=5.0.1'],
    zip_safe=False)
