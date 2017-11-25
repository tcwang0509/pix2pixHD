# label2img

Pytorch implementation for turning semantic label maps to photo-realistic images, for example:

## Prerequisites
- Linux or macOS
- Python 2 or 3
- NVIDIA GPU (12G or 24G memory) + CUDA CuDNN

## Getting Started
### Installation
- Install PyTorch and dependencies from http://pytorch.org
- Install Torch vision from the source.
```bash
git clone https://github.com/pytorch/vision
cd vision
python setup.py install
```
- Install python libraries [dominate](https://github.com/Knio/dominate).
```bash
pip install dominate
```
- Clone this repo:
```bash
git clone https://github.com/tcwang0509/label2img
cd label2img
```

### Dataset
- We use the Cityscapes dataset. Please download it from https://www.cityscapes-dataset.com/ (registration required).
A sample subset can be downloaded from (TODO).
After downloading, please put it under the `datasets` folder.

### training
- Train a model (`bash ./scripts/train_512p_label.sh`):
```bash
#!./scripts/train_512p_label.sh
python train.py --name label2city_512p
```
- To view training results and loss plots, please see tensorboard logs in `./checkpoints/label2city_512p/logs`. To see more intermediate results, check out  `./checkpoints/label2city_512p/web/index.html`

### multi-GPU training
- Train a model using multiple GPUs (`bash ./scripts/train_512p_label_multigpu.sh`):
```bash
#!./scripts/train_512p_label_multigpu.sh
python train.py --name label2city_512p --pool_size 1 --batchSize 8 --gpu_ids 0,1,2,3,4,5,6,7
```

### training at full resolution
- To train the images at full resolution (2048 x 1024) requires a GPU with 24G memory (`bash ./scripts/train_1024p_label_24G.sh`).
If only GPUs with 12G memory are available, please use the 12G script (`bash ./scripts/train_1024p_label_12G.sh`), which will crop the images during training.

### Testing
- Test the model (`bash ./scripts/test_512p_label.sh`):
```bash
#!./scripts/test_512p_label.sh
python test.py --name label2city_512p --phase test --how_many 1
```
The test results will be saved to a html file here: `./results/label2city_512p/test_latest/index.html`.

More example scripts can be found at `scripts` directory.

## Training/test Details
- Flags: see `options/train_options.py` and `options/base_options.py` for all the training flags; see `options/test_options.py` and `options/base_options.py` for all the test flags.