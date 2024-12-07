from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-scientist",
    version="0.1.7",
    author="",  # TODO: Add your name
    author_email="",  # TODO: Add your email
    description="An AI-powered scientific research assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",  # TODO: Add your repository URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "anthropic",
        "aider-chat",
        "backoff",
        "openai",
        "matplotlib",
        "pypdf",
        "pymupdf4llm",
        "torch",
        "numpy",
        "transformers",
        "datasets",
        "tiktoken",
        "wandb",
        "tqdm",
        "scikit-learn",
        "einops",
    ],
    entry_points={
        "console_scripts": [
            "launch-scientist=launch_scientist:main",
        ],
    },
    package_data={
        "ai_scientist": [
            "templates/*/*.py",
            "templates/*/template.tex",
            "templates/*/references.bib",
            "templates/*/*.pdf", 
            "fewshot_examples/*",
            "fewshot_examples/*.pdf",
        ],
    },
    include_package_data=True,
) 