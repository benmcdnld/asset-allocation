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
        install_requires=[
            'pip install requests==2.28.0',
            'pip install numpy==1.22.4',
            'pip install pandas==1.4.2',
            'pip install matplotlib==3.5.2',
            'pip install seaborn==0.11.2',
            'pip install lxml==4.9.0',
            'pip install openpyxl==3.0.10',
            'pip install statsmodels==0.13.2',
            'pip install sklearn==1.1.1',
            'pip install bs4==4.11.1',
            'pip install pyportfolioopt==1.5.3'
        ], 
        keywords=['python', 'finance', 'portfolio', 'asset allocation'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Finance",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)