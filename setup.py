import setuptools

setuptools.setup(
    name='pwgen',
    version='0.1',
    description='Secure but easy-to-remember passwords.',
    author='Charles D. Holmes',
    author_email='charles.d.holmes@gmail.com',
    py_modules=['pwgen'],
    entry_points={'console_scripts': ['pwgen = pwgen:main']}
    )
