from setuptools import setup, find_packages
setup(
    name = "stackoverflow",
    version = "0.1",
    packages = find_packages(),

    entry_points = {
        "console_scripts": [
            "stackoverflow = stackoverflow.so.py",
            "so = stackoverflow.so.py",
        ]
    }
)
