import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="counter-stats",
    version="0.0.1",
    author="Albert Pang",
    author_email="alpaaccount@mac.com",
    description="Python module for various Counter class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alpaalpa/counter-stats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "hiredis",
        "munch",
        "redis"
    ]
)
