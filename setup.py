import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_hint",
    version="0.2.0",
    author="Vieolo OÜ",
    author_email="info@vieolo.com",
    description="Type hinting package for django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vieolo/django-hint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
