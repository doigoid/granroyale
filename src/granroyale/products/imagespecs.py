from imagekit.specs import ImageSpec 
from imagekit import processors 

# first we define our thumbnail resize processor 
class ResizeSquareThumb(processors.Resize): 
    width = 75
    height = 75
    crop = True

class ResizeHorizThumb(processors.Resize):
    width = 215

class ResizeVertThumb(processors.Resize):
    height = 125

# now we define a display size resize processor
class ResizeDisplay(processors.Resize):
    width = 580
    height = 340

class ResizeMedium(processors.Resize):
    width = 250
    
# now lets create an adjustment processor to enhance the image at small sizes 
class EnhanceThumb(processors.Adjustment): 
    contrast = 1.2 
    sharpness = 1.1 

# now we can define our thumbnail spec 
class HorizThumbnail(ImageSpec): 
    access_as = 'h_thumbnail_image' 
    pre_cache = True 
    processors = [ResizeHorizThumb, EnhanceThumb] 

class VertThumbnail(ImageSpec): 
    access_as = 'v_thumbnail_image' 
    pre_cache = True 
    processors = [ResizeVertThumb, EnhanceThumb] 

class SquareThumbnail(ImageSpec):
    access_as = 's_thumbnail_image'
    pre_cache = True
    processors = [ResizeSquareThumb]

class Medium(ImageSpec):
    access_as = "medium_image"
    pre_cache = True
    processors = [ResizeMedium,]
    
# and our display spec
class Display(ImageSpec):
    increment_count = True
    processors = [ResizeDisplay]

    
