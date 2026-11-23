# AI Engineering Journey

Hello, I am Awshaf Ahmath.
This repository documents my learning journey as I prepare for AI engineering internships.

## Install pytest

- The virtual environment must be active:

```bash
source .venv/bin/activate
pip install pytest
pytest --version
```

## Run the tests

- Run this from the repository root (the `ai-engineering-journey` folder):

```bash
pytest lesson03 -v
```

- `-v` shows the name of each test.

## Lesson 04

- Install all project dependencies from the repository root:

```bash
pip install -r requirements.txt
```

- or install `requests` directly:

```bash
pip install requests
```

- No API key is needed. GitHub allows about 60 requests per hour without a key.
- Run github_user.py with a GitHub username (for example, octocat):

```bash
    python lesson04/github_user.py octocat
```

- Run the Lesson 04 tests:

```bash
    pytest lesson04 -v
```
