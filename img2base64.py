#!/usr/bin/env python3
import base64
import os
import argparse
import pyperclip

def image_to_base64(image_path):
    """Convert an image file to a Base64 encoded string."""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def get_mime_type(file_extension):
    """Return the MIME type based on the file extension."""
    mime_types = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'bmp': 'image/bmp',
        'webp': 'image/webp',

    }
    return mime_types.get(file_extension.lower(), 'application/octet-stream')

def generate_markdown(base64_string, image_name, mime_type):
    """Generate Markdown code for displaying the Base64 encoded image."""
    return f'![{image_name}](data:{mime_type};base64,{base64_string})'

def generate_html(base64_string, mime_type):
    """Generate HTML code for displaying the Base64 encoded image."""
    return f'<img src="data:{mime_type};base64,{base64_string}" alt="{mime_type}" />'

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert an image to a Base64 encoded string and generate Markdown or HTML code.')
    parser.add_argument('image_path', help='Path to the image file, including the file name')
    parser.add_argument('--format', '-f', choices=['markdown', 'html'], default='markdown', help='Output format: markdown or html')

    args = parser.parse_args()

    # Extract the file extension and file name
    file_extension = os.path.splitext(args.image_path)[1][1:]
    file_name = os.path.splitext(os.path.basename(args.image_path))[0]
    mime_type = get_mime_type(file_extension)

    # Convert the image to Base64
    base64_string = image_to_base64(args.image_path)

    # Generate the appropriate output
    if args.format == 'html':
        output_code = generate_html(base64_string, mime_type)
    else:
        output_code = generate_markdown(base64_string, file_name, mime_type)

    # Print to screen
    print(f"\n{args.format.capitalize()} Code:\n")
    print(output_code)

    # Copy to clipboard
    pyperclip.copy(output_code)
    print("\nThe code has also been copied to the clipboard.")

if __name__ == "__main__":
    main()