import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="PyTypeWriter",
    version="0.1",
    author="Ollielab",
    author_email="mail@ollielab.xyz",
    description="Python text engine with animations, colors and ASCII art!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ollielab/PyTypeWriter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)