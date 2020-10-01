## Python Project Setup (Deepnote)
> Best Practices for begining a Python Project on Deepnote (so your projects work well in any virtual/local environment)

## Deepnote
> Create a Deepnote Project

##### 1. Create a **Deepnote Project** called ```python_project_template```. Note that you can access various resources via the ***question mark*** on ***bottom left*** of a project e.g. Documentation.

##### 2. Deepnote will start you out with a sample notebook. **Delete** it.

## Git & Github
> Integrating Git and Github into our Deepnote Project

##### 1. Create a new Github Repo with a Readme and .gitignore (python) file. 

If you have a **Local Project Template**, create a new Github repo from that template.

##### 2. On Deepnote Project, navigate to **Git Services** tab (left nav bar).

##### 3. ***Paste*** the SSH of your Github repo into the **Github** text field.

##### 4. ***Click*** the **Link Github Repository** button.

By **default** Deepnote will **clone** the project into a new ***folder***. If you have any ***existing*** files or folders that you'd like to add to the version controlled project, simply drag and drop them into the project folder. **Alternatively**, we reccommend you work from the Deepnote project root by simply dragging everything (including ```.git``` folder) out of the 'project folder' and deleting the empty project folder.

##### 5. **\[Reccomended\]** **Move** Github project into Deepnote project ***root***. Including ```.git``` and delete empty folder.

## Terminal (Deepnote)
> Setting up a Terminal (CLI) for our Deepnote Project

##### 1. On Deepnote Project, navigate to **Terminals** tab (left nav bar).

##### 2. ***Click*** the ```+``` icon to create a new Terminal.

##### 3. ***Rename*** the **Terminal** if you'd like.

##### 4. Now we can use this **Terminal** as we would ***locally***. The ***prompt*** will read ```jovyan@deepnote:~/work```:

```bash
$ cd python_project_template # If working within project folder, change into project folder (containing .git folder) first.
$ ls -al
$ git status
```

## Gitignore
> Ignoring ```.deepnote``` folder/files and ```init.ipynb``` file.

##### If you are working from your ***Deepnote Project Root***, you'll notice untracked items ```.deepnote``` and ```init.ipynb``` in ```git status``` output. We ***don't*** need to check these files/folders into our version controlled project, so we can simply add them to the bottom of our ```.gitignore``` file:

```
# Deepnote files
.deepnote/
init.ipynb
```

## Readme
> Below is a template for a good basic Readme. Please use it. Also see the [```Readme```](./Readme.md) to this project which is written off the template below. Even if you don't know the full extent of your project, it's good practise to set up a Readme template that you can easily **edit as you progress**. If you are ***only*** going to be working on ***Deepnote***, we'd recommend creating a **```readme.ipynb```** or **```getting_started.ipynb```** as an ***alternative*** to what the [```Readme```](./Readme.md) is for your Github projects.

```markdown
## Project Title

> Sub-Heading (Small Description)

### Getting Started

> Place a more detailed description of your project, how it came about, inspiration, reading. 

#### ```User Story```

> User Story for your project. Decribe what you solutions does, in a brief step by step story.

#### ```Dependencies```

> Instructions for installing project dependencies (packages the project will depend on), see this projects [Readme](./Readme.md) for a good template.

#### ```Running```

> Instructions for running the solution.

#### ```Contributing```

> Instructions for contributing to the project.
```

## Dependencies
> Dealing with project dependencies (packages the project will depend on) on Deepnote

###

Handling Python project **dependencies** (packages, python version etc) locally is ***almost*** the same on Deepnote. One difference is that Deepnote already has it's own dependencies pre-installed, meaning we don't have to install commonly used packages like ```pandas```. However, it's good practice to track the dependencies of our projects ourselves (so our projects can be used outside of Deepnote? or so we can lock in package versions with ```pipenv``` on long term projects?). The [Documentation](https://docs.deepnote.com/environment/python-requirements) suggests using ```pip``` and a ```requirements.txt``` file, **which you are free to do**, however we can also use **```pipenv```**. To do this we'll need to replace some code in ```init.ipynb``` to deal with ```pipenv``` and ```Pipfile``` instead of ```pip``` and ```requirements.txt```. **Follow steps below to use ```pipenv``` to manage dependencies**:

##### 1. Simply customise ```init.ipynb``` file (Environment Tab) to install ```pipenv``` and project dependencies in ```Pipfile```. You'll already see the code cell for ```pip``` and ```requirements.txt``` there. We can just **replace the code in this code cell with ours** (which will also deal with deleting ```jupyter``` or ```jedi``` packages from Pipfile):

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

**Note:** We are using ```--skip-lock``` to tell ```pipenv``` not to create a ```Pipfile.lock```. This is because we are not building a long term project and don't want to increase project load times.

##### 2. Now you can install pacakges via ```pipenv``` in your project teminals e.g. ```pandas```:

```bash
$ pipenv install pandas --skip-lock
```

**Note**: **As per the warning in ```init.py``` do not install the packages ```jedi``` or ```jupyter```**. If you are using ```.ipynb``` files and would like to give your projects the oppertunity run locally (e.g. in jupyter notebook/lab), make sure you make a ***note*** of ```jupyter``` being a project dependency on your project **Readme** (or add ```jupyter = "*"``` to your version controlled ```Pipfile```).

##### 3a. Installing dependencies via ```pip``` during your projects initialisation phase can significantly increase the time it takes to load your projects after a restart (e.g. ```pip install pipenv``` in ```init.ipynb```). An alternative way of dealing with this in Deepnote is via the ```Dockerfile```. Read more about [custom environments here](https://docs.deepnote.com/environment/custom-environments). e.g. In the **```Dockerfile```** (Environment Tab), we can create an environment with ```pipenv``` pre-installed like so:

```dockerfile
FROM ..
RUN sudo apt-get update
RUN pip install pipenv
```

##### 3b. Hit ```Run build``` or ```Build``` and Deepnote will create a chached image of this custom environment (which will include ```pipenv``` by default). **Restart the machine when promt to do so**. This simple step will have cut our project's load time significantly! Remember to remove the ```pip install pipenv``` commands from your projects ```init.ipynb``` notebook.

## Sample Python Program

> Sample Project to Test Dependency Management. The script will use Pandas to fetch and parse HTML tables from Power10 website and output the number of tables found.

##### 1. **Copy** code below into a code cell (create a notebook if you don't have one in your project yet) and ***Run*** the code cell.

```python
import pandas

url = "https://www.thepowerof10.info/rankings/rankinglist.aspx?event=100&agegroup=ALL&sex=W&year=2020"

dfs = pandas.read_html(url)

len(dfs)
```

##### 2. You'll notice an error, if you scroll down, you'll see it's a missing package called ```lxml```. To install ```lxml``` via ```pipenv```, you can either open a project Terminal and use the CLI (Command Line):

```bash
$ pipenv install lxml --skip
```

##### 2. Or, simply add ```lxml``` to the project's ```Pipfile``` and restart the **project machine (Environment Tab)**:

```
[packages]
pandas = "*"
lxml = "*"
```

##### 3. Restart the notebook and re-run the code cell.  If you get ***unexpected errors*** even after ***installing the new package***, ***restart*** the **project machine (Environment Tab)**.

**Note**: Remove dependencies with ```pipenv uninstall``` e.g. ```pipenv uninstall lxml```.

## Sample Python Program

> Sample Project to Test Dependency Management. The script will use Pandas to fetch and parse HTML tables from Power10 website and output the number of tables found.

##### 1. **Copy** code below into a code cell (create a notebook if you don't have one in your project yet) and ***Run*** the code cell.

```python
import pandas

url = "https://www.thepowerof10.info/rankings/rankinglist.aspx?event=100&agegroup=ALL&sex=W&year=2020"

dfs = pandas.read_html(url)

len(dfs)
```

##### 2. You'll notice an error, if you scroll down, you'll see it's a missing package called ```lxml```. To install ```lxml``` via ```pipenv```, you can either open a project Terminal and use the CLI (Command Line):

```bash
$ pipenv install lxml --skip
```

##### 2. Or, simply add ```lxml``` to the project's ```Pipfile``` and restart the **project machine (Environment Tab)**:

```
[packages]
pandas = "*"
lxml = "*"
```

##### 3. Restart the notebook and re-run the code cell.  If you get ***unexpected errors*** even after ***installing the new package***, ***restart*** the **project machine (Environment Tab)**.

**Note**: Remove dependencies with ```pipenv uninstall``` e.g. ```pipenv uninstall lxml```.

## Customisation (Deepnote)
> Customise your Deepnote experience with ```init.ipynb``` e.g. in another code cell below your dependencies code cell

#### Git Alliases

```bash
%%bash
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

## Duplicating your Template Project
> Once you're happy with your Project you can simply duplicate it to use it as a Template. Duplicating the project will also copy over the custom ```Dockerfile``` and ```init.ipynb```. to your new project.

##### 1. Open your project template on Deepnote and click the ***dropdown*** next to the ***project name*** in the ***header***.

##### 2. Click the ```Duplicate project``` button to create a new project from your template. If you want to ***edit*** the custom environment, you'll have to revert back to default and build a new one.

##### 3. Optionally, you can create additional Deepnote projects, based off this template, that will relate to different solution. E.g. you could have a project template called ```Web Scraping Template``` that will have additional default packages or configurations that relate specifically to web scraping (e.g. nerodia, lxml, driver install step). Now when you start a new web scraping project, you could simply duplicate your web scraping template.

##### 4. See [EPL Web Scraper - Deepnote](https://deepnote.com/project/19f51d7b-ae79-4c51-906c-dee0138da144) project for example.

## 3rd Party Integrations

> If your project will need some sort of 3rd party integration, e.g. Accessing files from AWS S3 bucket or a collection from a MongoDB cluster, we strongly reccommend testing these integrations before moving on with your project. Feel free to use/copy the sample code in [```sample_notebook.ipynb```](./sample_notebook.ipynb) to include a sample notebook in your templates.