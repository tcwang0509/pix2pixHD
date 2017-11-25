from options.test_options import TestOptions
from data.data_loader import CreateDataLoader
from models.models import create_model
import numpy as np
import os, time
import util.util as util

opt = TestOptions().parse(save=False)
opt.nThreads = 1   # test code only supports nThreads = 1
opt.batchSize = 1  # test code only supports batchSize = 1
opt.serial_batches = True  # no shuffle
opt.no_flip = True  # no flip
opt.label_only = True
opt.dataset_mode = 'single'
opt.model = 'test'

dataset = os.path.basename(opt.dataroot)		
opt.instance_feat = True
opt.use_instance = True

opt.dataroot = os.path.join(opt.dataroot, 'train')
name = 'features'
save_path = os.path.join(opt.checkpoints_dir, opt.name)

############ Initialize #########
data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
dataset_size = len(data_loader)
model = create_model(opt)

########### Encode features ###########
reencode = True
if reencode:
	features = {}
	for label in range(opt.label_nc):
		features[label] = np.zeros((0, opt.feat_num+1))
	for i, data in enumerate(dataset):    
	    model.set_input(data)
	    feat = model.encode()
	    for label in range(opt.label_nc):
	    	features[label] = np.append(features[label], feat[label], axis=0) 
	        
	    print('%d / %d images' % (i+1, dataset_size))    
	save_name = os.path.join(save_path, name + '.npy')
	np.save(save_name, features)

######## Save encoded images for 1024p training #######
"""for i, data in enumerate(dataset):
	print(i)
	model.set_input(data)
	feat_map = model.encode_image()
	image_numpy = util.tensor2im(feat_map)
	save_path = model.image_paths[0].replace('/train/', '/train_feature_G4/')
	util.save_image(image_numpy, save_path)"""

############## Clustering ###########
n_clusters = opt.n_clusters
load_name = os.path.join(save_path, name + '.npy')
features = np.load(load_name).item()
from sklearn.cluster import KMeans
#from sklearn.preprocessing import StandardScaler
centers = {}
centers_no_pix_num = {}
for label in range(opt.label_nc):
	feat = features[label]
	feat = feat[feat[:,-1] > 0.5, :-1]		
	if feat.shape[0]:
		n_clusters = min(feat.shape[0], opt.n_clusters)
		kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(feat)
		centers_no_pix_num[label] = kmeans.cluster_centers_
save_name = os.path.join(save_path, name + '_clustered_%03d.npy' % opt.n_clusters)
save_name_no_pix_num = os.path.join(save_path, name + '_clustered_noPixNum_%03d.npy' % opt.n_clusters)
np.save(save_name, centers)
np.save(save_name_no_pix_num, centers_no_pix_num)
print('saving to %s' % save_name)