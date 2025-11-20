#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import argparse


def merge_json_files(search_dir, output_file):
    """
    合并多个文件夹下的JSON文件到一个文件中，并添加文件名作为video_name字段
    
    Args:
        search_dir (str): 搜索JSON文件的根目录
        output_file (str): 输出文件路径
    """
    merged_data = []
    json_count = 0
    
    # 遍历搜索目录下的所有文件
    for root, _, files in os.walk(search_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    # 读取JSON文件
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # 添加video_name字段（文件名，不包含扩展名）
                    video_name = os.path.splitext(file)[0]
                    data['video_name'] = video_name
                    
                    # 添加到合并数据中
                    merged_data.append(data)
                    json_count += 1
                    print(f"处理文件: {file_path}")
                    
                except json.JSONDecodeError as e:
                    print(f"警告: 文件 {file_path} 不是有效的JSON文件: {e}")
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")
    
    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 写入合并后的JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n合并完成!")
    print(f"成功处理了 {json_count} 个JSON文件")
    print(f"合并结果保存在: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='合并多个文件夹下的JSON文件')
    parser.add_argument('--dir', type=str, default=os.path.join(os.getcwd(), 'results'), 
                       help='搜索JSON文件的目录（默认：results目录）')
    parser.add_argument('--output', type=str, default='results/result.json',
                       help='输出文件路径（默认：results/result.json）')
    
    args = parser.parse_args()
    
    # 转换为绝对路径
    search_dir = os.path.abspath(args.dir)
    output_file = os.path.abspath(args.output)
    
    print(f"开始搜索目录: {search_dir}")
    print(f"输出文件: {output_file}")
    
    merge_json_files(search_dir, output_file)