############## To train images at 2048 x 1024 resolution after training 1024 x 512 resolution models #############
##### Using GPUs with 12G memory (not tested)
# Adding instances and encoded features
python train.py --name label2city_feat_1024p --netG cas_resnet --ngf 32 --num_D 3 --pool_size 1 \
  --load_pretrain checkpoints/label2city_feat_512p/ --niter_fix_global 10 --resize_or_crop crop \
  --fineSize 1024 --use_instance --instance_feat