## Python Project Setup
> Best Practices for begining a Python Project Locally (so your projects work well in any virtual/local environment)

## Github  
> Setting up a Github Repo for the Project

##### 1. Set up a **Github repo** for your project called ```python_project_template```. Your choice as to Private or Public.

##### 2. Setup with a **Readme and Gitignore (python)**

##### 3. No need to setup a **licence** unless your creating an ***Open Source*** Project, in which case choose the licence that best suits your protection needs.

## Git
> Cloning Project Locally

##### 1. **Copy the SSH** of your project repo.

##### 2. On your CLI, clone your project into a directory called ```python_project_template```.

```bash
$ git clone git@github.com:user_name/python_project_template.git python_project_template
$ cd python_project_template
$ ls -al
$ git status
```

## Readme 
> Below is a template for a good basic Readme. Please use it. Also see the [```Readme```](./Readme.md) to this project which is written off the template below. Even if you don't know the full extent of your project, it's good practise to set up a Readme template that you can easily **edit as you progress**.

```markdown
## Project Title

> Sub-Heading (Small Description)

### Getting Started

> Place a more detailed description of your project, how it came about, inspiration, reading. 

#### ```User Story```

> User Story for your project. Decribe what you solutions does, in a brief step by step story.

#### ```Dependencies```

> Instructions for installing project dependencies, see this projects [Readme](./Readme.md) for a good template.

#### ```Running```

> Instructions for running the solution.

#### ```Contributing```

> Instructions for contributing to the porject.
```

## Dependencies
> Dealing with project dependencies locally (so they can work well in any virtual/local environment)

###

**Note**: We ***reccommend*** handling ***project dependencies*** via ```pipenv```. See [this guide](https://realpython.com/pipenv-guide/) for help on ```pipenv``` (if not familiar or installed) **Follow steps below to use ```pipenv``` to manage dependencies**.

##### 1. On CLI, install ```pipenv``` with ```pip``` (if not already installed)

```bash
$ pip install --user pipenv
```

##### 2. Run ```pipenv install```

```
$ pipenv install
...
Creating a Pipfile for this project…
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (a6xxxx)!
Installing dependencies from Pipfile.lock (a6xxxx)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
```

**Note**: You can now ***install*** all other possible dependecies you may need for your project via the **CLI** e.g. ```pipenv install jupyter pandas```.

## Sample Python Program

> Sample Project to Test Dependency Management. Using Pandas to fetch and parse HTML tables from Power10 website and output the number of tables found.

##### 1. As we know we're going to be using Jupyter and Pandas, so install them via ```pipenv```, if you haven't already: 

```bash
$ pipenv install jupyter pandas
```

##### 2. **Copy** code below into a python script (or a notebook if you prefer). e.g. ```touch test_script.py```, open in VSCode then type:

```python
import pandas

url = "https://www.thepowerof10.info/rankings/rankinglist.aspx?event=100&agegroup=ALL&sex=W&year=2020"

dfs = pandas.read_html(url)

print(len(dfs))
```

##### 4. Run the ```test_script.py``` file via CLI:

```bash
$ pipenv run python test_script.py
```

##### 5. You'll notice an error, if you scroll down, you'll see it's a missing package called ```lxml```. Install ```lxml``` via ```pipenv```:

```bash
$ pipenv install lxml
$ pipenv run python test_script.py
```

**Note**: Delete test script/notebook e.g. ```rm test_script.py``` and remove dependencies with ```pipenv uninstall``` e.g. ```pipenv uninstall lxml```.

## 3rd Party Integrations

> If your project will need some sort of 3rd party integration, e.g. Accessing files from AWS S3 bucket or a collection from a MongoDB cluster, we strongly reccommend testing these integrations before moving on with your project. Feel free to use the sample code in [```sample_notebook.ipynb```](./sample_notebook.ipynb).