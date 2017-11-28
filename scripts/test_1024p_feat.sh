################################ Testing ################################
# first precompute and cluster all features
python encode_features.py --name label2city_1024p_feat --netG local --ngf 32 --resize_or_crop none;
# use instance-wise features
python test.py --name label2city_1024p_feat --phase test --how_many 10 --netG local --ngf 32 --resize_or_crop none --use_instance --instance_feat