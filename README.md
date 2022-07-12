# TrainTTS

TrainTTS is a script to monitor British train stations on the network rail system for departing/arriving or passing trains.

TrainTTS uses [TransportApi](transportapi.com) to get train information. 
**TrainTTS is only accurate by the minute, and is less accurate for passing trains**

``Warning: TrainTTS may have bugs on larger stations``


## Setup and Configuration 


To continue, you must have a TransportAPI API key. Including the ``app_id`` and ``app_key`` fields.

You can get a free API key here: [TransportAPI Developer Portal](https://developer.transportapi.com/)

**Once you have the ``app_id`` and ``app_key`` you can create a ``config.json`` file in this folder**
```json
// config.json

{
    "appId": "eea4cfc3",
    "appKey": "7995a63fce1941ee469c3a3e5dda54c5"
}

```

**Also please install the following dependencies:**
```
pyttsx3
```

**If you are having errors and you are using windows please install:**

```
pypiwin32
```

# Starting the application

Once you have finished setting up the config file, you can run the main.py file.