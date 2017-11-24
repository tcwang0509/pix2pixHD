################################# Training ##############################

#### Please uncomment which model you want to train

############## To train images at 1024 x 512 resolution #############
### Using labels only
python train.py --name label2city_512p

### Adding instances and encoded features
# python train.py --name label2city_feat_512p --use_instance --instance_feat


############## To train images at 2048 x 1024 resolution after training above #############
######## Using GPUs with 24G memory
### Using labels only
#python train.py --name label2city_1024p --netG cas_resnet --ngf 32  \
#  --num_D 3 --pool_size 10 --load_pretrain checkpoints/label2city_512p/ --niter_fix_global 10 --resize_or_crop none

### Adding instances and encoded features
# python train.py --name label2city_feat_1024p --dataroot ../label2img/datasets/cityscape/ --netG cas_resnet --ngf 32 \
#  --num_D 3 --pool_size 1 --load_pretrain checkpoints/label2city_feat_512p/ --niter_fix_global 10 --resize_or_crop none \
#  --use_instance --instance_feat --load_features

##### Using GPUs with 12G memory (not tested)
# Using labels only
#python train.py --name label2city_1024p --dataroot ../label2img/datasets/cityscape/ --netG cas_resnet --ngf 32 \
#  --num_D 3 --pool_size 10 --load_pretrain checkpoints/label2city_512p/ --niter_fix_global 10 --resize_or_crop crop \
#  --fineSize 1024
# Adding instances and encoded features
#python train.py --name label2city_feat_1024p --dataroot ../label2img/datasets/cityscape/ --netG cas_resnet --ngf 32 \
#  --num_D 3 --pool_size 1 --load_pretrain checkpoints/label2city_feat_512p/ --niter_fix_global 10 --resize_or_crop crop \
#  --fineSize 1024 --use_instance --instance_feat

######## For multi-GPU training #######
# --batchSize 8 --gpu_ids 0,1,2,3,4,5,6,7 --pool_size 1 --lr ?


################################ Testing ################################
#python test.py --name label2city_1024p --phase test --how_many 50 
