# gradio_setup

Gradio setup notebook for Nurnberg ML course

- [ ] create a space
- [ ] try basic interface
- [ ] try in notebook
- [ ] use an experted learner
- [ ] use nbdev
- [ ] try the API in Github Pages

## Hugginface spaces deployment

**Select gradio backend** when creating your huggingface spaces

To deploy this on Huggingface spaces

1. create a new huggingface spaces directory:
```bash
git clone https://huggingface.co/spaces/[USER_NAME]/[SPACE_NAME]
```

2. add an app.py file with the gradio interface to the huggingface space
```bash
git add app.py
git commit -m "Add application file"
git push
```

