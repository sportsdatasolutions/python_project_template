## Python Project Template

> Setup Template for Python Projects in Deepnote (or Locally)

### Getting Started

> See [```getting_started_local.ipynb```](./getting_started_local.ipynb) and [```getting_started_deepnote.ipynb```](./getting_started_deepnote.ipynb).

For **learning purposes**, ***recreate*** these project setup templates for yourself. ***Customise*** it to have it make sense to you, so every time you start a new project (either locally or on Deepnote) you can ***quickly refer*** to this template of yours on Github! 

To just **run** the [```sample_notebook.ipynb```](./sample_notebook.ipynb) instead, **fork** this repo, **clone** it **locally (via CLI)**, or, **clone** it into a **Deepnote Project (via Git Services Tab)**, then, follow the instructions below. 

#### ```Dependencies```

> **If cloned locally**, install dependencies in ```Pipfile``` + ```jupyter```. See [this guide](https://realpython.com/pipenv-guide/) for help on ```pipenv``` (if not familiar) e.g.

```bash
# Install pipenv (if not already)
$ pip install pipenv
# Run pipenv install (within cloned project directory)
$ pipenv install
# Install other dependencies e.g. jupyter
$ pipenv install jupyter
```

> **If cloned in Deepnote**, ***replace*** the code in ```init.ipyb``` (via Environment Tab) ***with code below***, and ***restart*** the ***machine***.

```bash
%%bash
# If your project has a 'Pipfile' file, we'll install it here apart from blacklisted packages that interfere with Deepnote (see above).
if test -f Pipfile
  then
    sed -i '/jedi/d;/jupyter/d;' ./Pipfile
    pip install pipenv
    pipenv install
  else echo "There's no Pipfile, so nothing to install. This is the case with most projects."
fi
```

#### ```User Story```

> The script is in the form of an interactive Python notebook. Please see ```sample_notebook.ipynb```.

+ This script reads and parses CSV data from URL (via pandas),
+ filters out athletes representing ```Australia```,
+ and displays the filtered dataframe.
+ The Script then reads and parses in JSON data from URL (same data),
+ filters out athletes representing ```Great Britain```,
+ and finally writes the filtered dataframe into two new files,
+ one with the data parsed as CSV, and the other parsed as JSON.

#### ```Running```

> To run the script simply ***open and run*** the ```sample_notebook.ipynb``` file within Deepnote. If not in Deepnote, make sure you have ```jupyter``` installed first:

```bash
$ pipenv run jupyter notebook sample_notebook.ipynb
```

#### ```Contributing```

> See ```contributing.md``` (or simply place your own version of instructions below)

