from setuptools import setup

with open("readme.md") as f:
    long_description = f.read()

setup(
    name='image-grid',
    version='0.0.2',
    author='Rasmus Laurvig Haugaard',
    author_email='rasmus.l.haugaard@gmail.com',
    description='assembles images in a grid',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/RasmusHaugaard/image-grid',
    scripts=[
        'bin/image-grid',
    ],
    install_requires=[
        'numpy',
        'Pillow',
        'natsort',
    ],
    python_requires='>=3.6',
)
