import base64
import os
import json
import datetime
import time
import glob
# Install SDK:  pip install 'volcengine-python-sdk[ark]' .
from volcenginesdkarkruntime import Ark 
from config import ARK_API_CONFIG, MODEL_CONFIG, PROCESSING_CONFIG, PROMPT_CONFIG

client = Ark(
    # The base URL for model invocation .
    base_url=ARK_API_CONFIG["base_url"], 
    # Get API Key：https://console.volcengine.com/ark/region:ark+cn-beijing/apikey
    api_key=ARK_API_CONFIG["api_key"], 
)

# 定义方法将指定路径视频转为Base64编码
def encode_video(video_path):
    with open(video_path, "rb") as video_file:
        return base64.b64encode(video_file.read()).decode('utf-8')

# 处理单个视频文件
def process_video(video_path):
    """处理单个视频文件并返回分析结果"""
    try:
        print(f"正在处理视频: {os.path.basename(video_path)}")
        
        # 获取视频文件名（不含扩展名）
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        
        # 将视频转为Base64编码
        base64_video = encode_video(video_path)
        
        completion = client.chat.completions.create(
            model=MODEL_CONFIG["model_name"],
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "video_url",
                            "video_url": {
                                "url": f"data:video/mp4;base64,{base64_video}"
                            },         
                        },
                        {
                            "type": "text",
                            "text": PROMPT_CONFIG["video_analysis_prompt"],
                        },
                    ],
                }
            ],
        )
        
        # 获取AI返回的内容
        result_content = completion.choices[0].message.content
        
        return {
            "success": True,
            "video_name": video_name,
            "result_content": result_content
        }
        
    except Exception as e:
        print(f"处理视频 {os.path.basename(video_path)} 时出错: {str(e)}")
        return {
            "success": False,
            "video_name": os.path.basename(video_path),
            "error": str(e)
        }

# 批量处理视频目录下的所有视频
def batch_process_videos(video_dir=PROCESSING_CONFIG["video_dir"], output_dir=PROCESSING_CONFIG["output_dir"]):
    """批量处理视频目录下的所有视频文件"""
    
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取所有视频文件
    video_files = glob.glob(os.path.join(video_dir, "*.mp4"))
    
    if not video_files:
        print(f"在目录 {video_dir} 中未找到任何MP4视频文件")
        return
    
    print(f"找到 {len(video_files)} 个视频文件，开始批量处理...")
    print("=" * 50)
    
    # 生成批次时间戳
    batch_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 处理统计
    processed_count = 0
    success_count = 0
    failed_count = 0
    
    # 处理每个视频文件
    for video_path in video_files:
        processed_count += 1
        print(f"\n[{processed_count}/{len(video_files)}] " + "=" * 40)
        
        # 处理视频
        result = process_video(video_path)
        
        if result["success"]:
            success_count += 1
            
            # 保存结果到JSON文件
            output_filename = f"{result['video_name']}_{batch_timestamp}.json"
            output_filepath = os.path.join(output_dir, output_filename)
            
            with open(output_filepath, 'w', encoding='utf-8') as f:
                f.write(result['result_content'])
            
            print(f"✓ 处理成功 - 结果已保存到: {output_filepath}")
            
        else:
            failed_count += 1
            print(f"✗ 处理失败 - 错误: {result['error']}")
        
        # 添加延迟，避免API请求过于频繁
        if processed_count < len(video_files):
            print(f"等待{PROCESSING_CONFIG['delay_between_requests']}秒后处理下一个视频...")
            time.sleep(PROCESSING_CONFIG['delay_between_requests'])
    
    print("\n" + "=" * 50)
    print(f"批量处理完成!")
    print(f"总计处理: {processed_count} 个视频")
    print(f"成功: {success_count} 个")
    print(f"失败: {failed_count} 个")
    print(f"结果文件保存在: {output_dir} 目录")

# 主程序
if __name__ == "__main__":
    # 批量处理视频目录下的所有视频
    batch_process_videos()