# PDF转PNG转换器

这是一个简单的Python程序，用于将文件夹中的所有PDF文件转换为PNG图片。

## 环境要求

- Python 3.6+
- pdf2image
- Pillow

## 安装依赖

在使用之前，请先安装所需的依赖包：

```bash
pip install -r requirements.txt
```

### MacOS用户注意事项

MacOS用户需要安装poppler：

```bash
brew install poppler
```

## 使用方法

1. 运行程序：
```bash
python pdf_to_png.py
```

2. 在提示时输入包含PDF文件的文件夹路径

3. 程序会在指定文件夹中创建一个名为"images"的子文件夹，并将所有转换后的PNG文件保存在其中

## 输出格式

- 每个PDF文件的每一页都会被转换为单独的PNG文件
- 输出文件名格式：`原始文件名_page_页码.png`
- 所有PNG文件都保存在输入文件夹下的"images"子文件夹中
