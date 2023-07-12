"""Setup.py for Pypi.org"""
from distutils.core import setup

setup(
    name="tsp_2opt",
    packages=["tsp_2opt"],
    version="0.0.1",
    description="Solver to efficiently find good sub-optimal solutions to the TSP. It uses the 2-opt heuristic and the search part is implemented in Rust.",
    author="Mehdi Bnc <mehdi-bs@live.fr>",
    url="https://github.com/mehdibnc/TSP2opt",
    license="MIT",
    
    install_requires=[
        "numpy>=1.20.1",
    ],
    keywords=["test", "regression", "automatically"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Rust",
    ],
    python_requires=">=3.7",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
