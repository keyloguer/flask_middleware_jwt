from setuptools import setup

setup(
    name='flask_middleware_jwt',
    version='1.0',
    author='Daniel Pereira Zitei, Carla de Almeida Madureira',
    author_email='daniel.zitei@gmail.com, carla.almadureira@gmail.com',
    packages=['flask_middleware_jwt'],
    description="This is a middleware for jwt",
    url='https://github.com/keyloguer/flask_middleware',
    install_requires=['pyjwt', 'requests', 'flask']
)