@echo off
start "" ".\vv-engine\run.exe"
python3 -m pip install --upgrade pip
python3 -m pip install git+https://github.com/huggingface/accelerate
python3 -m pip install datasets
python3 -m pip install transformers
python3 -m pip install torch
python3 -m pip install json
python3 -m pip install requests
python3 -m pip install pyaudio
python3 -m pip install bs4
python main.py