# img2base64.py

img2base64.py is a script that I wrote that will convert jpeg, gif, png, and a few more formats into base64 and then give you the code in markdown or html format for directly importing images into a file without needing to upload the file separately. Because this is usually a **huge** block of code, it will also send it to your clipboard so you can paste it directly into your code. I suggest

## How to use it

### Requiredments:
You will need the python-pyperclip library. This is used to send the completed code to your system's clipboard.

### Commands:
```
usage: img2base64.py [-h] [--format {markdown,html}] image_path

Convert an image to a Base64 encoded string and generate Markdown or HTML code.

positional arguments:
  image_path            Path to the image file, including the file name

options:
  -h, --help            show this help message and exit
  --format {markdown,html}, -f {markdown,html}
                        Output format: markdown or html
```
