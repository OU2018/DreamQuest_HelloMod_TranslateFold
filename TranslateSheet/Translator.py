from googletrans import Translator

# 初始化翻译器
translator = Translator()

# 定义读取文件和写入文件的路径
input_file = 'Solved.txt'
output_file = 'Translated.txt'

def translate_line(line):
    """
    处理每一行，翻译并替换 '待翻译' 为翻译后的内容。
    """
    try:
        # 输出原始行以调试
        print(f"Processing line: {line.strip()}")
        
        # 通过分隔符提取英文部分（例如 'Attack (1)'）
        english_text = line.split(',')[0].strip()
        
        # 输出提取的英文部分
        print(f"Extracted text for translation: {english_text}")
        
        # 翻译英文内容
        translated = translator.translate(english_text, src='en', dest='zh-cn')
        
        # 输出翻译后的文本
        print(f"Translated text: {translated.text}")
        
        # 用翻译后的内容替换 '待翻译'
        translated_line = line.replace('待翻译', translated.text)
        
        return translated_line
    except Exception as e:
        # 捕获任何异常，输出错误信息并返回原始行
        print(f"Error occurred while translating line: {line.strip()}")
        print(f"Error: {e}")
        return line  # 返回原始行

def process_file(input_file, output_file):
    """
    处理输入文件并生成翻译后的输出文件。
    """
    # 打开输入文件并读取所有行
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    # 如果文件为空，输出调试信息
    if not lines:
        print(f"{input_file} is empty!")
        return
    
    # 打开输出文件准备写入
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            # 处理每一行，翻译并替换
            translated_line = translate_line(line)
            # 写入翻译后的行到文件
            outfile.write(translated_line + '\n')

# 执行处理
process_file(input_file, output_file)
print(f"翻译完成，结果已输出到 {output_file}")
