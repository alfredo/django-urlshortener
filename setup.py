from setuptools import setup, find_packages

setup(
    name = "django-urlshortener",
    version = "0.1alpha",
    url = 'https://github.com/alfredo/django-urlshortener',
    license = 'BSD',
    description = "URL shortener",
    author = 'Alfredo Ramirez',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
