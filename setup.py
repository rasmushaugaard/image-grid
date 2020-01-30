import setuptools

with open("readme.md") as f:
    long_description = f.read()

setuptools.setup(
    name='image-grid',
    version='0.0.4',
    author='Rasmus Laurvig Haugaard',
    author_email='rasmus.l.haugaard@gmail.com',
    description='assembles images in a grid',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/RasmusHaugaard/image-grid',
    scripts=[
        'bin/image-grid',
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'Pillow',
        'natsort',
    ],
    python_requires='>=3.6',
)
