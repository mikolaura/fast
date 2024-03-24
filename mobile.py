
from PIL import Image
import requests
from fastapi import FastAPI
app = FastAPI()
import json
from ultralytics import YOLO
@app.post("/pred")
def pred(url: str):
    image = Image.open(requests.get(url, stream=True).raw)
    #     transforms.Resize((640, 640)),
    # transforms.PILToTensor()])

    # torch_image = transform(image)
    model = YOLO("best.pt")

    result = model.predict(image)
    names = model.names
    res = []
    for r in result:
        
        for c in r.boxes.cls:
            res.append(names[int(c)])
    some_dict = {"results": res}
    return json.dumps(some_dict, indent=4, default=str)