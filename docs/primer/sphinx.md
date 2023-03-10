# Sphinx Documentation

``` 
sudo apt-get install  texmaker gummi texlive texlive-full texlive-latex-recommended latexdraw intltool-debian lacheck libgtksourceview2.0-0 libgtksourceview2.0-common lmodern luatex po-debconf tex-common texlive-binaries texlive-extra-utils texlive-latex-base texlive-latex-base-doc texlive-luatex texlive-xetex texlive-lang-cyrillic texlive-fonts-extra texlive-science texlive-latex-extra texlive-pstricks
```

<div class="todo">

- Link checking is facilitated by sphinx using `make linkcheck` (on
  windows)
- Add section on FontAwesome inline icons from `sphinx-panels`
- <https://fontawesome.com/>
- Add tutorial/ section on maintaining a bibliography in Sphinx.

</div>

## Compile documentation with Sphinx

This example is a step-by-step guide on how to compile the tudat
documentation locally on your system using `sphinx`. This procedure
works to compile documentation for both the
[tudat-space](https://docs.tudat.space/en/latest/) and the documentation
you are currently reading.

<div class="note">

<div class="title">

Note

</div>

This procedure requires that Anaconda or Miniconda is installed. For
information regarding the use of the conda ecosystem, please see
`Getting Started with Conda`.

</div>

1.  Create an environment that will be satisfy all dependencies required
    for building documentation, then activate it. This can be done by
    downloading this `environment.yaml`
    (`yaml <_static/environment.yaml>`), which will install the
    `tudat-docs` conda environment.

``` bash
conda env create -f environment.yaml & conda activate tudat-docs
```

2.  Enter the root directory of a repository containing a `docs`
    directory, which contains a `source` subdirectory. The following
    command is specific to cloning and entering the `tudat-space`
    repository.

``` bash
git clone https://github.com/tudat-team/tudat-space.git & cd tudat-space
```

3.  Build the documentation using the `sphinx-build` command, specifying
    that html is to be built with the supplied source and output build
    directory.

``` bash
sphinx-build -b html docs/source docs/build
```

4.  View the local build of the documentation by opening the
    `docs/build/index.html` with your preferred browser.

<div class="tip">

<div class="title">

Tip

</div>

**\[PyCharm/CLion\]** You can do this in by right clicking `index.html`
in the Project tree and selecting `Open with Browser`.

</div>

### Compiling Documentation in PyCharm

If you are using PyCharm, the compilation of the documentation after
each edit can be simplified by setting up a run configuration tailored
for sphinx. The procedure is described below.

1.  From the main toolbar, click on `Run > Edit Configurations`;
2.  In the window that has just opened, click on the `+` button
    (upper-left) to add a new configuration;
3.  From the drop-down menu, select `Python docs > Sphinx task`;

<figure>
<img src="_static/sphinx_config_pycharm_step1.png" class="align-center"
width="200" />
</figure>

4.  Give a name to the new run configuration;
5.  Make sure that the field `Command` is set on `html`;
6.  For the `input` and `output` fields, select the `source` and `build`
    folders respectively.

![](_static/sphinx_config_pycharm_step2.png)

Make sure that the correct run configuration is selected. If so,
pressing *Run* will be equivalent to executing the following command
from the command line:

``` bash
sphinx-build -b html docs/source docs/build
```

## Troubleshooting

In this section, we collect the most recurring bugs that can happen
while using sphinx, hoping that it will save precious time to future
Tudat contributors.

### No changes shown in browser

It happens often that the browser shows cached data instead of the
updated html files. As a result, if you don't see your changes, try to
empty/delete the cache of your browser (see, e.g., this
[guide](https://its.uiowa.edu/support/article/719)).

### No changes shown in online docs

It can happen that, after pushing your changes to the `origin`
repository, no changes are shown on the actual website (e.g., on
tudat-space or on this website). Some suggestions to identify the
problem will follow:

1.  Check that you pushed to the `main` branch. The documentation is
    built by readthedocs only if changes are pushed to that branch.
2.  Check that the build was successful. This can be monitored via the
    "Builds" link in the [readthedocs_menu]() (see screenshot above). If
    the build was not successful, you can click on it and see the output
    of the build. This can be helpful to identify where things are going
    wrong.

<figure>
<img src="_static/build_output.png" class="align-center" width="600" />
</figure>

### Sphinx commands not working

If a sphinx command does not work, for instance the following:

``` 
.. toctree::
   intro
   guide
```

it can be due to many things, but before going crazy into debugging
mode, check that the amount of spaces before `intro` and `guide`
correspond to three empty spaces. Sphinx requires *three* empty spaces,
but the tab key corresponds to *four* empty spaces: if you use it in
sphinx commands, it can generate a lot of confusion because the extra
white space will break the sphinx command and it is *very* difficult to
notice as well. To be clear, this will likely **not** work:

``` 
.. toctree::
    intro
    guide
```
