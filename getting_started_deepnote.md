## Python Project Setup (Deepnote)
> Best Practices for setting up a Python Project Template on Deepnote

![deepnote](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/Links/deepnote.jpg)

## Deepnote
> Create a Deepnote Project (to act as your template)

#### 1. If you haven't already, take the time to read the [Deepnote Docs](https://docs.deepnote.com/), it really isn't long or complicated!

#### 2. Create a **Deepnote Project** called ```python_project_template```. 

#### 3. Join their **Community**!

+ **Note** that you can access the **command palette** and various other **resources** via the **icons** on the **bottom left** of your project **sidebar** e.g. ***link to join their community***.

#### 4. To create a template that is Github friendly, we'll want to include some of ther usual repo suspects e.g. ***Gitignore***, ***Readme***, ***Contributing Guide*** (and ***LICENCE*** if applicable).

### ```Readme.md```
> Below is a template for a good basic Readme. Please use it. 

Also see the [```Readme```](./Readme.md) to this project which is written off the template below. Even if you don't know the full extent of your project, it's good practise to set up a Readme template that you can easily **edit as you progress**.

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

> Instructions for contributing to the project. See [contributing.md](./contributing.md)
```

> If you want to provide some **contribution guidelines**, create a **```contributing.md```** file within the root of your project. Check out our **sample [```contributing.md```](./contributing.md)** file.

### ```.gitignore```
> Ignoring ```.deepnote``` folder/files and ```init.ipynb``` file with Gitignore file.

We reccommend simply including [Github's Python Gitignore Template](https://github.com/github/gitignore/blob/master/Python.gitignore). If you want to build your template with the deepnote project root as our actual project root, you'll have to add a couple files within our deepnote environment that we don't need version controlled.

```
# Deepnote files
.deepnote/
init.ipynb
```

## Dependencies & Customisation
> Dealing with project dependencies (packages the project will depend on)

Handling Python project **dependencies** (packages, python version etc) locally is ***virtually*** the same on Deepnote. One difference is that Deepnote already has it's own dependencies pre-installed, meaning we don't have to install commonly used packages like ```pandas```. See [```init.ipynb```](./init.ipynb) for more info. 

### ```requirements.txt```

It's good practice to track the ***dependencies*** of our projects via a ```requirements.txt``` file or ```Pipfile```. The [Documentation](https://docs.deepnote.com/environment/python-requirements) suggests using ```pip``` and a ```requirements.txt``` file so your project pacakages are loaded (via ```init.ipynb```) into your Deepnote project everytime you open it. You can also easily install and add packages to your projects on demand via your notebooks e.g.

![deepnotePip](https://mcusercontent.com/c977a94491aefa0b53bca6f72/images/798ac624-85a6-43c7-a7e7-1ce794be3924.gif)

### ```init.ipynb```

Example of cusomisation via ```bash``` and ```init.ipynb``` (setting Git Aliasas for the Commmand Line). Simply place the code block below into a new code cell within your projects ```init.ipynb```.

```bash
%%bash
# Git Aliases to make you feel at home
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```
### ```Dockerfile```
> Read more about **custom environments** and the **Dockerfile** in the [documentation](https://docs.deepnote.com/environment/custom-environments).

Installing dependencies via ```pip``` during your projects initialisation phase can increase the time it takes to load your projects after a restart. An alternative way of dealing with our environment dependencies in Deepnote is via the ```Dockerfile``` e.g. we can ***build*** an environment with ```chromium-driver``` pre-installed like so:

```dockerfile
FROM ..
RUN sudo apt-get update
RUN pip install chromium-driver -y
```

## Duplicating your Template Project
> Once you're happy with your Template Project you can simply duplicate it to use it as a base for your next Python project. Duplicating the project will also copy over any customisations to ```Dockerfile``` and ```init.ipynb```. e.g.

#### 1. Open your project template on Deepnote and hover/click the ***project title*** (in the ***header***).

#### 2. Click the ```Duplicate project``` button to create a new project from your template. If you want to ***edit*** the Dockerfile, it's best to revert back to default, then build a new one.

#### 3. To get version controlling, create a new (empty) Github repo, copy it's ***ssh*** and link it via your new project's Github integration. **Move the ```.git``` folder** (and any additional files e.g. LICENCE) **into your project root** and **delete the cloned folder**.

#### ***Tip:*** You can create additional Deepnote projects, based off this template, that will relate to different solutions. E.g. you could have a project template called ```Web Scraping Template``` that will have additional default packages or configurations that relate specifically to web scraping (e.g. ```nerodia```, ```lxml```, ```chromium-driver```).

#### ***Note:*** See this [EPL Web Scraper](https://deepnote.com/project/19f51d7b-ae79-4c51-906c-dee0138da144) project as an example. If you want to test out your Template, try it with our sample Python Project below!

## Sample Python Project

> Sample Project to Test your Template. Uses Pandas to fetch and parse HTML tables from Power10 website and output the number of tables found.

#### 1. **Copy** code below into a code cell (create a notebook if you don't have one in your project yet) and ***Run*** the code cell.

```python
import pandas

url = "https://www.thepowerof10.info/rankings/rankinglist.aspx?event=100&agegroup=ALL&sex=W&year=2020"

dfs = pandas.read_html(url)

len(dfs)
```

#### 2. Install the missing ```lxml``` pacakge e.g. run the following command in a code cell and follow prompts to delete the cell and add it to ```requirements.txt```:

```bash
!pip install lxml
```

**Note**: Remove dependencies with ```pip uninstall``` or delete them from ```requirements.txt```.

#### 3. If you restart your notebook (once ```lxml``` has been installed), it should run smoothly and output a number 🎉 
