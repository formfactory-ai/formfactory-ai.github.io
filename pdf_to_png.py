import os
from pdf2image import convert_from_path
from pathlib import Path

def convert_pdf_to_png(input_folder):
    # 确保输入文件夹存在
    if not os.path.exists(input_folder):
        print(f"错误：文件夹 '{input_folder}' 不存在")
        return

    # 获取所有PDF文件
    pdf_files = list(Path(input_folder).glob("*.pdf"))
    
    if not pdf_files:
        print(f"在文件夹 '{input_folder}' 中没有找到PDF文件")
        return

    # 为输出创建images文件夹
    output_folder = os.path.join(input_folder, "images")
    os.makedirs(output_folder, exist_ok=True)

    # 处理每个PDF文件
    for pdf_path in pdf_files:
        try:
            print(f"正在处理: {pdf_path.name}")
            
            # 将PDF转换为图片
            images = convert_from_path(pdf_path)
            
            # 保存每一页为PNG
            for i, image in enumerate(images):
                output_file = os.path.join(output_folder, f"{pdf_path.stem}_page_{i+1}.png")
                image.save(output_file, "PNG")
                print(f"已保存: {output_file}")
                
        except Exception as e:
            print(f"处理 {pdf_path.name} 时发生错误: {str(e)}")

if __name__ == "__main__":
    # 获取用户输入的文件夹路径
    folder_path = "MM2025-Bobo-FormFactory-v1/figs"
    convert_pdf_to_png(folder_path) 