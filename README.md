
## setup
. cd my_project

# in case you want to add projects
. uv add requests pandas jupyter ipykernel
. uv sync

# go to the source part
source .venv/bin/activate

# create kernel for it to be runned 
python -m ipykernel install --user --name=nyc_use_case --display-name "Python (nyc use case)"
