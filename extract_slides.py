import fitz
import os

PDF_PATH = r"C:\Users\thoma\OneDrive\Desktop\AverysRootDirectory\personal\familyHistory\Mimis funeral service slideshow.pdf"
OUT_DIR = r"C:\Users\thoma\OneDrive\Desktop\AverysRootDirectory\personal\familyHistory\images\squires"

os.makedirs(OUT_DIR, exist_ok=True)

doc = fitz.open(PDF_PATH)
print(f"Total pages: {len(doc)}")

for i, page in enumerate(doc):
    slide_num = i + 1
    mat = fitz.Matrix(150 / 72, 150 / 72)  # 150 DPI
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(OUT_DIR, f"slide_{slide_num:03d}.jpg")
    pix.save(out_path)
    print(f"Saved slide_{slide_num:03d}.jpg")

print("Done.")
