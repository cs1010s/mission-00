from setuptools import setup, find_packages

setup_args = dict(
    name='mission00',
    version='1.0',
    description='Package setup for Mission 0',
    packages=find_packages(),
    author='Russell Saerang',
    install_requires = [
        'pillow',
        'seaborn',
        'scipy',
        'cocos2d @ https://github.com/cs1010s/cocos/releases/download/2220/cocos.zip'
    ],
)

if __name__ == '__main__':
    setup(**setup_args, include_package_data=True)