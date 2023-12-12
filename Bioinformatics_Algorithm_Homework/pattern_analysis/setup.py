from setuptools import setup, find_packages

setup(
    author="Anni Liu",
    description="A package for analyzing patterns for genome sequences",
    name="pattern_analysis",
    packages=find_packages(include=["pattern_analysis", "pattern_analysis.*"]),
    version="0.1.0",
)
