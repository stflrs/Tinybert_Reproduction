# 要删除的字符串
string_to_remove = " . "

# 打开原始文件和新文件
with open('glove.840B.300d.txt', 'r', encoding='utf-8') as original_file, \
        open('glove.840B.300d_new.txt', 'w', encoding='utf-8') as new_file:
    # 逐行读取原始文件
    for line in original_file:
        # 删除指定字符串
        if ' . ' in line:
            print(line)
        # modified_line = line.replace(string_to_remove, ' ')

        # 将修改后的行写入新文件
        # new_file.write(modified_line)

print("已删除指定字符串并将结果写入新文件。")