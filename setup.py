from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess
import sys


class PostInstall(install):
    """Automatically run the skill installer after pip install."""
    def run(self):
        install.run(self)
        subprocess.check_call([sys.executable, "-m", "donescene.installer"])


class PostDevelop(develop):
    """Automatically run the skill installer after pip install -e."""
    def run(self):
        develop.run(self)
        subprocess.check_call([sys.executable, "-m", "donescene.installer"])


setup(
    name="donescene",
    version="1.0.0",
    description="DoneScene — AI coding protocol skills for Antigravity",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Rohit978",
    author_email="Rohit978@users.noreply.github.com",
    url="https://github.com/Rohit978/donescene",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "donescene": ["skills/ds-*/**/*", "skills/ds-*/SKILL.md"],
    },
    entry_points={
        "console_scripts": [
            "donescene=donescene.installer:main",
        ],
    },
    cmdclass={
        "install": PostInstall,
        "develop": PostDevelop,
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
