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

##### **Note**: By **default** Deepnote will **clone** the project into a new ***folder***. If you have any ***existing*** files or folders that you'd like to add to the version controlled project, simply drag and drop them into the project folder. **Alternatively**, you can work from the Deepnote project root by simply dragging everything (including ```.git``` folder) out of the 'project folder' and deleting the empty project folder.

## Terminal
> Setting up a Terminal (CLI) for our Project

##### 1. On Deepnote Project, navigate to **Terminals** tab (left nav bar).

##### 2. ***Click*** the ```+``` icon to create a new Terminal.

##### 3. ***Rename*** the **Terminal** if you'd like.

##### 4. Now we can use this **Terminal** as we would ***locally***. The ***prompt*** will read ```jovyan@deepnote:~/work```:

```bash
$ cd python_project_template    # if working within project folder
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

**Note**: Handling Python project dependencies locally is ***almost*** the same on Deepnote. Only difference is that Deepnote already has it's own dependencies pre-installed. It's good practice to track the dependencies of our projects ourselves (so our projects can be used outside of Deepnote). The [Documentation](https://docs.deepnote.com/environment/python-requirements) suggests using ```pip``` and a ```requirements.txt``` file (which you are free to do), however we can also use ```pipenv```. To do this we'll need to replace some code in ```init.ipynb``` to deal with ```pipenv``` and ```Pipfile``` instead of ```pip``` and ```requirements.txt```. **Follow steps below to use ```pipenv``` to manage dependencies**.

##### 1. Simply customise ```init.ipynb``` file (Environment Tab) to install ```pipenv``` and project dependencies in ```Pipfile```. You'll already see the code cell for ```pip``` and ```requirements.txt``` there. We can just **replace the code in this code cell with ours** (which will also deal with deleting ```jupyter``` or ```jedi``` packages from Pipfile):

```bash
%%bash
# Make sure we change into the project directory, if this project is in the root directory comment out the line below.
cd project_folder # Change project_folder to your actual project folder name!
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

##### 2. **Run** the the ***code cell*** or **restart** the ***machine***. The bash script will firstly change directory into your project folder and check if there is a ```Pipfile```. If there is one, it will remove blacklisted packages, install ```pipenv```, and run ```pipenv install```. If not, it will install ```pipenv``` and run ```pipenv install``` to initialise a ```Pipfile``` and ```Pipfile.lock```.

**Note**: If you ***don't*** want to work out of a ***project folder** within Deepnote, you can simply ***drag*** all the files and folders (including ```.git``` folder) into the root of your Deepnote project, and delete the empty project folder. In the ```init.ipynb``` file, simply **comment out** the line that ```cd```s into the 'project folder'. At the same time, as you're now operating in the Deepnote project root, you'll want to ***add*** **```.deepnote```**  and **```init.ipynb```** to your **```.gitignore```** file. e.g.

```
# ignore deepnote files
.deepnote
init.ipynb
```

**Do This**: You can now ***install*** all other possible dependecies you may need for your project via the **Terminal** e.g. 

  ```bash
  # if working out of project folder
  $ cd project_folder
  $ pipenv install pandas
  # if working from Deepnote root
  $ pipenv install pandas
  ``` 

  If you **restart** your ***machine*** (Environment Tab), Deepnote will run the ```init.ipynb``` file to install all you're project dependencies automatically via ```pipenv```.

**Note**: **As per the warning in ```init.py``` do not install the packages ```jedi``` or ```jupyter```**. If you are using ```.ipynb``` files however, make sure you make ***note*** ```jupyter``` down as a project dependency on your project **Readme**.

## Sample Python Program

> Sample Project to Test Dependency Management. The script will use Pandas to fetch and parse HTML tables from Power10 website and output the number of tables found.

##### 1. As we know we're using Pandas, so install ```pandas``` via ```pipenv```. Open Terminal, ``cd`` into project folder if working within one: 

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