from setuptools import setup, find_packages

setup(
    name = "granroyale",
    version = "0.1",
    url = 'http://granroyalebicycles.com',
    description = "Gran Royale Bikes website",
    author = 'doigoid',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = [
        'setuptools',
        'pysqlite',
        'MySQL-python',
        'South',
        'simplejson',
        'django-imagekit',
    ],
)
