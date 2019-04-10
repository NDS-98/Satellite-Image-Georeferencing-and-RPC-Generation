import numpy as np
import elevation
import time
from decimal import Decimal
import PyQt5
from PyQt5.QtWidgets import QMessageBox


class RPC:
    def __init__(self):
        self.pgbar = None
        self.inputfileLoc = None
        self.outputfileLoc = None
        self.rmse = 0

    def writeToFile(self):

        n = sum(1 for line in open(self.inputfileLoc))
        # n=151
        x = np.zeros(shape=(n,1))
        y = np.zeros(shape=(n,1))
        z = np.zeros(shape=(n,1))
        r = np.zeros(shape=(n,1))
        c = np.zeros(shape=(n,1))
        r_actual = np.zeros(shape=(n, 1))
        c_actual = np.zeros(shape=(n, 1))
        u = np.zeros(shape=(n,20))

        with open(self.inputfileLoc, 'r') as f:
            # for i in range(1):
            #      f.readline()
            data = f.readlines()

            i=0
            for line in data:
                words = line.split()
                r_actual[i][0] = words[1]
                c_actual[i][0] = words[2]
                y[i][0] = words[3]
                x[i][0] = words[4]
                i+= 1


        jump = 100/n
        # Getting elevation takes most of the time

        for i in range(n):
            try:
                z[i][0] = elevation.getelevation(x[i][0], y[i][0])
            except:
                # Internet connection is needed to access Google Maps Elevation API
                self.error("There might be a connection problem. Please check your Internet connection!")

            jump += 100/n
            self.pgbar.setValue(jump)
            PyQt5.QtWidgets.QApplication.processEvents()

        # Calculating offset and scale values
        offset_x = np.sum(x)/n
        offset_y = np.sum(y)/n
        offset_z = np.sum(z)/n
        offset_r = np.sum(r_actual)/n
        offset_c = np.sum(c_actual)/n

        scale_x = max(abs(np.max(x) - offset_x), abs(np.min(x) - offset_x))
        scale_y = max(abs(np.max(y) - offset_y), abs(np.min(y) - offset_y))
        scale_z = max(abs(np.max(z) - offset_z), abs(np.min(z) - offset_z))
        scale_r = max(abs(np.max(r_actual) - offset_r), abs(np.min(r_actual) - offset_r))
        scale_c = max(abs(np.max(c_actual) - offset_c), abs(np.min(c_actual) - offset_c))
        # scale_y = np.max(y) - np.min(y)
        # scale_z = np.max(z) - np.min(z)
        # scale_r = np.max(r) - np.min(r)
        # scale_c = np.max(c) - np.min(c)


        for i in range(n):

            x[i][0],y[i][0],z[i][0] = ((x[i][0]-offset_x)/scale_x), ((y[i][0]-offset_y)/scale_y), ((z[i][0]-offset_z)/scale_z)
            r[i][0] = ((r_actual[i][0]-offset_r)/scale_r)
            c[i][0] = ((c_actual[i][0] - offset_c) / scale_c)

            u[i] = [1, y[i][0], x[i][0], z[i][0], y[i][0]*x[i][0], y[i][0]*z[i][0], x[i][0]*z[i][0], y[i][0]*y[i][0],
                    x[i][0]*x[i][0], z[i][0]*z[i][0], x[i][0]*y[i][0]*z[i][0], y[i][0]*y[i][0]*y[i][0],
                    y[i][0]*x[i][0]*x[i][0], y[i][0]*z[i][0]*z[i][0], y[i][0]*y[i][0]*x[i][0], x[i][0]*x[i][0]*x[i][0],
                    x[i][0]*z[i][0]*z[i][0], y[i][0]*y[i][0]*z[i][0], x[i][0]*x[i][0]*z[i][0], z[i][0]*z[i][0]*z[i][0]]


        v = np.delete(u, np.s_[0:1], axis=1)

        v_r = v*-r
        M = np.hstack([u,v_r])
        mTranspose = M.transpose()
        m_inverse = np.linalg.inv(np.dot(mTranspose,M))
        j = np.linalg.multi_dot([m_inverse,mTranspose,r])

        v_c = v*-c;
        N = np.hstack([u,v_c])
        nTranspose = N.transpose()
        n_inverse = np.linalg.inv(np.dot(nTranspose, N))
        k = np.linalg.multi_dot([n_inverse, nTranspose, c])

        # Opening file using user specified location
        f = open(self.outputfileLoc+"/"+self.inputfileLoc[self.inputfileLoc.rfind('/')+1:self.inputfileLoc.rfind('.')]+"_rpc.txt",'w+')

        L = ["LINE_OFF: "+ ["", "+"][offset_r > 0] +  str(offset_r)+" pixels\n",
            "SAMP_OFF: "+ ["", "+"][offset_c > 0] +  str(offset_c)+" pixels\n",
            "LAT_OFF: "+ ["", "+"][offset_x > 0] +  str(offset_x)+" degrees\n",
            "LONG_OFF: "+ ["", "+"][offset_y > 0] +  str(offset_y)+" degrees\n",
            "HEIGHT_OFF: "+ ["", "+"][offset_z > 0] +  str(offset_z)+" meters\n",
            "LINE_SCALE: "+ ["", "+"][scale_r > 0] +  str(scale_r)+" pixels\n",
            "SAMP_SCALE: "+ ["", "+"][scale_c > 0] +  str(scale_c)+" pixels\n",
            "LAT_SCALE: "+ ["", "+"][scale_x > 0] +  str(scale_x)+" degrees\n",
            "LONG_SCALE: "+ ["", "+"][scale_y > 0] +  str(scale_y)+" degrees\n",
            "HEIGHT_SCALE: "+ ["", "+"][scale_z > 0] +  str(scale_z)+" meters\n"]

        f.writelines(L)

        for i in range(20):
            f.write("LINE_NUM_COEFF_"+str(i+1)+": " + ["", "+"][j[i][0] > 0] +  str('%.15E' % Decimal(j[i][0]))+"\n")
        f.write("LINE_DEN_COEFF_1: 1.000000000000000e+00\n")
        for i in range(19):
            f.write("LINE_DEN_COEFF_"+str(i+2)+": " + ["", "+"][j[20+i][0] > 0] +  str('%.15E' % Decimal(j[20+i][0]))+"\n")

        for i in range(20):
            f.write("SAMP_NUM_COEFF_"+str(i+1)+": " + ["", "+"][k[i][0] > 0] +  str('%.15E' % Decimal(k[i][0]))+"\n")
        f.write("SAMP_DEN_COEFF_1: 1.000000000000000e+00\n")
        for i in range(19):
            f.write("SAMP_DEN_COEFF_"+str(i+2)+": " + ["", "+"][k[20+i][0] > 0] +  str('%.15E' % Decimal(k[20+i][0]))+"\n")

        f.close()
        # print(J)
        # print()
        # print(K)

        coeff_a = j[0:20]
        coeff_b = j[20:]
        coeff_b = np.insert(coeff_b, 0, 1).reshape(20, 1)

        coeff_c = k[0:20]
        coeff_d = k[20:]
        coeff_d = np.insert(coeff_d, 0, 1).reshape(20, 1)

        r_new = (np.dot(u, coeff_a)) / (np.dot(u, coeff_b)) * scale_r + offset_r
        c_new = (np.dot(u, coeff_c)) / (np.dot(u, coeff_d)) * scale_c + offset_c

        r_c = np.hstack((r_new - r_actual, c_new - c_actual))
        # print()
        print(r_c)

        squared = r_c ** 2

        squared_sum = np.sum(squared)

        mse = squared_sum / n

        self.rmse = np.sqrt(mse)
        print()
        print(self.rmse)

    ########################################################################

    # Display error message
    def error(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle("Error")
        msg.resize(300,150)

        msg.show()
        msg.exec_()

########################################################################

