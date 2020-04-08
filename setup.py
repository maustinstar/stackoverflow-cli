from setuptools import setup, find_packages
setup(
    name = "stackoverflow",
    version = "0.1",
    packages = find_packages(),

    install_requires = [
        "requests>=2.23.0",
        "beautifulsoup4>=4.9.0",
    ],

    entry_points = {
        "console_scripts": [
            "stackoverflow = stackoverflow.so.py",
            "so = stackoverflow.so.py",
        ]
    }
)
