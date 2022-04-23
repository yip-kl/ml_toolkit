import setuptools

setuptools.setup(
    name='ml_toolkit',
    version='1.0',
    description='Toolkit for ML projects',
    url='https://github.com/yip-kl/ml_toolkit',
    packages=['ml_toolkit'],
    install_requires=['sklearn', 'matplotlib', 'google-cloud-storage', 'pandas', 'numpy']
    )