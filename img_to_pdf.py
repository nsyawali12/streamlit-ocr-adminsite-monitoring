from pdf2image import convert_from_path

## KHUSUS Converting PDF ke JPG

pdf_file_path = "dataset/monitoring_harian/monitoring_harian_petak5.pdf"

images = convert_from_path(pdf_file_path)

for i, image in enumerate(images):
    image.save(f'harian_pakan_{i+1}.png', 'PNG')
    
print(f'{len(images)} images saved.')

