import setuptools

with open("README.md", "r") as f:
    description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Podcast Listening Time Prediction"
AUTHOR_USER_NAME = "Kishor"
SRC_REPO = "PodcastListeningTimePrediction"


setuptools.setup(
    name = SRC_REPO, 
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email = "kishor04reddy@gmail.com",
    long_description=description,
    long_description_content_type="text/markdown",
    url =  "https://github.com/kishor2004reddy/PodcastListeningTimePrediction.git",
    package_dir={"": "src"},
    packages = setuptools.find_packages(where = "src")
)