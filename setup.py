from setuptools import setup

setup(name='zero_message',
      version='0.1',
      description='Lightweight ROS-like pub-sub tool utilizing ØMQ',
      url='https://github.com/yodahuang/zero-message',
      author='Yanda Huang',
      author_email='yord.huang@gmail.com',
      license='MIT',
      packages=['zero_message'],
      install_requires=[
            'zmq',
            'fire'
      ],
      entry_points= {
            'console_scripts': ['zerotopic=zero_message.utils.zerotopic:main']
      },
      zip_safe=False)