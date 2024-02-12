# OpenAI Assistants API Voice Assistant
This project is currently under development. I sound the orignal code repo at https://github.com/sohail8611/voice_assistant_with_openai.git

I thought it was a pretty cool idea and it fits a specific need for a custom voice assistant that can use OpenAI's Assistants API. You need to login to platform.openai.com and create an assistant, give it your custom instructions, enable the features you want it to use and add files if you want to have a custom knowledge base. This project requires an OpenAI API key and the Assistants ID as well as a Thread ID to use.

### Clone Repo
```
git clone https://github.com/rockettpc/OpenAI-Assistants-API-Voice-Assistants.git
```

### CD into directory
```
cd OpenAI-Assistants-API-Voice-Assistants
```
Optionally rename it to something shorter and customized to your needs.

### Create a virtual environment
```
python3 -m venv voice_assistant_venv
```

### Activate virtual environment
```
source voice_assistant_venv/bin/activate
```

### Install requirements
```
pip3 install -r requirements.txt
```

### Customize assistant
You will need to obtain and insert your OpenAI API key into the utils.py file as well as your Assistant ID and Thread ID and save the file

### Run the voice assistant
```
python3 tts.py
```
Now you should be able to CTRL click the url in the terminal and test your voice assistant

### Deactivate virtual environment
```
deactivate
```
