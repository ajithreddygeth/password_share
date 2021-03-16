# PASSION
Safe password and sensitive data sharing.

## How it works?
This is a safe password sharing application.
Just paste a password or some sensitive data into the text field and you will get a "password withdrawal" URL.
Share this URL through any usual channel.

## Is it safe?
Yep, your data is being encrypted in clients browser so no sensitive information is sent via HTTP.
Encrypted passwords are deleted from server after the first withdrawal.
Even if the password is not withdrawn, it will expire automatically.

## Install
- Clone this repository
- Rename `config.dist.py` file to `config.py`
- Edit configuration file to meet your needs
- Run `make build`

## Run
- Jump into the virtual environment `source .venv/bin/activate`
- Run `python3 index.py` 
