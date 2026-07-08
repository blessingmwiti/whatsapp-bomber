# Send a message multiple times

Send a message multiple times to someone on WhatsApp

> Tested on WhatsApp desktop app

## Recommended

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

### Update the copy and paste shortcut command according to your OS.

> Mac OS shortcut is currently set. Just comment it and uncomment the Windows/Linux method

## Run

> This version will resend the message 100 times, this can be changed in the for loop code to the number of times of your choice

> Remember, you have 5 seconds to open the WhatsApp chat and click on the typing area. Now just wait for it to complete

```bash
python3 bomb.py
```
