# pre-commit-hooks

This repo contains (mirrors of) various pre-commit hooks used by Penn Labs. We are using [pre-commit](https://pre-commit.com/) to handle the installation of these hooks.

The [template repositories](github.com/pennlabs/templates) provided by Penn Labs contain config files to enable suggested pre-commit hooks.

## Installation

* Install pre-commit `pip3 install pre-commit`
* `cd` into a repository with a defined `.pre-commit-config.yaml`  and run `pre-commit install`

Now the defined pre-commit hooks will run whenever you attempt to make a commit in that repository.

## Usage

After installing the pre-commit hooks, use git as you normally would. The only difference is when trying to run a `git commit` you should see something like this:

```bash
detect-private-key.............................................Passed
black..........................................................Passed
isort..........................................................Failed
```

If all the hooks pass, then the commit will be created exactly as if you didn't have any hooks installed. However, if there's a failure, you'll have to fix the issues before being able to commit. Some of the hooks will autofix issues for you, in order to see what they changed, just run `git diff`
