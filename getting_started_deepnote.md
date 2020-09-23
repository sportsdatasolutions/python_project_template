## Python Project Setup
> Best Practices for begining a Python Project on Deepnote (so your projects work well in any virtual/local environment)

## Github  
> Setting up a Github Repo for the Project

##### 1. Set up a **Github repo** for your project called python_project_template. Your choice as to Private or Public.

##### 2. Setup with a **Readme and Gitignore (python)**

##### 3. No need to setup a **licence** unless your creating an ***Open Source*** Project, in which case choose the licence that best suits your protection needs.

## Deepnote
> Create a Deepnote Project

##### 1. Create a **Deepnote Project** called ```python_project_template```. Note that you can access various resources via the ***question mark*** on ***bottom left*** of a project e.g. Documentation.

##### 2. Deepnote will start you out with a sample notebook. **Delete** it.

## Git
> Integrating Git and Github into our Deepnote Project

##### 1. **Copy the SSH** of your project repo.

##### 2. On Deepnote Project, navigate to **Git Services** tab (left nav bar).

##### 3. ***Paste*** the SSH of your repo into the **Github** text field.

##### 4. ***Click*** the **Link Github Repository** button.

##### **Note**: By **default** Deepnote will **clone** the project into a new ***folder***. We ***reccommend*** keeping it this way, placing any project files within the version controlled directory (this will now be the root of your project, it will contain a ```.git``` folder and your Readme + Gitignore). If you have any ***existing*** files or folders that you'd like to add to the version controlled project, simply drag and drop them into the project root.

## Terminal
> Setting up a Terminal (CLI) for our Project

##### 1. On Deepnote Project, navigate to **Terminals** tab (left nav bar).

##### 2. ***Click*** the ```+``` icon to create a new Terminal.

##### 3. ***Rename*** the **Terminal** if you'd like.

##### 4. Now we can use this **Terminal** as we would ***locally***. The ***prompt*** will read ```jovyan@deepnote:~/work```:

```bash
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
> Dealing with project dependencies on Deepnote

###

**Note**: Handling Python project dependencies locally is ***almost*** the same on Deepnote. Deepnote already has it's own dependencies pre-installed but it's good practice to track the dependencies of our own projects ourselves (so our projects can be used outside of Deepnote). The [Documentation](https://docs.deepnote.com/environment/python-requirements) suggests using ```pip``` and a ```requirements.txt``` file (which you are free to do), however we can also use ```pipenv```. For this we'll need to create our own code in ```init.ipynb``` to deal with ```pipenv``` and ```Pipfile``` instead of ```pip``` and ```requirements.txt```. **Follow steps below to use ```pipenv``` to manage dependencies**.

##### 1. On Open Terminal and install ```pipenv``` with ```pip```

```bash
$ pip install pipenv
```

##### 2. Run ```pipenv install```

```
$ pipenv install
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Creating a Pipfile for this project…
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (a65489)!
Installing dependencies from Pipfile.lock (a65489)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
```

**Note**: ```pipenv``` identifies that you are already working within a virtual environment (as you would locally with ```pipenv```). So simply creates a ```Pipfile``` and ```Pipfile.lock``` without initialising another virtual environment.

##### 3. Customise Deepnote ```init.ipynb``` to install ```pipenv``` and project dependencies in ```Pipfile```. You'll already see the code block for ```pip``` and ```requirements.txt``` there. We can just **replace this code block** with ours (which will also deal with deleting ```jupyter``` or ```jedi``` packages from Pipfile):

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

**Note**: You can now ***install*** all other possible dependecies you may need for your project via the **Terminal** e.g. ```pipenv install pandas```. If you restart your machine, deepnote will run the ```init.ipynb``` file to install all you're project dependencies automatically via ```pipenv```.

**Note**: **As per the warning in ```init.py``` do not install the packages ```jedi``` or ```jupyter```**. If you are using ```.ipynb``` files however, make sure you make ***note*** ```jupyter``` down as a project dependency on your project **Readme**.

## Sample Python Program

> Sample Project to Test Dependency Management. The script will use Pandas to fetch and parse HTML tables from Power10 website and output the number of tables found.

##### 1. As we know we're using Pandas, so install ```pandas``` via ```pipenv```. Open Terminal: 

```bash
$ pipenv install pandas
```

##### 2. **Copy** code below into a code cell (create a notebook if you don't have one in your project yet) and ***Run*** the code cell.

```python
import pandas

url = "https://www.thepowerof10.info/rankings/rankinglist.aspx?event=100&agegroup=ALL&sex=W&year=2020"

dfs = pandas.read_html(url)

len(dfs)
```

##### 3. You'll notice an error, if you scroll down, you'll see it's a missing package called ```lxml```. Install ```lxml``` via ```pipenv```:

```bash
$ pipenv install lxml
```

##### 4. Restart the notebook and re-run the code cell.

**Note**: Remove dependencies with ```pipenv uninstall``` e.g. ```pipenv uninstall lxml```.

## 3rd Party Integrations (Deepnote)

> Use the code in [```sample_notebook.ipynb```](./sample_notebook.ipynb) (type it all out, don't copy paste over :P) to test out Deepnote integrations (see Integrations Tab on Deepnote Project).