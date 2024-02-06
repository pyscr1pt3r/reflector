from setuptools import setup, find_packages

setup(
    name='refl',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
        'ratelimit',
        'urllib3'
    ],
    entry_points={
        'console_scripts': [
            'reflector = reflector.main:main'
        ]
    },
    url='https://github.com/pyscr1pt3r/refl',
    license='MIT',
    author='pyscr1pt3r',
    author_email='pyscr1pt3r@proton.me',
    description='Turn urls into profit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)