from setuptools import setup

# read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='zeromessage',
      version='0.2',
      description='Lightweight ROS-like pub-sub tool utilizing ZeroMQ',
      url='https://github.com/yodahuang/zero-message',
      author='Yanda Huang',
      author_email='yord.huang@gmail.com',
      license='MIT',
      packages=['zeromessage'],
      install_requires=[
            'zmq',
            'fire'
      ],
      entry_points= {
            'console_scripts': ['zerotopic=zeromessage.utils.zerotopic:main']
      },
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown'
)