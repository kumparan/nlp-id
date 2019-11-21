from distutils.core import setup

# Package details
setup(
  name = 'nlp_id',
  packages = ['nlp_id'],
  version = '0.1.0',
  license='MIT',
  description = "Kumparan's NLP Services",
  author = 'Frandy Eddy',
  author_email = 'eddy.frandy@gmail.com',
  url = 'https://github.com/kumparan/nlp-id',
  keywords = ['Indonesian', 'Bahasa', 'NLP'],
  package_data={
        '': ['data/*'],
    },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Text Processing :: Linguistic',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)