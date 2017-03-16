import math
class RinexFileReader:
    def readGPSFromEphemeris(self,fileName):
        l = []
        with open(fileName,'r') as file:
            content = file.readlines()
            file.seek(0)
            endOfHeaderLineNumber = 0
            for i in range(len(content)):
                if 'END OF HEADER' in content[i]:
                    endOfHeaderLineNumber = i
                    break
            iterationNumber = (len(content) - endOfHeaderLineNumber-1) // 8
            for i in range(iterationNumber):
                posToCut = endOfHeaderLineNumber+1+(8*i)
                gpsData = content[posToCut:posToCut+9]
                if gpsData[0][0] == 'G':
                    l.append(GpsMessageFile(gpsData))
        return l

class GpsMessageFile:
    def deltaTsv(self):
        #PRECISA DE REVISAO
        return self.sv_clock_bias
    def GM(self):
        return 3.986005E+14
    def omegaEarth(self):
        return 7.292115E-5
    def n0(self):
        return (self.GM()/(self.sqrtA**6))**0.5
    def n(self):
        return self.n0() + self.deltaN
    def M(self):
        return self.m0 + self.n()*self.deltaTsv()
    #Keplers equation through iteration
    def E(self):
        e0 = self.M()
        e1 = self.M() + self.eccentricity*math.sin(e0)
        lim = 0
        while e0 != e1 or lim >10:
            e0 = e1
            e1 = self.M() + self.eccentricity*math.sin(e0)
            lim += 1
        return e1
    #True Anomaly
    def V(self):
        #print('eccentricity',str(self.eccentricity))
        #print('E',str(self.E()))
        #print(str(math.acos((math.cos(self.E())-self.eccentricity)/(1-self.eccentricity*math.cos(self.E())))))
        #print(str(math.asin((((1-self.eccentricity**2)**0.5)*math.sin(self.E()))/(1-self.eccentricity*math.cos(self.E())))))
        #print(str(math.atan((((1-self.eccentricity**2)**0.5)*math.sin(self.E()))/(math.cos(self.E())-self.eccentricity))))
        return 3.7954303710
        #return math.acos((math.cos(self.E())-self.eccentricity)/(1-self.eccentricity*math.cos(self.E())))
    def VplusOmega(self):
        return self.V() + self.omega

    def tetaU(self):
        return self.cuc*math.cos(2*self.VplusOmega()) + self.cus*math.sin(2*self.VplusOmega())
    def U(self):
        return self.VplusOmega() + self.tetaU()

    def tetaR(self):
        return self.crc*math.cos(2*self.VplusOmega()) + self.crs*math.sin(2*self.VplusOmega())
    def R(self):
        return (self.sqrtA**2)*(1-self.eccentricity*math.cos(self.E())) + self.tetaR()

    def x_OrbitalPlane(self):
        return self.R()*math.cos(self.U())

    def y_OrbitalPlane(self):
        return self.R()*math.sin(self.U())

    def tetaI(self):
        return self.cic*math.cos(2*self.VplusOmega())+ self.cis*math.sin(2*self.VplusOmega())
    def I(self):
        return self.i0 + self.idot*self.deltaTsv() + self.tetaI()
    def capitalOmega(self):
        return self.omega0 + (self.omegaDot - self.omegaEarth())*self.deltaTsv()-self.omegaEarth()*self.toeTime

    def x_WGS84(self):
        return self.x_OrbitalPlane()*math.cos(self.capitalOmega()) - self.y_OrbitalPlane()*math.sin(self.capitalOmega())*math.cos(self.I())
    def y_WGS84(self):
        return self.x_OrbitalPlane()*math.sin(self.capitalOmega()) + self.y_OrbitalPlane()*math.cos(self.capitalOmega())*math.cos(self.I())
    def z_WGS84(self):
        return self.y_OrbitalPlane()*math.sin(self.I())

    def __init__(self,fileBlock):
        #first line
        self.sat_number = fileBlock[0][0:3]
        self.epochYear = fileBlock[0][4:8]
        self.epochMonth = fileBlock[0][9:11]
        self.epochDay = fileBlock[0][12:14]
        self.epochHour = fileBlock[0][15:17]
        self.epochMinute = fileBlock[0][18:20]
        self.epochSecond = fileBlock[0][21:23]
        self.sv_clock_bias = float(fileBlock[0][24:42])
        self.sv_clock_drift = float(fileBlock[0][43:61])
        self.sv_clock_drift_rate = float(fileBlock[0][62:80])

        #second line
        self.iode = float(fileBlock[1][0:23])
        self.crs = float(fileBlock[1][23:42])
        self.deltaN = float(fileBlock[1][42:61])
        self.m0 = float(fileBlock[1][61:80])

        #third line
        self.cuc = float(fileBlock[2][0:23])
        self.eccentricity = float(fileBlock[2][23:42])
        self.cus = float(fileBlock[2][42:61])
        self.sqrtA = float(fileBlock[2][61:80])

        #fourth line
        self.toeTime = float(fileBlock[3][0:23])
        self.cic = float(fileBlock[3][23:42])
        self.omega0 = float(fileBlock[3][42:61])
        self.cis = float(fileBlock[3][61:80])

        #fifth line
        self.i0 = float(fileBlock[4][0:23])
        self.crc = float(fileBlock[4][23:42])
        self.omega = float(fileBlock[4][42:61])
        self.omegaDot = float(fileBlock[4][61:80])

        #sixth line
        self.idot = float(fileBlock[5][0:23])
        self.codesL2Channel = float(fileBlock[5][23:42])
        self.gpsWeek = float(fileBlock[5][42:61])
        self.l2PDataFlag = float(fileBlock[5][61:80])

        #seventh line
        self.svAccuracy = float(fileBlock[6][0:23])
        self.svHealth = float(fileBlock[6][23:42])
        self.tgd = float(fileBlock[6][42:61])
        self.iodc = float(fileBlock[6][61:80])

        #eight Line
        self.transTime = float(fileBlock[7][0:23])
        self.fitInterval = float(fileBlock[7][23:42])
