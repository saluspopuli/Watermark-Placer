from PIL import Image
import os
import glob

if __name__ == "__main__":
    
    files_to_convert_size = 0
    index = 0
    
    watermark_file = input("Enter the name of the watermark file (Include file extension): ")
    watermark = Image.open(watermark_file).convert("RGBA")
    
    scale_s = input("Enter the scale of the watermark (0-1): ")
    new_width = int(watermark.size[0] * float(scale_s))
    new_length = int(watermark.size[1] * float(scale_s))
    
    watermark = watermark.resize((new_width, new_length))
    
    location_s = input("Enter the location of the watermark (x,y): ")
    x = int(location_s.split(",")[0])
    y = int(location_s.split(",")[1])
    
    extension = input("Enter the file extension of the images to convert: ")
    files_to_convert = glob.glob("*." + extension)
    files_to_convert_size = len(files_to_convert)
    
    if watermark_file in files_to_convert:
        files_to_convert.remove(watermark_file)
    
    img = Image.open(files_to_convert[0]).convert("RGBA")
    img.paste(watermark, (x,y), mask=watermark)
    img.convert("RGB").show()
    
    print("Files to convert: " + str(files_to_convert_size))
    input("Press enter to convert all files...")
    
    try:
        os.mkdir("OUTPUT")
    except:
        pass
    
    for file in files_to_convert:
        print("Converting image " + str(index) + " of " + str(files_to_convert_size) + "...")
                
        img = Image.open(file).convert("RGBA")
        img.paste(watermark, (x,y), mask=watermark)
        
        file_name, file_extension = os.path.splitext(file)
        new_file_name = file_name + "_watermarked" + file_extension
        
        img.convert("RGB").save(os.path.join("OUTPUT", new_file_name))
        index += 1
