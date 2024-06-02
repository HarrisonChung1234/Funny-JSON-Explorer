import argparse
import json
import os
from factories import TreeFactory, RectangleFactory
from lib.explorer import FunnyJsonExplorer

# 构建命令行参数解析器
parser = argparse.ArgumentParser(description='Explore JSON data in different styles.')
parser.add_argument('-f', '--file', type=str, help='JSON file path', default='fruits.json')
parser.add_argument('-s', '--style', type=str, help='Style (tree/rectangle)', default='rectangle')
parser.add_argument('-i', '--icon_family', type=str, help='Icon family name', default='star')

# 解析命令行参数
args = parser.parse_args()

# 如果未提供文件路径，则使用默认JSON数据
with open(args.file, encoding='utf-8', errors='ignore') as f:
    json_data = json.load(f)
icon_families = {}
icon_folder_path = 'icon_family'
for file_name in os.listdir(icon_folder_path):
    if file_name.endswith('.json'):
        icon_file_path = os.path.join(icon_folder_path, file_name)
        with open(icon_file_path, encoding='utf-8') as icon_file:
            icon_family = json.load(icon_file)
            icon_name = file_name[:-5]
            icon_families[icon_name] = icon_family
selected_icon_family = {}
if args.icon_family:
    selected_icon_family = icon_families.get(args.icon_family, {})
else:
    selected_icon_family = icon_families.get('default', {})
# 根据提供的样式选择工厂
if args.style == 'rectangle':
    factory = RectangleFactory()
else:
    factory = TreeFactory()

explorer = FunnyJsonExplorer(factory, icon_family=selected_icon_family)
explorer.show(json_data)
