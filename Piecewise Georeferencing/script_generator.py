from PIL import Image
from PIL import ImageDraw
import numpy 

def transformblit(src_points,src_img,quad):
    if not quad:
        ((x11,x12), (x21,x22), (x31,x32)) = src_points
        # read image as RGB and add alpha (transparency)
        src_copy=src_img.copy()
        im = src_copy.convert("RGBA")

        # convert to numpy (for convenience)
        imArray = numpy.asarray(im)

        # create mask
        polygon =[(x11,x12), (x21,x22), (x31,x32)] 
        maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
        ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
        mask = numpy.array(maskIm)

        # assemble new image (uint8: 0-255)
        newImArray = numpy.empty(imArray.shape,dtype='uint8')

        # colors (three first columns, RGB)
        #newImArray[:,:,:] = imArray[:,:,:]

        # transparency (4th column)
        for i in range(4):
            newImArray[:,:,i] = mask*imArray[:,:,i]
        # back to Image from numpy
        newIm = Image.fromarray(newImArray, "RGBA")
        return newIm
    else:
        ((x11,x12), (x21,x22), (x31,x32),(x41,x42)) = src_points
        # read image as RGB and add alpha (transparency)
        src_copy=src_img.copy()
        im = src_copy.convert("RGBA")

        # convert to numpy (for convenience)
        imArray = numpy.asarray(im)

        # create mask
        polygon =[(x11,x12), (x21,x22), (x31,x32),(x41,x42)] 
        maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
        ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
        mask = numpy.array(maskIm)

        # assemble new image (uint8: 0-255)
        newImArray = numpy.empty(imArray.shape,dtype='uint8')

        # colors (three first columns, RGB)
        #newImArray[:,:,:] = imArray[:,:,:]

        # transparency (4th column)
        for i in range(4):
            newImArray[:,:,i] = mask*imArray[:,:,i]

        # back to Image from numpy
        newIm = Image.fromarray(newImArray, "RGBA")
        return newIm
def getScript(src_points,dst_points,trianglecount,srcLoc,dstloc,polynomial,resampling):
    trans_script="gdal_translate -of GTiff"
    warp_script="gdalwarp -r "+resampling+" -order "+polynomial+" -co COMPRESS=NONE -dstalpha -overwrite "
    
    for i in range(len(src_points)):
        trans_script=trans_script+" -gcp  {srclat} {srclong} {dstlat} {dstlong}".format(srclat=src_points[i][0],srclong=src_points[i][1],dstlat=dst_points[i][0],dstlong=dst_points[i][1])
    
    trans_script=trans_script+' "'+srcLoc+'"'+' "'+dstloc+'/temp/'+str(trianglecount)+'.png"'
    warp_script=warp_script+' "'+dstloc+'/temp/'+str(trianglecount)+'.png"'+' "'+dstloc+'/modified/out.tif"'
    
    return trans_script,warp_script
