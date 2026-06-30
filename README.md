p01_mod_arg:
    * Show how to code input argument
    * How to code and run module and sub-module
    * git branchs:
        - main: the main release
        - dev: in development for next release
        - fea: other team member working on
    * How to run the demo:
        - git clone https://github.com/jundong123/pyfun
        - cd p01_mod_arg
        - export PYTHONPATH=$PYTHONPATH:`pwd`
        - cd {any_where_you_want}
        - python -m packages.mod_arg -h  # for help info
        - # try different input arguments
    * Notes:
        - the code run order, especially "__init__" functions
        - python "-m" option
        - packages.mod_arg, it is "." here, not "/"
        - why and when to use this frame?


