# Send a message multiple times

Send a message multiple times to someone on WhatsApp

> Tested on WhatsApp desktop app Windows 11

## Optional

Setup a virtual environment

```bash
python -m venv venv
```

And activate it

### Windows

Via Powershell

```bash
./.venv/Scripts/Activate.ps1
```

Via cmd

```bash
./.venv/Scripts/Activate.bat
```

### WSL / Linux

```bash
source ./.venv/Scripts/activate
```

## Install requirements

Install requirements

```bash
pip install -r requirements.txt
```

## Run

> This version will resend the message 500 times, this can be chnaged in the for loop code to the number of times of your choice

> Remember, you have 8 seconds to open the WhatsApp chat and click on the typing area. Now just wait for it to complete

```bash
python bomb.py
```
