import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='outrageclf',
      version='0.1.6',
      description='Outrage Classifier - developed by the Crockett Lab',
      long_description=README,
      url='https://github.com/CrockettLab/outrage_classifier',
      install_requires=[
            'emoji==1.6.3',
            'joblib',
            'keras==2.8.0',
            'nltk',
            'numpy==1.26.4',
            'scikit-learn',
            'tensorflow==2.8.0',
            'protobuf==3.20.0'
      ],
      author='Tuan Nguyen Doan',
      author_email='tuan.nguyen.doan@aya.yale.edu',
      license='Creative Commons Attribution-NonCommercial-ShareAlike 2.0',
      packages=['outrageclf'],
      include_package_data=True,
      zip_safe=False)
