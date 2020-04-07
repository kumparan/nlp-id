from setuptools import setup

# Package details
setup(
  name='nlp_id',
  packages=['nlp_id'],
  version='0.1.9.2',
  license='MIT',
  description="Kumparan's NLP Services",
  long_description=open("README.md", "r").read(),
  long_description_content_type="text/markdown",
  author='Frandy Eddy',
  author_email='eddy.frandy@gmail.com',
  url='https://github.com/kumparan/nlp-id',
  keywords=['Indonesian', 'Bahasa', 'NLP'],
  package_data={
        '': ['data/*'],
    },
  install_requires=[
        "scikit-learn==0.22",
        "nltk==3.4.5",
        "wget==3.2"
    ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Text Processing :: Linguistic',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)