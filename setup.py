try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='pykakao',
    description='Simple KakaoTalk LOCO/HTTP API protocol wrapper',
    version='0.1.0',
    py_modules=['pykakao'],
    install_requires=[
        'pymongo>=2.6.3',
        'pycrypto>=2.6.1',
        'rsa>=3.1.2',
    ],
    author='ltj0507',
    author_email='ltj0507@naver.com',
    license='MIT',
    url='https://github.com/spargesoft/pykakao',
)
