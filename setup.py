from setuptools import setup, find_packages

setup(
    name="file-type-identifier",
    version="1.0.0",
    description="Identify file types via magic bytes, extensions, and MIME types",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/yourusername/file-type-identifier",
    license="MIT",
    python_requires=">=3.9",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    py_modules=["identifier", "cli"],
    entry_points={
        "console_scripts": [
            "filetype=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Environment :: Console",
    ],
)
