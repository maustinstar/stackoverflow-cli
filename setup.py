from setuptools import setup, find_packages

setup(
    name = "stackoverflow",
    version = "0.1.3",
    packages = find_packages(),

    install_requires = [
        "requests>=2.23.0",
        "beautifulsoup4>=4.9.0",
    ],

    entry_points = {
        "console_scripts": [
            "stackoverflow = stackoverflow.so:main",
            "so = stackoverflow.so:main",
        ]
    },

    # metadata
    author= "Michael Verges",
    description= "Browse Stackoverflow from your command line.",
    keywords= "browse stack overflow stackoverflow",
    url = "https://github.com/maustinstar/stackoverflow-cli",
    project_urls={
        "Bug Tracker": "https://github.com/maustinstar/stackoverflow-cli",
        "Source Code": "https://github.com/maustinstar/stackoverflow-cli/issues",
    }
)
