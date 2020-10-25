fifa_2019_players
==============================

FIFA 2019 Players

Dataset from kaggle [FIFA 2019 Players](https://www.kaggle.com/karangadiya/fifa19)

Project Organization
------------

    ├── LICENSE
    ├── README.md                           <- The top-level README for developers using this project.
    ├── data
    │   ├── external                        <- Data from third party sources.
    │   ├── interim                         <- Intermediate data that has been transformed.
    │   ├── processed                       <- The final, canonical data sets for modeling.
    │   └── raw                             <- The original, immutable data dump.
    │
    ├── docs                                <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── reports                             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures                         <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt                    <- The requirements file for reproducing the analysis environment, e.g.
    │                                          generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                            <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                                 <- Source code for use in this project.
    │   ├── __init__.py                     <- Makes src a Python module
    │   │
    │   ├── etl                             <- Scripts for data ETL
    |   |   ├── __init__.py                 <- Makes src a Python module
    │   |   └── players_etl.py              <- FIFA player ETL script
    │   |
    │   └── reports                         <- Scripts for generating reports
    |       ├── __init__.py                 <- Makes src a Python module
    │       └── mean_age_by_nationality.py  <- Mean, sum, and total ages for FIFA players by nationality
    | 
    └── tox.ini                             <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
