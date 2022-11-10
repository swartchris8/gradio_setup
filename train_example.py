from fastai.vision.all import *

path = untar_data(URLs.PETS)

dls = ImageDataLoaders.from_name_re(
    path, get_image_files(path/'images'), 
    pat='(.+)_\d+.jpg', item_tfms=Resize(230), 
    batch_tfms=aug_transforms(size=224, min_scale=0.75)
)

learn = vision_learner(dls, models.resnet18, metrics=accuracy)
learn.fine_tune(1)

learn.path = Path('.')
learn.export()

