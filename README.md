# img2base64.py

img2base64.py is a script that I wrote that will convert jpeg, gif, png, and a few more formats into base64 and then give you the code in markdown or html format for directly importing images into a file without needing to upload the file separately. Because this is usually a **huge** block of code, it will also send it to your clipboard so you can paste it directly into your code.

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

## Output:

Your output will look like something like this depending on the size of the image. I suggest that you disable Word Wrap when working with this code.

### Markdown
```
img2base64.py favicon.png 

Markdown Code:

![favicon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAu1JREFUaEO9Wmt6xCAI1Mu09z/XHsJ+JrrxATgjpvnTdoPADA/Rbgyf3xSkJ38aQwj1pyiUP9QElgsbjYoxWEUKUQVi+aiCerAbIvOrr8P3L5W/W7BBIwKra7SIUJ4MgbGYRFlOKYSYIbWPvDhL2RGBwABejyLl7555yJgqdACIzwGAcMiAAQTNgcdODCnksnvlWbhzMCK2JVcaDc0gEzXqa4DwEUCZn43evejkA0XExea66RQJH5EKEJ9SaxftSPGaaUjiN8TdjRzo0qtUs0g42rVWjtjv4ZlIVCMCYWvClifyhxA1uhbBJ2EQ0coSJ+nsI9KMDnVco3feF8YPjIzF0HixJUXAiIrMsCeMi7V5vrzGeNopaChFiDwmE+Pn9yJ8el4g8EQt9H5Wz/MZBj2PCMBUx8azhIeU4nlMIaSoH9yM1CILw5MkbqCro67HuX9ei6fW4FibVsc2RGE87xqR2ZTQGqEYxnKl5j1wVWNaJ8/sT4egMGnCGNZudXsCfedgpTglppx4OwIfWr6C45URViMUe4YwpceIu7gVHKyR86PJPR/FmJPKfrCIeIriVBT2gTweMKPF97q47MTzSIFcFw3oATK6iGgO7wBRCQScwhKgV/ROajmd1We4smMKTe6ZtfJLJOoIXSKQZurju61t9brv1sZ4xOGjsz9msHJ9dbGGsI3U2smbsqb8p2DVSjFIfVgxIDu+894IK1rDthMYENKpp1g3GQCWOa6DqnbACgCcaemiusEN/srUKvAtjFuLJi82U+vAYGio2ImWCWRH4bLhH9usiqVCiAxEZWsjDZQlHpKktevUGh0BU+I5xi4qf9JXdxlpzJDf5SE/hs9Pytdbrk1qI1BIJ5plZkPfaXv5FQ6glaIinnRa2Vin1taAx4eIAylFRjzq6qMBZ3DFI/m+878Hw0VEsysWrHYmwKLFEnYECGv04QMDhRX9wVsUMlEucbhND7WavzjUdtrXdnb8bniAzwbpkk/hD6bLTo9ZDsFVAAAAAElFTkSuQmCC)

The code has also been copied to the clipboard.
```


### HTML
```
img2base64.py favicon.png -f html 

Html Code:

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAu1JREFUaEO9Wmt6xCAI1Mu09z/XHsJ+JrrxATgjpvnTdoPADA/Rbgyf3xSkJ38aQwj1pyiUP9QElgsbjYoxWEUKUQVi+aiCerAbIvOrr8P3L5W/W7BBIwKra7SIUJ4MgbGYRFlOKYSYIbWPvDhL2RGBwABejyLl7555yJgqdACIzwGAcMiAAQTNgcdODCnksnvlWbhzMCK2JVcaDc0gEzXqa4DwEUCZn43evejkA0XExea66RQJH5EKEJ9SaxftSPGaaUjiN8TdjRzo0qtUs0g42rVWjtjv4ZlIVCMCYWvClifyhxA1uhbBJ2EQ0coSJ+nsI9KMDnVco3feF8YPjIzF0HixJUXAiIrMsCeMi7V5vrzGeNopaChFiDwmE+Pn9yJ8el4g8EQt9H5Wz/MZBj2PCMBUx8azhIeU4nlMIaSoH9yM1CILw5MkbqCro67HuX9ei6fW4FibVsc2RGE87xqR2ZTQGqEYxnKl5j1wVWNaJ8/sT4egMGnCGNZudXsCfedgpTglppx4OwIfWr6C45URViMUe4YwpceIu7gVHKyR86PJPR/FmJPKfrCIeIriVBT2gTweMKPF97q47MTzSIFcFw3oATK6iGgO7wBRCQScwhKgV/ROajmd1We4smMKTe6ZtfJLJOoIXSKQZurju61t9brv1sZ4xOGjsz9msHJ9dbGGsI3U2smbsqb8p2DVSjFIfVgxIDu+894IK1rDthMYENKpp1g3GQCWOa6DqnbACgCcaemiusEN/srUKvAtjFuLJi82U+vAYGio2ImWCWRH4bLhH9usiqVCiAxEZWsjDZQlHpKktevUGh0BU+I5xi4qf9JXdxlpzJDf5SE/hs9Pytdbrk1qI1BIJ5plZkPfaXv5FQ6glaIinnRa2Vin1taAx4eIAylFRjzq6qMBZ3DFI/m+878Hw0VEsysWrHYmwKLFEnYECGv04QMDhRX9wVsUMlEucbhND7WavzjUdtrXdnb8bniAzwbpkk/hD6bLTo9ZDsFVAAAAAElFTkSuQmCC" alt="image/png" />

The code has also been copied to the clipboard.
```
