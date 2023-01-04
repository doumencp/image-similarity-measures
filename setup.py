import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image-similarity-measures",
    version="0.3.5",
    author="UP42",
    maintainer=[
        {'name ': 'Pierre Doumenc', 'email': 'fcharp35@gmail.com'},
        {'name ': 'François Charpentier', 'email': 'fcharp35@gmail.com'}
    ],
    author_email="support@up42.com",
    description="Evaluation metrics to assess the similarity between two images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doumencp/image-similarity-measures",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
    ],
    extras_require={
        "rasterio": ["rasterio"],
        "speedups": ["pyfftw"],
    },
    install_requires=["numpy", "scikit-image", "opencv-python", "phasepack", "matplotlib"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "image-similarity-measures=image_similarity_measures.evaluate:main"
        ],
    },
)
