import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="PyTextWriter",
    version="0.2",
    author="Ollielab",
    author_email="mail@ollielab.xyz",
    description="Python text engine which prints text to the console complete with animations, colors, and ASCII art!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ollielab/PyTextWriter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)