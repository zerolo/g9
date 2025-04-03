from setuptools import setup, find_namespace_packages

setup(
    name="g9_api_client",
    version="0.0.2",
    python_requires='>=3',
    package_dir={'': '.'},
    packages=find_namespace_packages(where='.'),
    install_requires=[
        "httpx>=0.24.0",
    ]
)
