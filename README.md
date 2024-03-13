里面是一些处理数据的脚本文件。

总结：把jpg放到img里，使用labelimg标注完成，使用enhence.py增强一下，再使用change.py转换为txt存到data文件夹下。

之后划分数据集为测试集  验证集  训练集

parse_spatial 是添加位置属性的脚本
related是添加相邻药品信息的脚本
data eve all是集合上面两个的，可以直接修改数据库文件
drugv3是现在再用的数据库json
ctmask 处理images，将mask部分取出，写上根目录和输出目录即可
readtxt 读取yolo的结果txt，输出检测到的信息，还需要根据实际情况调整
