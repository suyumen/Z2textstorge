import subprocess
import os
import csv

# Step 1: 执行爬虫
subprocess.call(['python', 'crawl.py'])

# Step 2: 数据存储到hadoop
hadoop_path = '/usr/local/hadoop/bin/hadoop'
input_dir = '/data/input'
output_dir = '/data/output'

os.chdir('scraped_files')
subprocess.call([hadoop_path, 'fs', '-put', '.', input_dir])
os.chdir('..')

# Step 3: 创建文件
with open('/mapreduce/index.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'doc_name', 'count'])

with open('/mapreduce/tf_idf.csv', 'w') as f:
    pass

# Step 4: 执行mapreduce
subprocess.call([hadoop_path, 'jar', 'path/to/hadoop-streaming.jar',
                 '-input', input_dir, '-output', output_dir,
                 '-mapper', '/mapreduce/mapper.py', '-reducer', '/mapreduce/reducer.py',
                 '-file', '/mapreduce/mapper.py', '-file', '/mapreduce/reducer.py'])

# Step 5: 下载文件
os.makedirs('output', exist_ok=True)
subprocess.call([hadoop_path, 'fs', '-get', output_dir + '/tf_idf.csv', 'output'])

print("Done!")
