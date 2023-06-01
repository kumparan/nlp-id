from setuptools import setup

# Package details
setup(
    name="nlp_id",
    packages=["nlp_id"],
    version="0.1.14.0",
    license="MIT",
    description="Kumparan's NLP Services",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Frandy Eddy, Dhanang Hadhi Sasmita, Zavli Juwantara",
    author_email="eddy.frandy@gmail.com, dhananghadhi@gmail.com, juwantaraz@gmail.com",
    url="https://github.com/kumparan/nlp-id",
    keywords=["Indonesian", "Bahasa", "NLP"],
    package_data={
        "": ["data/*"],
    },
    install_requires=["scikit-learn==1.2.2", "nltk==3.8.1", "wget==3.2", "pytest==7.3.1"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
