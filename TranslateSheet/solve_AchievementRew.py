import csv
import re

# 定义函数来处理CSV文件
def process_csv(input_file):
    # 打开输入的CSV文件
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # 打开输出的TalentName.csv和CardName.csv文件
    with open('TalentName.csv', mode='a', newline='', encoding='utf-8') as talent_file, \
         open('CardName.csv', mode='a', newline='', encoding='utf-8') as card_file:
        
        talent_writer = csv.writer(talent_file)
        card_writer = csv.writer(card_file)

        # 逐行处理CSV文件
        for row in rows:
            # 获取行中的第一个数据（即任务描述）
            first_column = row[0] if len(row) > 0 else ""

            # 如果匹配到 "Gain access to the ____ talent"
            talent_match = re.search(r"Gain access to the (.+?) talent", first_column)
            if talent_match:
                talent_name = talent_match.group(1)
                # 替换对应行中的<<TalentName|xx>>中的xx为talentName
                row[1] = re.sub(r"<<TalentName\|.*?>>", f"<<TalentName|{talent_name}>>", row[1])
                # 将talentName和"待译"添加到TalentName.csv文件中
                talent_writer.writerow([talent_name, "待译"])
                print(f"Processed Talent: {talent_name}")

            # 如果匹配到 "Gain access to the ____ card"
            card_match = re.search(r"Gain access to the (.+?) card", first_column)
            if card_match:
                card_name = card_match.group(1)
                # 替换待翻译字符串为“解锁卡牌【<<CardName|cardName>>】”
                row[1] = re.sub(r"待翻译", f"解锁卡牌【<<CardName|{card_name}>>】", row[1])
                # 将cardName和"待译"添加到CardName.csv文件中
                card_writer.writerow([card_name, "待译"])
                print(f"Processed Card: {card_name}")

        # 保存修改后的CSV文件
        with open(input_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)

# 主函数
if __name__ == '__main__':
    # 输入文件路径
    input_file = 'AchievementRew.csv'
    process_csv(input_file)
