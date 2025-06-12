from setuptools import setup, find_packages

setup(
    name="uscg_leetcode_validator",
    version="1.1.0",
    packages=find_packages(),
    author="toog",
    description="cmd injection.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'uscg-leetcode-validator=uscg_leetcode_validator.main:main',
        ],
    },
)
