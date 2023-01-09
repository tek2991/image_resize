# Import libraries
import os
from PIL import Image

# Get all files in folder and subfolder
def get_all_files(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files


# Resize parameter
max_height = 1080
max_width = 1920
image_quality = 80 # 0-100

# Get all files
files = get_all_files('./vps/vps-tracking.in/storage/app/public/invoices/') # Change path here

# Calculate new image size, resize and save
for file in files:
    # Check file is a valid image
    try:
        img = Image.open(file)
        img.verify()
    except (IOError, SyntaxError) as e:
        print('Bad file:', file)
        # write error to log.txt
        with open('err_log.txt', 'a') as f:
            f.write(str(e) + ' ' + '\r')
        continue
    img = Image.open(file)
    width, height = img.size
    if width > max_width or height > max_height:
        if width > height:
            new_height = int(max_width * height / width)
            new_width = max_width
        else:
            new_width = int(max_height * width / height)
            new_height = max_height
        new_size = (new_width, new_height)
        img = img.resize(new_size, Image.ANTIALIAS)
        img.save(file, optimize=True, quality=image_quality)

# End of file
