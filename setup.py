from setuptools import setup

setup(
    name='collage',
    version='0.0.1',
    scripts=[
        'bin/collage',
    ],
    install_requires=[
        'numpy',
        'Pillow',
    ],
)
