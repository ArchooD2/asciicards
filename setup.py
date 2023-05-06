import setuptools
long_desc = open("README.md").read()
required = [<Dependent Packages>] # Comma seperated dependent libraries name
setuptools.setup(
    name="asciicards",
    version="0.0.1", # eg:1.0.0
    author="PaperJam",
    author_email="none :(",
    license="GNU General Public License v3.0",
    description="ascii card library",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/ArchooD2/asciicards",
    packages = ['asciicards'],
    # project_urls is optional
    project_urls={
        "Bug Tracker": "<BUG_TRACKER_URL>",
    },
    key_words="<KEY WORDS>",
    install_requires=required,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
