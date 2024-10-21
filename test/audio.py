import requests
import json
import pyaudio
import flet as ft

def vvox_test(text):
    # Start your voicebox engine.
    host = "localhost"
    port = 50021
    
    params = (
        ('text', text),
        ('speaker', 14),
    )
    

    query = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params
    )

    synthesis = requests.post(
        f'http://{host}:{port}/synthesis',
        headers = {"Content-Type": "application/json"},
        params = params,
        data = json.dumps(query.json())
    )
    

    voice = synthesis.content
    pya = pyaudio.PyAudio()
    
    stream = pya.open(format=pyaudio.paInt16,
                      channels=1,
                      rate=24000,
                      output=True)
    
    stream.write(voice)
    stream.stop_stream()
    stream.close()
    pya.terminate()
    
   
def main(page: ft.Page):

    text = ft.Ref[ft.TextField]()

    def btn_click(e):
        vvox_test(apple)
        text.value = ""
        page.upgrade
        text.focus()
    page.add(
        ft.TextField(ref=text label="しゃべらせる文章ぷりーず", autofocus=True)
        ft.ElevatedButton("Speak", on_click=btn_click),
    )
    
        

ft.app(target=main)