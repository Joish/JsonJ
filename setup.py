from distutils.core import setup
setup(
  name = 'JsonParser',         # How you named your package folder (MyLib)
  packages = ['JsonParser'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library to prase Json Tree data in-order to make things simpler',   # Give a short description about your library
  author = 'Joish J Bosco',                   # Type in your name
  author_email = 'joishbosco99@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Joish/JsonParser',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Joish/JsonParser/archive/v_0.1.tar.gz',    # I explain this later on
  keywords = ['Python 3', 'Json', 'Tree','Tree Traversal', 'Recursive'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)