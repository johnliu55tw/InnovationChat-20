from setuptools import setup, find_packages

setup(
    name='playlist_search',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'kkbox_developer_sdk'
    ]
)
