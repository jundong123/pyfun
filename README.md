# p01_mod_arg

A simple demo project showing:

* Python package and subpackage structure
* Command-line arguments with `argparse`
* Running packages with `python -m`
* Execution order of `__init__.py` and `__main__.py`
* A simple Git branching workflow

## Git Branches

* `main` – stable release
* `dev` – development branch
* `fea-*` – feature branches

## Getting Started

Clone the repository:

```bash
git clone https://github.com/jundong123/pyfun.git
cd pyfun/p01_mod_arg
```

Set `PYTHONPATH`:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

You can now run the demo from **any directory**.

## Run

Show help:

```bash
python -m packages.mod_arg -h
```

Try different command-line options:

```bash
python -m packages.mod_arg
python -m packages.mod_arg -d
python -m packages.mod_arg -t
python -m packages.mod_arg --cfg config.yaml
```

## Notes

* `python -m` runs a Python **package/module**, not a file.
* Use package notation with **`.`**, not file paths with `/`.

```text
packages.mod_arg    ✓
packages/mod_arg    ✗
```

* Observe the execution order of `__init__.py` and `__main__.py`.
* Compare `python script.py` with `python -m packages.mod_arg`.
* This package structure is recommended for medium and large Python projects because it supports clean imports, modular code, and easier maintenance.
