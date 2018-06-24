from setuptools import setup, find_packages

setup(
    name='languagecodess',
    version='1.0.0',
    description="A library that normalises language codes",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programmsing Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='names languages iso ',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/alephdata/languagecodes',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[],
    entry_points={
    }
)