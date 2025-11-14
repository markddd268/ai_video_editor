# AI视频编辑器 (AI Video Editor)

基于火山引擎Ark API的AI视频内容分析工具，能够自动分析和描述视频内容，生成详细的时间轴和总结。

## 功能特性

- 🎥 **视频内容分析**: 使用先进的AI模型分析视频内容
- 📊 **时间轴分析**: 精确到0.1秒的时间段划分
- 📝 **详细描述**: 分析视频中的物品、人物、动作等信息
- 📄 **JSON输出**: 结构化的分析结果输出
- ⚡ **批量处理**: 支持批量处理多个视频文件
- 🛡️ **错误处理**: 完善的错误处理和进度跟踪

## 环境要求

- Python 3.12+
- 火山引擎Ark API访问权限

## 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd ai_video_editor
   ```

2. **安装依赖**
   ```bash
   pip install volcengine-python-sdk[ark]
   ```

3. **配置环境**
   ```bash
   # 复制配置文件模板
   cp config.example.py config.py
   
   # 编辑配置文件，填入你的API密钥
   nano config.py
   ```

## 配置说明

在 `config.py` 中配置以下参数：

```python
# API配置
ARK_API_CONFIG = {
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "api_key": "你的API密钥"  # 从火山引擎控制台获取
}

# 模型配置
MODEL_CONFIG = {
    "model_name": "doubao-seed-1-6-vision-250815"
}

# 处理配置
PROCESSING_CONFIG = {
    "video_dir": "video",           # 视频文件目录
    "output_dir": "results",        # 结果输出目录
    "delay_between_requests": 3     # API请求间隔(秒)
}
```

### 获取API密钥

1. 访问 [火山引擎控制台](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey)
2. 创建或选择API密钥
3. 将密钥填入配置文件中的 `api_key` 字段

## 使用方法

### 1. 准备视频文件

将需要分析的MP4视频文件放入 `video/` 目录中。

### 2. 运行分析程序

```bash
python main.py
```

### 3. 查看结果

分析结果将保存在 `results/` 目录中，每个视频对应一个JSON文件。

## 输出格式

AI分析结果以JSON格式返回，包含以下结构：

```json
{
    "timeline": [
        {
            "time": {
                "start_time": "0",
                "end_time": "0.9"
            },
            "content": "详细描述此时间段的内容"
        },
        {
            "time": {
                "start_time": "0.9",
                "end_time": "1.5"
            },
            "content": "详细描述此时间段的内容"
        }
    ],
    "summarize": "整体视频内容总结"
}
```

### 输出说明

- **timeline**: 时间轴数组，包含各个时间段的分析
  - **time**: 时间段信息
    - **start_time**: 开始时间(秒)
    - **end_time**: 结束时间(秒)
  - **content**: 该时间段的详细内容描述
- **summarize**: 整个视频的总结描述

## 项目结构

```
ai_video_editor/
├── main.py              # 主程序文件
├── config.example.py    # 配置文件模板
├── config.py           # 配置文件(需要手动创建)
├── pyproject.toml      # 项目配置
├── README.md           # 项目说明文档
├── video/              # 视频文件目录
│   └── [你的视频文件].mp4
└── results/            # 分析结果输出目录
    └── [结果文件].json
```

## 进度跟踪

程序运行时会显示详细的进度信息：

```
找到 X 个视频文件，开始批量处理...
==================================================

[1/X] ========================================
正在处理视频: video1.mp4
✓ 处理成功 - 结果已保存到: results/video1_20231201_143022.json
等待3秒后处理下一个视频...

[2/X] ========================================
...

批量处理完成!
总计处理: X 个视频
成功: X 个
失败: X 个
结果文件保存在: results 目录
```

## 注意事项

1. **API限制**: 请注意API调用频率限制，程序已内置3秒延迟
2. **文件格式**: 目前仅支持MP4格式的视频文件
3. **网络连接**: 确保能够正常访问火山引擎API服务
4. **存储空间**: 确保有足够的存储空间保存视频和结果文件

## 错误排查

### 常见问题

1. **API密钥错误**
   - 检查配置文件中的API密钥是否正确
   - 确认API密钥有足够的权限

2. **视频文件无法处理**
   - 确认视频文件为MP4格式
   - 检查视频文件是否损坏
   - 确认视频文件大小在API限制范围内

3. **网络连接问题**
   - 检查网络连接
   - 确认能够访问火山引擎服务

### 日志查看

程序会输出详细的处理日志，包括：
- 当前处理的视频文件名
- 处理进度
- 错误信息(如有问题)

## 版本信息

- **当前版本**: 0.1.0
- **Python要求**: >=3.12
- **依赖包**: volcengine-python-sdk[ark]

## 技术支持

如有问题或建议，请通过以下方式联系：
- 创建Issue
- 提交Pull Request

## 许可证

仅供学习交流使用，如要商用请联系作者：
![添加微信](images/wx-qr.png)
