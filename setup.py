from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Tools to help build, analyze, and stress test portfolios'

# Setting up
setup(
        name="asset-allocation", 
        version=VERSION,
        author="Ben McDonald",
        author_email="benmcdnld@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'finance', 'portfolio', 'asset allocation'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Finance",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)