# Shikibetsu
Deep Transfer Learning for Person Re-Identification. 

Basenet: GoogLeNet, pretrained on Imagenet.

Two step Fine Tuning:
  1. (MARKET1501 + CUHK03) Base network -> Large Re-Id dataset
  2. (PRID + CUHK01) Large Re-Id -> Small Re-Id
