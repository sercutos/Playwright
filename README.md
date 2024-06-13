# Testing Frontend OpenECOE plataform using Playwright

## Check NODEJS
- node --version
- npm --version
## Clone repository.

- git clone https://github.com/sercutos/Playwright
## Create environment folder: 
python -m venv .\venv\ 
.\venv\Scripts\activate
## VScode plugin recommended:
- Playwright Test for VSCode
## Install dependencies:
- pip install pytest-playwright
- playwright install
- pip install -r requirements.txt
## UPGRADE playwright if it's necessary
-pip install pytest-playwright playwright -U
## Commands:
- pytest (play all test together)
- pytest <name_of_test> (play one by one test)
- pytest --ff <test_name>.py (Execute test without  cache)

