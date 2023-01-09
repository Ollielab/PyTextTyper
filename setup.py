import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTypeWriter-CoolOllie2", # Replace with your own username
    version="0.0.1",
    author="Ollielab",
    author_email="mail@ollielab.xyz",
    description="Python typewriter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/driscollis/arithmetic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)