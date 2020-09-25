## Python Project Template

> Setup Template for Python Projects in [Deepnote](https://deepnote.com/) (or Locally)

### Getting Started

> See [```getting_started_local```](./getting_started_local.md) and [```getting_started_deepnote```](./getting_started_deepnote.md). If viewing this in [Deepnote](https://deepnote.com/), see ```.ipynb``` versions.

**Note**: For **learning purposes**, ***recreate*** these project setup templates for yourself. ***Customise*** it to have it make sense to you, so every time you start a new project (either locally or on Deepnote) you can ***quickly refer*** to this template of yours on Github! 

#### ```User Story```

> The sample program is in the form of an ***interactive Python notebook***. See **[```sample_notebook.ipynb```](./sample_notebook.ipynb)**.

+ This script reads and parses CSV data from URL (via pandas),
+ filters out athletes representing ```Australia```,
+ and displays the filtered dataframe.
+ The Script then reads and parses in JSON data from URL (same data),
+ filters out athletes representing ```Great Britain```,
+ and finally writes the filtered dataframe into two new files,
+ one with the data parsed as CSV, and the other parsed as JSON.

**Note**: To **run** code in the sample notebook, ***recreate*** this project, or ***fork*** this repo. You can then **clone** your own ***fork**& **locally (via CLI)** or **clone** it into a **Deepnote Project (via Git Services Tab)**. **Once cloned, follow the instructions below**. 

#### ```Dependencies```

> **If cloned locally**, install dependencies ```jupyter``` + ```pandas```. See [this guide](https://realpython.com/pipenv-guide/) for help on ```pipenv``` (if not familiar) e.g.

```bash
# Install pipenv (if not already)
$ pip install pipenv
# Install dependencies with pipenv
$ pipenv install jupyter pandas
```

> **If cloned in Deepnote**, and you want to use **```pipenv```**, ***replace*** the code in **```init.ipyb```** (via Environment Tab) ***with code below***, and ***restart*** the ***machine***.

```bash
%%bash
# Make sure we change into the project directory, if you have placed your project in the deepnote root directory comment out the line below.
cd python_project_template
# If your project has a 'Pipfile' file, we'll install it here apart from blacklisted packages that interfere with Deepnote (see above).
if test -f Pipfile
  then
    sed -i '/jedi/d;/jupyter/d;' Pipfile
    pip install pipenv
    pipenv install
  else echo "There's no Pipfile, so nothing to install. This is the case with most projects."
fi
```

#### ```Running```

> To run the notebook simply ***open and run*** the **```sample_notebook.ipynb```** file ***within Deepnote***. If running ***locally*** with ```pipenv```, then open the ```jupyter``` console like...

```bash
$ pipenv run jupyter notebook .
```

#### ```Contributing```

> See [```contributing.md```](./contributing.md)

