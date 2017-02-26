python spider_process_mongo.py
仅使用了 mongo db
需要在本机启动mongo，使用默认端口，可以在创建 MongoUrlManager 的时候设置Mongo服务器和端口

python spider_process_mr.py
同时用了 mongo 与 reids
需要在本机启动mongo及redis，使用默认端口，可以在创建 MongoRedisUrlManager 的时候设置Mongo服务器和端口