import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

dev_requires = [
    'build==0.5.1',
    'twine>=3.4.2,<4',
    'pip-tools>=5,<6',
    'pytest>=6.2.4,<6.3'
]

setuptools.setup(
    name="openpyutils",
    version="0.0.4",
    author="YiXiaoCuoHuaiFenZi",
    author_email="249664317@qq.com",
    description="open source of python utils.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YiXiaoCuoHuaiFenZi/OpenPyUtils",
    project_urls={
        "Bug Tracker": "https://github.com/YiXiaoCuoHuaiFenZi/OpenPyUtils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    extras_require={
        "dev": dev_requires
    },
)
