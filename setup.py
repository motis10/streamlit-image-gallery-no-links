from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-image-gallery-enhanced",
    version="1.0.1",
    author="motis10",
    author_email="moti.stein@gmail.com",
    description="Enhanced Streamlit component for displaying images in a responsive grid with hover effects and click callbacks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/motis10/streamlit-image-gallery-no-links",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords="streamlit, image, gallery, grid, component, hover, interactive",
    python_requires=">=3.7",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
    extras_require={
        "devel": [
            "wheel",
            "pytest==7.4.0",
            "playwright==1.39.0",
            "requests==2.31.0",
            "pytest-playwright-snapshot==1.0",
            "pytest-rerunfailures==12.0",
        ]
    }
)
