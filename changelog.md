
# Changelog

Jupman Jupyter Manager 

http://jupman.readthedocs.com

## January 16th 2020 - 3.1

- removed jupman.init root parameter
- bugfixes
- upgraded nbsphinx from 0.3.4 to 0.5.0
- upgraded sphinx_rtd_theme from 0.2.5b1 to 0.4.3
- upgraded sphinx from 1.7.6 to 2.3.1
- upgraded recommonmark from 0.4.0 to 0.6.0

## December 29th 2019 - 3.0

- much simplified folder structure 
  - [Issue 33](https://github.com/DavidLeoni/jupman/issues/33)

- removed solutions from header requirement 
  - [Issue 32](https://github.com/DavidLeoni/jupman/issues/32)

- introduced tests (pytest, hypothesis)
- removed old_news in favor of changelog.md
- Latex:
    - much better PDF cover
    - using xelatex
    - set up unicode mappings
- several fixes

## September 24th 2018 - 2.0

- now using index.ipynb as home. Hurray !

## September 19th 2018 - 1.0

- fixed build.py
- added html templates examples
- cleaned toc (was showing too much when loading)


## August 26th 2018 - 0.9

- implemented generation of exercises from solutions
  [Issue 14(https://github.com/DavidLeoni/jupman/issues/14)
- reverted to old jupman.init() code
  [Issue 12](https://github.com/DavidLeoni/jupman/issues/12)

## August 12th 2018 - 0.8

- Prepended all functions in jupman.py with `jupman_`

- replaced index with proper homepage. 
  see [Issue 11](https://github.com/DavidLeoni/jupman/issues/11)
  
  - from now on you need home.ipynb file, because replacing index.rst is a nightmare! 
  - new index.rst is just a placeholder which simply redirects to home.html. Do not modify it.
  - put the toctree in toc.rst
  
- exercises ipynb can now stay in exercises/ folder; when exercises are zipped,
  jupman automatically adds to the zip the required site files. 
  see [Issue 12](https://github.com/DavidLeoni/jupman/issues/12)
  
- Tried %run at beginning of notebooks, without much satisfaction
  (see discussion in [Issue 12](https://github.com/DavidLeoni/jupman/issues/12)): 
  
- disabled toc by default in html files. To enable it, in python use `%run -i ../../jupman --toc`
- renamed past-exams directory from 'past-exams' to 'exams'
- created `info`, `error`, `warn`, `fatal` functions to `conf.py`
- introduced new variable `exercise_common_files` in `conf.py` for common files to be zipped
- added pages `exam-project` , `markdown` , `project-ideas`, 
- added `cc-by.png`
- renamed `changelog.txt` to `changelog.md`
- now using templates with curly brackets in in templating, like `_JM_{some_property}`
- jupman.js : now when manually saving html in Jupyter, resulting html correctly hides cells
- Fixes https://github.com/DavidLeoni/jupman/issues/2 : 
  now toc is present in local build for pdfs 

## August 3rd 2018 - 0.7

- added jupman.py pytut() for displaying Python tutor in the cells
- added  jupman.py toc=False option to jupman.py init to disable toc
- removed  jupman.pyuseless networkx import from 

- fixed usage indentation
- added changelog.txt

