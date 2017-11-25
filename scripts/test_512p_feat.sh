################################ Testing ################################
# first precompute and cluster all features
python encode_features.py --name label2city_512p_feat;
# use instance-wise features
python test.py --name label2city_512p_feat --phase test --how_many 50 --use_instance --instance_feat