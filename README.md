# [EuroPython 2023] From Jupyter Notebooks to a Python Package: The Best of Both Worlds

A Jupyter notebook is quite handy for rapid REPL (Read-Eval-Print-Loop) style tasks
such as exploratory data analysis. However, we would feel deficiencies in
proper SW engineering supports at some point as the notebook grows
to have larger and more complicated code. It is because the Jupyter notebook lacks
several important features including code sharing, refactoring support,
*git* integration and advanced editing. Fortunately, traditional full-fledged IDEs,
such as *VS Code* or *PyCharm*, are available at hand and they support
these lacking features very well.
Then, why don’t we take advantage of the best of both worlds?

In this beginner-level hands-on talk, I will demonstrate how to
transform a Jupyter notebook workflow to a proper Python package using *VS Code*.
I will also introduce several basic but essential refactoring recommendations.
By doing so, you can use the refactored package for several notebooks
and even share with your colleagues and friends.

## Target Audience

- Jupyter notebook beginner
- Python beginner

## Outline

### Introduction

- Full-fledged IDEs (Before Jupyter Notebook)
  - *VS Code*, *PyCharm*, *Spyder*, etc.
  - One iteration takes a long journey
- With Jupyter notebook
  - Pros: REPL, interactivity, visualization, rapid prototyping, result sharing, etc.
  - Cons: code sharing, refactoring support, *git* integration, advanced editing, etc.
- IDE and Jupyter Notebook are not exclusive. We can benefit from the best of both worlds.

### Data Science Workflow with Jupyter

- REPL (Read-Eval-Print-Loop)
- Simple Refactoring
  - Repeated code to functions
  - Put everything in order
- How about multiple notebooks that requires the same functions?
  - Easy but dirty way: ctrl+c -> ctrl+v

### To (Your Own) Package

- Why? Benefits
- Module (a Python file)
- Package
  - A directory containing a *\__init__.py* file
  - Other settings to be a proper package
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

Sin-seok SEO @Safran Tech, Safran SA

- [Webpage](https://sesise.webflow.io/)
- [LinkedIn](https://www.linkedin.com/in/sin-seok-seo-9a470949/)
- [GitHub](https://github.com/sesise0307)
