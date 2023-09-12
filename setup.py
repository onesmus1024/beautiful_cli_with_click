from setuptools import setup



setup(
    name='beautiful_cli_with_click',
    version='0.1',
    py_modules=['beautiful_cli_with_click'],
    install_requires=[
        'Click',
    ],
    entry_points='''

        [console_scripts]
        ones_cli = init:hello
    ''',
)


# Run the following command to install the package:
# $ pip install --editable .
#
# Run the following command to run the script:
# $ beautiful_cli_with_click --count=3 --name=John
# Hello John!
# Hello John!
# Hello John!
