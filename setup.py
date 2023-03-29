from setuptools import setup, find_packages

setup(
    name='codeaidkit',
    version='0.1.0',
    description='A comprehensive Python package for analyzing and improving code quality',
    author='Payton Webber',
    author_email='paytonwebber@gmail.com',
    url='https://github.com/PaytonWebber/CodeAidKit',
    packages=find_packages(),
    install_requires=[
        'pycodestyle',
        'radon',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)