from fastai.vision.all import *

learn = load_learner('export.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

import gradio as gr

gradio_interface = gr.Interface(
    fn=predict,
    inputs=gr.inputs.Image(shape=(512, 512)),
    outputs=gr.outputs.Label(num_top_classes=3),
    examples=["cat.jpeg", "dog.jpeg", "catdog.jpeg"]
)
gradio_interface.launch()