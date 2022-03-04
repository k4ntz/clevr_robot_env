import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clevr_robot_env",
    version="1.0.0",
    author="Deepmind",
    author_email="author@example.com",
    description="Developing RL agents at the intersection of vision, language, and control.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/google-research/clevr_robot_env",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
