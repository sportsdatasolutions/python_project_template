## Python Project Templates (Tutorial)

> Setup Template for Python Projects in [Deepnote](https://deepnote.com/) or Locally

### Getting Started

> This setup guide inspired our [Python Project Template](https://github.com/sportsdatasolutions/python_project). If you are coming from there, have a read of our ***getting started*** guides (linked below) to give you more of an ***understanding*** as to how you can ***customise*** your own version of the template.

#### See our **[Getting Started Locally Guide](./getting_started_local.md)** 
> To create your own ***Github Repo*** for ***Local Python Projects***. You can then setup your resulting Github Repo as a [Github Template](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-template-repository) for future projects!

#### See our **[Getting Started Deepnote Guide](./getting_started_deepnote.md)** 
> To create your own ***Deepnote Project Template*** for ***Deepnote Projects***. Feel free to view this [Tutorial in Deepnote](https://deepnote.com/project/38ed87ae-207f-4a03-bfc1-5204106200d5), see ```.ipynb``` versions.

#### ```Story - Sample Notebook```

> This section, and sections below are ***example*** **Readme** elements for the **[sample notebook](./sample_notebook.ipynb)**. This is ***not*** a part of the tutorial, simply here as a ***reference*** for how to set up ***Readmes*** for your future projects. To follow the **tutorials**, run through the **Getting Started Guides** above.

+ This notebook reads and parses CSV data from URL (via pandas),
+ filters out athletes representing ```Australia```,
+ and displays the filtered dataframe.
+ The notebook then reads and parses in JSON data from URL (same data),
+ filters out athletes representing ```Great Britain```,
+ and finally writes the filtered dataframe into two new files,
+ one with the data parsed as CSV, and the other parsed as JSON.

#### ```Dependencies```

> **If cloned locally**, install dependencies (packages the project will depend on) ```jupyter``` + ```pandas```. See [this guide](https://realpython.com/pipenv-guide/) for help on ```pipenv``` (if not familiar) e.g.

```bash
# Install pipenv (if not already)
$ pip install --user pipenv
# Install packages with pipenv
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
    pipenv install --skip-lock
  else
    pip install pipenv
    pipenv install --skip-lock
fi
```

#### ```Running```

> To run the notebook simply ***open and run*** the **```sample_notebook.ipynb```** file ***within Deepnote***. If running ***locally*** with ```pipenv```, then open the ```jupyter``` console like...

```bash
$ pipenv run jupyter notebook .
```

#### ```Contributing```

> See [```contributing.md```](./contributing.md)

