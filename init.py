#!/usr/bin/env python
# coding:utf-8
import subprocess

hadoop_path = '/usr/local/hadoop/bin/hadoop'
local_input = '/usr/zyy/zyy1/news_pages'
input_dir = '/'
output_dir = '/output'
subprocess.call(['python3', 'crawl.py'])
subprocess.call([hadoop_path, 'fs', '-rm','-r', output_dir])
subprocess.call(['rm','-r','/usr/zyy/zyy1/index-tf_idf.csv'])
subprocess.call([hadoop_path, 'fs', '-put', local_input, input_dir])

subprocess.call([hadoop_path, 'jar', '/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar',
                 '-input', '/news_pages', '-output', output_dir,
                 '-mapper', 'python3 /usr/zyy/zyy1/mapreduce/mapper.py', '-reducer', 'python3 /usr/zyy/zyy1/mapreduce/reducer.py',
                 '-file', '/usr/zyy/zyy1/mapreduce/mapper.py', '-file', '/usr/zyy/zyy1/mapreduce/reducer.py','-file', '/usr/zyy/zyy1/mapreduce/new_stopwords.txt'])
subprocess.call([hadoop_path, 'fs', '-get', '/output/part-00000','/usr/zyy/zyy1/index-tf_idf.csv'])

subprocess.call(['python3', 'pre.py'])

