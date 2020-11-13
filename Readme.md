## Python Project Templates (Tutorial) [<img height="31" align="right" src="https://beta.deepnote.com/buttons/launch-in-deepnote-white.svg">](https://deepnote.com/project/38ed87ae-207f-4a03-bfc1-5204106200d5#%2Fgetting_started_deepnote.ipynb)

![deepnote](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/Links/deepnote.jpg)

## Getting Started

> This setup guide inspired our [Python Project Template](https://github.com/sportsdatasolutions/python_project). If you are coming from there, have a read of our ***getting started*** guides (linked below) to give you more of an ***understanding*** as to how you can ***customise*** your own version of the template.

### See our **[Getting Started Deepnote Guide](./getting_started_deepnote.md)** 
> To create your own ***Deepnote Project Template*** for ***Deepnote Projects***. Launch this tutorial in [Deepnote](https://deepnote.com/) via the button at [top](#python-project-templates-tutorial-) of this Readme.

### See our **[Getting Started Locally Guide](./getting_started_local.md)** 
> To create your own ***Github Repo*** for ***Python Projects***. You can then setup your resulting Github Repo as a [Github Template](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-template-repository) for future projects!

### ```Story - Sample Notebook```

> This section, and sections below are ***example*** **Readme** elements for the **[sample notebook](./sample_notebook.ipynb)**. This is ***not*** a part of the tutorial, simply here as a ***reference*** for how to set up ***Readmes*** for your future projects. To follow the **tutorials**, run through the **Getting Started Guides** above.

+ This notebook reads and parses CSV data from URL (via pandas),
+ filters out athletes representing ```Australia```,
+ and displays the filtered dataframe.
+ The notebook then reads and parses in JSON data from URL (same data),
+ filters out athletes representing ```Great Britain```,
+ and finally writes the filtered dataframe into two new files,
+ one with the data parsed as CSV, and the other parsed as JSON.

### ```Dependencies```

> **If cloned locally**, install dependencies (packages the project will depend on) ```jupyter``` + ```pandas```. See [the docs](https://docs.pipenv.org/) for help on ```pipenv``` (if not familiar) e.g.

```bash
# Install pipenv (if not already)
$ pip install --user pipenv
# Install packages with pipenv
$ pipenv install jupyter pandas
```

> **If cloned in Deepnote**, and you want to use **```pipenv```**, ***replace*** the code in **```init.ipyb```** (via Environment Tab) ***with code below***, and ***restart*** the ***machine***.

```bash
%%bash
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

### ```Running```

> To run the notebook simply ***open and run*** the **```sample_notebook.ipynb```** file ***within Deepnote***. If running ***locally*** with ```pipenv```, then open the ```jupyter``` console like...

```bash
$ pipenv run jupyter notebook .
```

## Contributing

> See [```contributing.md```](./contributing.md)

