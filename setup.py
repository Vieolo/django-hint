import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-hint",
    version="0.0.1",
    author="Vieolo OÜ",
    author_email="info@vieolo.com",
    description="Typehinting package for django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vieolo/django-hint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
)
