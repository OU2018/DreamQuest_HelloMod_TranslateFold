import re

# 正则表达式：匹配 , "xx"));
pattern = r',\s*"([^"]+)"\s*\)\);'

# 读取 UnSolved.txt 文件内容
with open('UnSolved.txt', 'r', encoding='utf-8') as unsolved_file:
    lines = unsolved_file.readlines()

# 创建或打开 Solved.txt 文件进行写入
with open('Solved.txt', 'w', encoding='utf-8') as solved_file:
    for line_num, line in enumerate(lines, 1):
        print(f"正在处理第 {line_num} 行: {line.strip()}")  # 输出当前处理的行
        # 使用正则提取每行中的 "xx" 部分
        match = re.search(pattern, line)
        
        if match:
            extracted_content = match.group(1)
            print(f"提取的内容: {extracted_content}")  # 输出提取到的内容
            solved_file.write(f"{extracted_content}, 待翻译,\n")
        else:
            print(f"未能提取到内容: {line.strip()}")  # 输出未匹配的行

print("处理完成，已将结果输出到 Solved.txt 文件。")
