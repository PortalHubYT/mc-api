import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mc_api",
    version="0.0.1",
    author="PortalHubYT, cyclotruc",
    author_email="portalhub.business@gmail.com",
    description="A minecraft API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PortalHubYT/mc_api",
    project_urls={
        "Bug Tracker": "https://github.com/PortalHubYT/mc_api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "mc_api"},
    packages=setuptools.find_packages(where="mc_api"),
    python_requires=">=3.6",
)