from setuptools import setup

setup(
    name = 'buildings_api',
    version = '0.1.0',
    description = 'An API about tall buildings',
    author = 'Brahm Lower',
    author_email = 'bplower@gmail.com',

    packages = ['buildings_api'],
    package_dir = {'buildings_api': 'src'},

    install_requires = [
        'falcon',
        'PyYAML',
        'sqlalchemy',
        'psycopg2-binary'
    ],
    entry_points = {
        'console_scripts': [
            'buildings-api=buildings_api:main'
        ]
    }
)