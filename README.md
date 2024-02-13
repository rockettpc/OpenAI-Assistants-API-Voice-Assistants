# OpenAI Assistants API Voice Assistant
This project is currently under development. I found the orignal code repo at https://github.com/sohail8611/voice_assistant_with_openai.git

I thought it was a pretty cool idea and it fits a specific need for a custom voice assistant that can use OpenAI's Assistants API. You need to login to platform.openai.com and create an assistant, give it your custom instructions, enable the features you want it to use and add files if you want to have a custom knowledge base. This project requires an OpenAI API key and the Assistants ID as well as a Thread ID to use.

### Note: The OpenAI API is a paid service. Please ensure you are aware of the costs associated with its use.

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

## index.html Structure:

The code starts with a basic HTML structure declaration.
It sets the language to English using lang="en".
The <head> section is present where metadata and CSS/JavaScript links are often included. However, this part is not shown in the provided code snippet.
CSS styling:

The CSS styles defined in the <style> section:
Styles the body to have no margin, centered content, a specific background color, and a font family.
Styles the #assistant-container to have centered text.
Styles the #assistant_heading to have a large font size.
Styles the #microphone-button which is a circular button with specific dimensions, colors, and cursor style.
Defines an animation class .listening for the microphone button which creates a pulsating effect.
The @keyframes rule defines the animation behavior for the pulsating effect.
HTML body:

Contains a <div> with the id assistant-container which holds a microphone button (<button id="microphone-button">) and a paragraph with the id assistant_heading displaying the heading text.
JavaScript functionality:

Within the <script> tag:
It waits for the DOM content to be fully loaded before executing the JavaScript code.
It initializes variables for handling speech recognition and audio recording.
Checks if the required APIs (webkitSpeechRecognition and MediaRecorder) are supported by the browser.
Sets up the speech recognition and audio recording functionality.
Defines functions for handling the end of audio playback and sending audio data to a server.
Adds an event listener to the microphone button for starting/stopping the recognition and recording processes.
Runtime behavior:

When the microphone button is clicked, it starts/stops the speech recognition and audio recording processes based on the current state.
Once audio data is captured, it is sent to a specified server endpoint using a POST request.
The response from the server is processed to play the received audio and execute additional actions when the audio playback ends.
Overall, this code snippet combines HTML, CSS, and JavaScript to create a simple web interface for voice input using the browser's Web Speech API and MediaRecorder API. It allows users to interact with a voice assistant through a microphone button on the webpage.
