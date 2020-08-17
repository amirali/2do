from setuptools import setup

setup(
    name = 'twodo',
    version = '1',
    description = 'Yet another simple todo cli in Python',
    author = 'Amirali Esfandiari',
    author_email = 'amiralinull@gmail.com',
    url = 'https://github.com/realamirali/twodo',
    py_modules = ['twodo'],
    install_requires = ['fire'],
    packages = ['twodo'],
    package_dir = {'twodo': 'twodo'},
    python_requires = '>=3',
    classifiers = [
        'License :: OSI Approved :: MIT License',
    ],
    entry_points = '''
        [console_scripts]
        2do=twodo.cli:main
    '''
)
