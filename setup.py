from setuptools import find_packages, setup


setup(
    name="penn_labs_pre_commit_mirrors",
    version="0.0.0",
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["detect-private-key=custom_hooks.detect_private_key:main"]},
    install_requires=[
        "isort==4.3.21",
        "black==19.3b0",
        "flake8==3.7.9",
        "flake8-isort==2.7.0",
        "flake8-quotes==2.1.1",
    ],
)
