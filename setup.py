from setuptools import find_packages, setup


setup(
    name="penn_labs_pre_commit_mirrors",
    version="0.0.0",
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["detect-private-key=custom_hooks.detect_private_key:main"]},
    install_requires=[
        "isort==5.13.2",
        "black==24.3.0",
        "flake8==6.1.0",
        "flake8-isort==6.1.0",
        "flake8-quotes==3.3.2",
        "click==8.0.2"
    ],
)
