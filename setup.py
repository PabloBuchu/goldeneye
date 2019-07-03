import setuptools

from goldeneye import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="goldeneye",
    version=VERSION,
    author="Pawel Buchowski",
    author_email="pawel.buchowski@netguru.com",
    description="A wanna be all-purpose prometheus metrics exporter for WSGI based apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PabloBuchu/goldeneye",
    packages=setuptools.find_packages(),
    install_requires=['prometheus_client', 'werkzeug', 'objgraph'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)