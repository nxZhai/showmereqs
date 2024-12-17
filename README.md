# ShowMeReqs

A lightweight command-line tool that generates requirements.txt by analyzing import statements in your Python projects.

## Features

-   Intelligent third-party import detection
-   Automatic requirements.txt generation with precise versions
-   Display missing packages in current environment
-   Display import names that differ from PyPI package names for manual review
-   Clean and intuitive CLI interface

## Installation

Install via pip:

```bash
pip install showmereqs
```

## Usage

Generate requirements.txt for current directory:

```bash
showmereqs .
```

Or specify a project path:

```bash
showmereqs path/to/your/project
```

## Examples

-   #### Normal Output

![Normal Output](docs/images/normal_output.png)

-   #### Special Cases Detection

![Special Cases](docs/images/special_cases.png)

The tool will:

-   Mark packages not found in current environment
-   Highlight import names that differ from their PyPI package names
-   Generate a clean requirements.txt file or a detail one

## Why ShowMeReqs?

Traditional approaches like `pip freeze` capture all environment dependencies, while modern tools like Poetry can be overly complex for simple needs. ShowMeReqs bridges this gap by offering a streamlined solution that identifies only the dependencies your project actually uses.

Additionally, once ShowMeReqs generates the initial requirements.txt, you can easily migrate to modern package management tools for more comprehensive dependency management.

## Acknowledgments & License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.

ShowMeReqs uses package mapping and stdlib data from [pipreqs](https://github.com/bndr/pipreqs/tree/master) under the Apache 2.0 license. As pipreqs development has slowed, ShowMeReqs aims to provide an actively maintained alternative for the Python community.

## Roadmap

Future releases will include:

-   Additional CLI options for customization
-   Support for excluding specific packages or directories
-   Version range specifications
-   Integration with other package management tools

Feel free to open issues for feature requests or bug reports.
