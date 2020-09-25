## Python Project Template

> Setup Template for Python Projects in [Deepnote](https://deepnote.com/) or Locally

### Getting Started

> See [```getting_started_local```](./getting_started_local.md) and [```getting_started_deepnote```](./getting_started_deepnote.md). Feel free to view this in [Deepnote](https://deepnote.com/project/38ed87ae-207f-4a03-bfc1-5204106200d5), see ```.ipynb``` versions.

This setup guide inspired our [Python Project Template](https://github.com/sportsdatasolutions/python_project). If you are coming from there, have a read of our ***getting started*** guides (linked above) to give you more of an ***understanding*** as to how you can ***customise*** your own version of the template.

**Note**: Below are example Readme elements for the sample project. See **[```sample_notebook.ipynb```](./sample_notebook.ipynb)**.

#### ```User Story```

> The sample program is in the form of an ***interactive Python notebook***. The ***data*** used in the notebook is a list of ***Seasons Best from the 2017/18 Swimming Season***.

+ This notebook reads and parses CSV data from URL (via pandas),
+ filters out athletes representing ```Australia```,
+ and displays the filtered dataframe.
+ The notebook then reads and parses in JSON data from URL (same data),
+ filters out athletes representing ```Great Britain```,
+ and finally writes the filtered dataframe into two new files,
+ one with the data parsed as CSV, and the other parsed as JSON.

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
  else
    pip install pipenv
    pipenv install
fi
```

#### ```Running```

> To run the notebook simply ***open and run*** the **```sample_notebook.ipynb```** file ***within Deepnote***. If running ***locally*** with ```pipenv```, then open the ```jupyter``` console like...

```bash
$ pipenv run jupyter notebook .
```

#### ```Contributing```

> See [```contributing.md```](./contributing.md)

