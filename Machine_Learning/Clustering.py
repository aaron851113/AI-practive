#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:10:02 2018

@author: aaron
"""

from sklearn import cluster, datasets



if __name__ == "__main__":
        
    # 讀入鳶尾花資料
    iris = datasets.load_iris()
    iris_X = iris.data
    
    # KMeans 演算法
    kmeans_fit = cluster.KMeans(n_clusters = 3).fit(iris_X)
    
    # 印出分群結果
    cluster_labels = kmeans_fit.labels_
    print("分群結果：")
    print(cluster_labels)
    print("---")
    
    # 印出品種看看
    iris_y = iris.target
    print("真實品種：")
    print(iris_y)