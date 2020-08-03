from setuptools import setup
from setuptools import find_packages


setup(name='shuffle-big-file',
      version='0.0.1',
      description='Shuffle a big file that does not fit in memory',
      author='YaYaB',
      author_email='bezzayassine@gmail.com',
      url='https://github.com/YaYaB/shuffle-big-file',
      download_url='https://github.com/YaYaB/shuffle-big-file',
      license='MIT',
      classifiers=['License :: MIT License',
                   'Programming Language :: Python',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   ],
      install_requires=[],
      extras_require={},
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'shuffle-big-file=shuffle_big_file.shuffle_big_file:shuffle_big_file_cli',
              'generate-random-file=shuffle_big_file.shuffle_big_file:generate_random_file_cli'
          ]},

)