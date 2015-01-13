import PIL
import PIL.ImageDraw 

def encode_message(original_image, message, color):
    """
    Encodes a message in the image provided by the user by changing pixels into a sequence in which letters are encoded
    The sequence works on a grid: Right is the letter (A: 1, Z: 26) while Down is the position (First Letter: 1).
    Provide an image file to modify, a message to encode, and a color for the pixels
    """
    
    #Create a new PIL Image object from the image provided
    image = PIL.Image.open(original_image)
    
    #Change the image mode to RGB
    image = image.convert('RGB')
    
    #Define variables for width and height
    width, height = image.size
    
    #Create an array of pixels representing the image
    pixels = image.load()
    
    #If the message is short enough
    if len(message) <= height:
        #Iterate through for every character in the message
        for y in range(len(message)):
            
            #Print the character to be encoded to the command line
            print message[y]
            
            #Set x to be a number from 1-26 representing letters
            x = ord(message[y]) - 96
            y = y + 1
            #If x is less than or equal to the width
            if x in range(width):
                
                #Set the pixel to the color specified by the user
                pixels[x, y] = color
        #Save the image as a modified PNG
        image.save('modified.png')
    else:
        print("The message is too long")

    
def decode_message(modified_image, color):
    """
    Decodes a message encoded by the user with encode_message() by iterating through the picture and generating ASCII codes
    for every pixel of the corresponding color. Provide the encoded image and the color of the pixels used to encode the message
    """
    #Create a variable for the filename where the message will be stored
    filename = "message.txt"
    
    #Load the message file
    message = open(filename, 'w')
    
    #Load the image which is encoded as a PIL image object
    image = PIL.Image.open(modified_image)
    
    #Variables for width and height
    width, height = image.size
    
    #Create an array of pixels representing the image
    pixels = image.load()
    
    #Iterate through every row in the image
    for y in range(height):
        
        #Iterate through every column of the image
        for x in range(width):
            
            #If the pixel[x,y] matches the color specified by the user as the encoded pixel color
            if pixels[x, y] == color:
                
                #Create a variable for the ASCII code of the pixel's position
                letter = x + 96
                
                #Write the letter represented by the letter variable to a file
                message.write(chr(letter))
                print(chr(letter))
                
def clear_image_of_color(image, color):
    """
    Clears the image of any pixels containing the given color, allowing you to use the given color to encode the message without errors.
    """
    
    #Create a variable storing how many pixels are changed
    pixels_changed = 0

    #Load the image which is encoded as a PIL image object
    image = PIL.Image.open(image)
    
    #Variables for width and height
    width, height = image.size
    
    #Create an array of pixels representing the image
    pixels = image.load()
    
    #Define a color very close to the original
    new_color = (color[0] - 1, color[1] - 1, color[2] - 1)
    
     #Iterate through every row in the image
    for y in range(height):
        
        #Iterate through every column of the image
        for x in range(width):
            
            #If the pixel[x,y] matches the color specified by the user as the encoded pixel color
            if pixels[x,y] == color:
                pixels[x,y] = new_color
                pixels_changed = pixels_changed + 1
    print(pixels_changed)
    
    #Save the modified image
    image.save("cleared.png")