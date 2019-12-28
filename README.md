# pre-commit-hooks

This repo contains (mirrors of) various pre-commit hooks used by Penn Labs. We are using [pre-commit](https://pre-commit.com/) to handle the installation of these hooks.

The [template repositories](github.com/pennlabs/templates) provided by Penn Labs contain config files to enable suggested pre-commit hooks.

## Installation

* Install pre-commit `pip3 install pre-commit`
* `cd` into a repository with a defined `.pre-commit-config.yaml`  and run `pre-commit install`

Now the defined pre-commit hooks will run whenever you attempt to make a commit in that repository.
