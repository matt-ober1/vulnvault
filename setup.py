from setuptools import setup, find_packages

setup(
    name='vulnvault',
    version='0.1.0',
    description='Search for Vulnerabilities using the VulDB API',
    long_description=open('README.md').read(),  # Optional: Add a README file for better documentation
    long_description_content_type='text/markdown',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    license='GPL-3.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'vulnvault=vulnvault:main',  # Change this according to your main function location
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPL-3.0)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
