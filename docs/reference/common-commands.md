

## `conda smithy`

```bash
conda smithy rerender --feedstock_directory ./foo-feedstock
```

!!! note "Concerning the `conda-forge.yml`"
    A change to the `conda-forge.yml` file will not automatically trigger a re-rendering of the feedstock. To have the changes to `conda-forge.yml` reflected in the feedstock, you need to manually update the file and then re-render the feedstock.

## `mkdocs`

```bash
mkdocs new [dir-name]  # Create a new project.
```

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


```bash
mkdocs serve  # Start the live-reloading docs server.
```

```bash
mkdocs build  # Build the documentation site.
```

```bash
mkdocs -h     # Print help message and exit.
```

!!! reference "Further reference"
    - [MkDocs: Project documentation with Markdown](https://www.mkdocs.org)


## Project layout

