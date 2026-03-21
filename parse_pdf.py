import pdfplumber
import sys
import os

# 设置控制台输出编码为UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def parse_pdf(pdf_path):
    """解析PDF文件并返回文本内容"""
    text = ""
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"## 第 {i+1} 页\n\n"
                    text += page_text + "\n\n"
    except Exception as e:
        print(f"解析PDF时出错: {e}")
        return None
    
    return text

def save_as_markdown(content, output_path):
    """将内容保存为Markdown文件"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"已保存到: {output_path}")
        return True
    except Exception as e:
        print(f"保存文件时出错: {e}")
        return False

if __name__ == "__main__":
    pdf_path = r"C:\Users\z8644\Desktop\2026.3.4会议纪要.pdf"
    
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误: 找不到文件 {pdf_path}")
        sys.exit(1)
    
    # 解析PDF
    print(f"正在解析PDF: {pdf_path}")
    content = parse_pdf(pdf_path)
    
    if content:
        # 保存为Markdown文件
        output_path = r"D:\blog\andrea\meeting_notes.md"
        save_as_markdown(content, output_path)
        
        # 显示内容预览
        print("\n=== 内容预览 (前500字符) ===")
        print(content[:500])
        print("...")
    else:
        print("解析失败")
