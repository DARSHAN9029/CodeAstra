import requests
import json
import gradio as gr
import os

url="http://localhost:11434/api/generate"

headers={
    'Content-Type':'application/json'
}


#backend of the chatbot
history=[]
def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model":"CodeAstra",
        "prompt":final_prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("ERROR:",response.text)

#interface
port=int(os.environ.get('PORT',10000))

interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch(server_name="0.0.0.0",server_port=port)