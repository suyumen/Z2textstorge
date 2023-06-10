import csv

input_file = "index-tf_idf.csv"
output_index_file = "/usr/zyy/zyy1/mapreduce/index.csv"
output_tf_idf_file = "/usr/zyy/zyy1/mapreduce/tf_idf.csv"
found_tf_idf = False
tf_idf_lines = []

# 打开CSV文件进行读取
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# 寻找目标行"word,doc_name,doc_url,tf_idf"
target_row = ["word", "doc_name", "doc_url", "tf_idf"]
target_index = None
for i, row in enumerate(rows):
    if [cell.strip() for cell in row] == target_row:
        target_index = i
        break

# 如果找到目标行，截取目标行及其后面的行
if target_index is not None:
    tf_idf_rows = rows[target_index:]
    # 将截取的行保存为tf_idf.csv文件
    with open(output_tf_idf_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(tf_idf_rows)
        print("tf_idf.csv 文件保存成功")
else:
    print("未找到目标行")

# 如果找到目标行，截取目标行之前的内容
if target_index is not None:
    rows_to_keep = rows[:target_index]
    with open(output_index_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows_to_keep)
        print("index 文件内容更新成功")
else:
    print("未找到目标行")