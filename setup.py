import setuptools


def requirements():
    try:
        with open('requirements.txt') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        return ''


setuptools.setup(
    name='pwgen',
    version='0.1',
    description='Secure but easy-to-remember passwords.',
    author='Charles D. Holmes',
    author_email='charles.d.holmes@gmail.com',
    url='https://github.com/holmescharles/pwgen',
    py_modules=['pwgen'],
    entry_points={'console_scripts': ['pwgen = pwgen:main']},
    install_requires=requirements(),
    )
