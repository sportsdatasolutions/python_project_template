## Python Project Setup (Local)
> Best Practices for begining a Python Project Locally (so your projects work well in any virtual/local environment)

## Github  
> Setting up a Github Repo for the Project

#### 1. Set up a **Github repo** for your project called ```python_project_template```. Your choice as to Private or Public.

#### 2. Setup with a **Readme and Gitignore File (Python)**

#### 3. No need to setup a **licence** unless your creating an ***Open Source*** Project, in which case choose the licence that best suits your protection needs.

## Git
> Cloning Project Locally

#### 1. **Copy the SSH** of your project repo.

#### 2. On your CLI, clone your project into a directory called ```python_project_template```.

```bash
$ git clone git@github.com:user_name/python_project_template.git python_project_template
$ cd python_project_template
$ ls -al
$ git status
```

## Readme 
> Below is a template for a good basic Readme. Please use it.

Also see the [Readme](./Readme.md) to this project which is written off the template below. Even if you don't know the full extent of your project yet, it's good practise to set up a Readme template that you can easily **edit as you progress**. See [contributing.md](./contributing.md) file for an example/template to providing **contribution guidelines** for your projects (if applicable).

```markdown
## Project Title

> Sub-Heading (Small Description)

## Getting Started

> Place a more detailed description of your project, how it came about, inspiration, reading. 

### ```Story```

> User Story for your project. Decribe what you solutions does, in a brief step by step story.

### ```Dependencies```

> Instructions for installing project dependencies (packages the project will depend on).

### ```Running```

> Instructions for running the solution.

## Contributing

> Instructions for contributing to the project. See [contributing.md](./contributing.md).
```

## Dependencies
> Dealing with project dependencies (packages the project will depend on)

We ***reccommend*** handling ***project dependencies*** via ```pipenv```. See [the docs](https://docs.pipenv.org/) for help on ```pipenv``` (if not familiar or installed) **Follow steps below to use ```pipenv``` to manage dependencies**.

#### 1. Install ```pipenv``` with ```pip``` (if not already installed)

```bash
$ pip install --user pipenv
```

#### 2. Run ```pipenv install```

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

**Note**: You can now ***install*** all other possible packages you may need for your project e.g. ```pipenv install jupyter pandas```.

## Project as a Github Template
> Customise your Project Template (e.g. Readme, Contributing, Pipfile w/ Default Packages). Once you're happy with it, proceed to making it a proper template!

#### 1. On Github, make your Project a [Github Template](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-template-repository).

#### 2. You can create branches on this template that will relate to different versions of your base template. E.g. you could have a branch called ```python_web_scraping_template``` that will have additional default packages within it's Pipfile that relate specifically to web scraping. Now when your start a new web scraping project, you could tick the ```Include all branches``` option so you can merge in the web scraping branch via Pull Request before beginning your project!

#### 3. Click the ```Use this template``` button to create a new project from your template, and try the Sample Python Project below!

## Sample Python Project

> Sample Project to Test your Template. Uses Pandas to fetch and parse HTML tables from Power10 website and output the number of tables found.

#### 1. As we know we're going to be using Jupyter and Pandas, so install them via ```pipenv```, if you haven't already: 

```bash
$ pipenv install jupyter pandas
```

#### 2. **Copy** code below into a python script (or a notebook if you prefer). e.g. ```touch test_script.py```, open in VSCode then type:

```python
import pandas

url = "https://www.thepowerof10.info/rankings/rankinglist.aspx?event=100&agegroup=ALL&sex=W&year=2020"

dfs = pandas.read_html(url)

print(len(dfs))
```

#### 4. Run the ```test_script.py``` file via CLI:

```bash
$ pipenv run python test_script.py
```

#### 5. You'll notice an error, if you scroll down, you'll see it's a missing package called ```lxml```. Install ```lxml``` via ```pipenv```:

```bash
$ pipenv install lxml
$ pipenv run python test_script.py
```

**Note**: Delete test script/notebook e.g. ```rm test_script.py``` and remove dependencies with ```pipenv uninstall``` e.g. ```pipenv uninstall lxml```. 
