# [EuroPython 2023] From Jupyter Notebooks to a Python Package: The Best of Both Worlds

A Jupyter notebook is quite handy for rapid REPL (Read-Eval-Print-Loop) style tasks
such as exploratory data analysis and data science. However, we would feel
deficiencies in proper SW engineering supports at some point as the notebook grows
to have larger and more complicated code. It is because the Jupyter notebook lacks
several important features including code sharing, refactoring support,
version control and advanced editing. Fortunately, traditional full-fledged IDEs,
such as *VS Code* or *PyCharm*, are available at hand and they support
these lacking features very well.
Then, why don’t we take advantage of the best of both worlds?

In this beginner-level hands-on talk, I will demonstrate how to
transform Jupyter notebook workflows to a proper Python package using *VS Code*.
I will also introduce several basic but essential refactoring recommendations.
By doing so, you can use the package for several notebooks
and even share with your colleagues and friends.

## Target Audience

- Jupyter notebook beginner
- Python beginner

## Outline

### Introduction

- Jupyter Notebook
  - Provides ideal workflows for data science
  - Pros: REPL, interactivity, integration of code / output / documentation,
    visualization, rapid prototyping, result sharing, etc.
  - Cons: lacks of debugging, code sharing, refactoring, version control,
    advanced editing, etc.
- Full-fledged IDEs
  - Designed to maximize programmer productivity
  - One iteration might take a long journey
- We can benefit from the best of both worlds
  by using Python packages

### Jupyer Notebook Data Science Workflow

- [Data Loading](./notebook/1_data_loading.ipynb)
- [Preprocessing](./notebook/2_preprocessing.ipynb)
- [Exploratory Data Analysis (EDA)](./notebook/3_EDA.ipynb)
- [Prediction](./notebook/4_prediction.ipynb)

### To (Your Own) Package

- What is a package and why we do we want to use it?
- How to create a package
- (Essential) Refactoring
  - Naming and coding style (PEP8, *black*)
  - Code structure
- How to (properly) import in a Jupyter notebook
  - Based on local dependency
  - *sys.path.append()*
  - Install as a library: *pip install **-e** [DIR]*
  - *autoreload* magic command in a Jupyter notebook
- Make it available to the world: *pypi*

### Conclusion

- Some tips and references

## Contact

Sin-seok SEO@Safran Tech, Safran SA

- [Webpage](https://sesise.webflow.io/)
- [LinkedIn](https://www.linkedin.com/in/sin-seok-seo-9a470949/)
- [GitHub](https://github.com/sesise0307)
