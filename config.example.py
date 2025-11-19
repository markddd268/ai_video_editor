# 配置文件
# API配置
ARK_API_CONFIG = {
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "api_key": "abcdefghijklmnopqrstuvwxyz"
}

# 模型配置
MODEL_CONFIG = {
    "model_name": "doubao-seed-1-6-vision-250815"
}

# 处理配置
PROCESSING_CONFIG = {
    "video_dir": "video",
    "output_dir": "results",
    "delay_between_requests": 3  # 请求间隔时间（秒）
}

# 提示词配置
PROMPT_CONFIG = {
    "video_analysis_prompt": """这是一条关于'xxxxx'的广告切片，请结合时间顺序,详细描述视频中出现的物品、人物、动作，包括但不限于 数量，颜色，文字等信息。
，结果通过json返回。
json格式为：
{
    "summarize": "此处填写整体描述"
}"""
}