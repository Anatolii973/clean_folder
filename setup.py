from setuptools import setup


setup(name="clean_folder",
      version="0.1.0",
      description="My class",
      url="https://github.com/LAV1970/Homework_2",
      author="Anatoliy Kedis",
      author_email="tolkedis73@gmail.com",
      license="MIT",
      packages=["clean_folder"],
      entry_points={"console_scripts": ["clean-folder = clean_folder.clean:main"]},
      )
      