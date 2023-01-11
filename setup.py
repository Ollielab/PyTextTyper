import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="PyTextTyper",
    version="0.4.3",
    author="Ollielab",
    author_email="mail@ollielab.xyz",
    description="PyTextTyper is a text engine written in python which prints text to the console, fully complete with animations, colors, and ASCII art!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ollielab/PyTextTyper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)