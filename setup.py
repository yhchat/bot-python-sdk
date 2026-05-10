import setuptools 
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="yunhu", 
    version="0.0.12",
    author="yunhu",  
    description="云湖官方Python SDK",
    author_email="support@jwzhd.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.25.0',
        'httpx>=0.23.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', #对python的最低版本要求
)