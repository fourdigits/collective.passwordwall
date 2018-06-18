from setuptools import setup, find_packages

version = '0.1a1'

setup(name='collective.passwordwall',
      version=version,
      description="Passwordwall plugin",
      long_description=open("README.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='',
      author='Kees Hink',
      author_email='kees@fourdigits.nl',
      url='https://fourdigits.nl/',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )
