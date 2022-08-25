import os


def hex_colors(filepath):
    """
    Returns dictionary of color names and their corresponding hexadecimal codes.
    """
    
    hex_color_codes = {}
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            data = f.read().split('\n')
    elif os.path.isdir(filepath):           # Try and find the file if the path given is a directory.
        docs = os.listdir(filepath)
        if 'rgb_hex_colors.txt' in docs:    
            filepath = os.path.abspath(filepath + '/rgb_hex_colors.txt')
            hex_colors(filepath)            # Somewhat lazy, but is well within the recursion limit.
        else:
            print('File not found! Check the path and try again.')
    else:
        print('File not found! Check the path and try again.')
    
    for line in data:                       # Take color name and hex representation from each line.
        start = line.find('#')
        color = line[:line.find('\t')]
        code = line[start:line.find('\t', start)]
        hex_color_codes[color] = code       # ... and build the dictionary.
        
    return hex_color_codes


def rgb_colors(filepath):
    """
    Returns dictionary of color names and their corresponding rgb code tuples.
    """
    
    rgb_color_codes = {}
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            data = f.read().split('\n')
    elif os.path.isdir(filepath):           # Try and find the file if the path given is a directory.
        docs = os.listdir(filepath)
        if 'rgb_hex_colors.txt' in docs:    
            filepath = os.path.abspath(filepath + '/rgb_hex_colors.txt')
            hex_colors(filepath)            # Somewhat lazy, but is well within the recursion limit.
        else:
            print('File not found! Check the path and try again.')
    else:
        print('File not found! Check the path and try again.')
    
    for line in data:                       
        color = line[:line.find('\t')]
        r = line.find('(') + 1              # Get the red, green, blue numbers from (r, g, b) string
        g = line.find(')')                  # convert them all to integers...
        b = line[r:g].split(',')            # and create the tuple to build the dictionary.
        code = int(b[0]), int(b[1]), int(b[2])
        
        rgb_color_codes[color] = code
        
   return rgb_color_codes
