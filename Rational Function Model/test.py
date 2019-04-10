def divideInTriangles(Ui_obj,progressBar,srcPoints,dstPoints,srcLoc,dstLoc,threshold):
   os.system('mkdir '+dstLoc+'/modified')
   os.system('mkdir '+dstLoc+'/temp')
   npsrcPoints=np.array(srcPoints)
   srtriangles=spatial.Delaunay(npsrcPoints)
   npdstPoints=np.array(dstPoints)
   #image=Image.open(srcLoc)
   points=np.concatenate((npsrcPoints,npdstPoints),axis=1)
   #dstImg=Image.new(image.mode,image.size)
   statusArr=np.zeros((len(srtriangles.simplices),1))

   # For loop for all the triangles
   for i in range(len(srtriangles.simplices)):
      progressBar.setValue(float(i)/(len(srtriangles.simplices)-1)*100)
      if statusArr[i]==0:
         statusArr[i]=1
         srcTri=tuple(map(tuple,npsrcPoints[srtriangles.simplices][i]))
         dstTri=tuple(map(tuple,npdstPoints[srtriangles.simplices][i]))
         max_err=0
         max_err_src=None
         max_err_dst=None
         max_err_index=None
         for j in range(3):
            neighbour_index=srtriangles.neighbors[i][j]
            if not neighbour_index==-1 and statusArr[neighbour_index]==0:
               src_neighbours=npsrcPoints[srtriangles.simplices][neighbour_index]
            # Adding points of maximum error quadrilateral to src_quad
               src_quad=np.concatenate((src_neighbours,[npsrcPoints[srtriangles.simplices][i][j]]),axis=0)
               dst_neighbours=npdstPoints[srtriangles.simplices][neighbour_index]
               dst_quad=np.concatenate((dst_neighbours,[npdstPoints[srtriangles.simplices][i][j]]),axis=0)
               quad=np.concatenate((src_quad,dst_quad),axis=1)
               err=error.polynomial(1,quad,0,1,2,3)
               if err>max_err:
                  max_err_index=neighbour_index
                  max_err=err
                  max_err_src=src_quad
                  max_err_dst=dst_quad
         if max_err<threshold:
            #dstImg=script_generator.transformblit(srcTri,image,False)
            #dstImg.save(dstLoc+'/'+str(i)+'.png')

# Used for getting georeferencing script for 1st order polynomial

trans_script,warp_script=script_generator.getScript(srcTri,dstTri,i,srcLoc,dstLoc,"1","cubic")
         else:
            statusArr[max_err_index]=1
            #dstImg=script_generator.transformblit(max_err_src,image,True)
            #dstImg.save(dstLoc+'/'+str(i)+'.png')
            Ui_obj.showDial(i,max_err_src.tolist(),max_err_dst.tolist(),dstLoc,srcLoc)
   trans_script,warp_script= script_generator.getScript(npsrcPoints,npdstPoints,8,srcLoc,dstLoc,"1","cubic")
   os.system(trans_script)
   os.system(warp_script)
