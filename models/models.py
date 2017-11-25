import torch

def create_model(opt):
    from .label2img_model import Label2ImgModel
    model = Label2ImgModel()    
    model.initialize(opt)
    print("model [%s] was created" % (model.name()))

    if opt.isTrain and len(opt.gpu_ids):
        model = torch.nn.DataParallel(model, device_ids=opt.gpu_ids)

    return model
