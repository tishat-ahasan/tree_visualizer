from setuptools import setup, find_packages

setup(
    name="viewtree",
    version="0.1.0",
    description="A package to visualize binary trees using Graphviz.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="ext.md.khaliduzzaman@bracu.ac.bd",
    url="https://github.com/isaamrat/tree_visualizer",
    packages=find_packages(),
    install_requires=[
        "graphviz",
        "ipython"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
