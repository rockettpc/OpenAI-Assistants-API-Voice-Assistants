# Clone Repo
```
git clone https://github.com/rockettpc/OpenAI-Assistants-API-Voice-Assistants.git
```

## CD into directory
```
cd OpenAI-Assistants-API-Voice-Assistants
```
Optionally rename it to something shorter and customized to your needs.

## Create a virtual environment
```
python3 -m venv voice_assistant_venv
```

## Activate virtual environment
```
source voice_assistant_venv/bin/activate
```

## Install requirements
```
pip3 install -r requirements.txt
```

## Customize assistant
You will need to obtain and insert your OpenAI API key into the utils.py file as well as your Assistant ID and Thread ID and save the file

## Run the voice assistant
```
python3 tts.py
```
Now you should be able to CTRL click the url in the terminal and test your voice assistant

### Deactivate virtual environment
```
deactivate
```
