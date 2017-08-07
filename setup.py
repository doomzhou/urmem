from setuptools import setup

setup(
    name= 'urmem',
    version= '0.0.42',
    packages = ['urmem'],
    entry_points = {
        "console_scripts": [
            "urmem = urmem.urmem:main",
        ]
    },
    author='doomzhou',
    author_email='zzepaigh@gmail.com',
    license='Apache',
    url='https://github.com/doomzhou/urmem',
    description='Download a git repo raw file content in every server, sometimes for source bash_profile'
)
