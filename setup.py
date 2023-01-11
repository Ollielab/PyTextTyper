import setuptools

MINIMAL_DESCRIPTION = '''PyTextTyper is a text engine written in python which prints text to the console, fully complete with animations, colors, and ASCII art!'''

def long_description():
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        return description
    except Exception:
        return MINIMAL_DESCRIPTION

setuptools.setup(
    name="PyTextTyper",
    version="0.4.6",
    author="Ollielab",
    author_email="mail@ollielab.xyz",
    description="PyTextTyper is a text engine written in python which prints text to the console, fully complete with animations, colors, and ASCII art!",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ollielab/PyTextTyper",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    include_package_data=True
)



