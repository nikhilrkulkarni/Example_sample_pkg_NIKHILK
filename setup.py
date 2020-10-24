import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="example-pkg-NIKHILK",
        version="0.0.1",
        author="Nikhil Kulkarni",
        authon_email="nikhilkulkarni4013@gmail.com",
        description="A small example package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/pypa/sampleproject",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",           
            ],
        python_requires='>=3.6',
        )
