from gpsMessageFile import GpsMessageFile
from nose.tools import assert_equals

fileContent = ["G01 2017 02 13 22 00 00 4.918128252029E-05 9.094947017729E-13 0.000000000000E+00",
               "     6.000000000000E+00-7.018750000000E+01 4.509830709694E-09-2.275517339128E+00",
               "    -3.596767783165E-06 6.229116464965E-03 4.574656486511E-06 5.153692497253E+03",
               "     1.656000000000E+05 9.313225746155E-09-6.361854098473E-01-5.960464477539E-08",
               "     9.666622276019E-01 2.948750000000E+02 5.418360356115E-01-8.197841473003E-09",
               "    -2.078658013021E-10 1.000000000000E+00 1.936000000000E+03 0.000000000000E+00",
               "     2.000000000000E+00 0.000000000000E+00 5.122274160385E-09 6.000000000000E+00",
               "     1.584180000000E+05 4.000000000000E+00"]
gps = GpsMessageFile(fileContent)

def test_09():
    f = ["G01 2017 02 13 22 00 00 4.918128252029E-05 9.094947017729E-13 0.000000000000E+00",
                   "     6.000000000000E+00-7.018750000000E+01 4.509830709694E-09-2.275517339128E+00",
                   "    -3.596767783165E-06 6.229116464965E-03 4.574656486511E-06 5.153692497253E+03",
                   "     1.656000000000E+05 9.313225746155E-09-6.361854098473E-01-5.960464477539E-08",
                   "     9.666622276019E-01 2.948750000000E+02 5.418360356115E-01-8.197841473003E-09",
                   "    -2.078658013021E-10 1.000000000000E+00 1.936000000000E+03 0.000000000000E+00",
                   "     2.000000000000E+00 0.000000000000E+00 5.122274160385E-09 6.000000000000E+00",
                   "     1.584180000000E+05 4.000000000000E+00"]
    g = GpsMessageFile(fileContent)
    g.sv_clock_bias = 600
    g.sqrtA = 5153.70151138
    g.deltaN = 0.51052126526E-8
    g.m0 = -2.566425905#E-4
    g.omega = 0.2339967413720
    g.eccentricity = 4.392384667880E-3
    g.deltaN = 6.677063840800E-9
    g.toeTime = 14400
    g.cuc = -1.553446054460E-6
    g.cus = 3.330409526820E-6
    g.crc = 283.21875
    g.crs = -31.96875
    g.cic = -8.75443220139E-8
    g.cis = 1.43423676491E-7
    g.idot = -3.314423773340E-10
    g.i0 = 0.9002982524
    g.omega0 = -1.09222818
    g.omegaDot = -9.302887502600E-9

    assert_equals(round(g.n0(),13),1.458515787E-4)
    assert_equals(round(g.n(),8),round(1.458566839E-4,8))
    assert_equals(round(g.M(),5),round(-2.478911895,5))
    assert_equals(round(g.E(),2),round(-2.483339711,2))
    assert_equals(g.V(),3.7954303710)
    assert_equals(g.tetaU(),0.0000077489)
    assert_equals(-14951033.509,g.x_OrbitalPlane())
    assert_equals(-22136660.810,g.y_OrbitalPlane())

#eighth line
def test_08():
    assert_equals(gps.transTime, 1.584180000000E+05)
    assert_equals(gps.fitInterval, 4.000000000000E+00)


#seventh line
def test_07():
    assert_equals(gps.svAccuracy, 2.000000000000E+00)
    assert_equals(gps.svHealth, 0.000000000000E+00)
    assert_equals(gps.tgd, 5.122274160385E-09)
    assert_equals(gps.iodc, 6.000000000000E+00)

#sixth line
def test_06():
    assert_equals(gps.idot, -2.078658013021E-10)
    assert_equals(gps.codesL2Channel, 1.000000000000E+00)
    assert_equals(gps.gpsWeek, 1.936000000000E+03)
    assert_equals(gps.l2PDataFlag, 0.000000000000E+00)

#fifth line
def test_05():
    assert_equals(gps.i0, 9.666622276019E-01)
    assert_equals(gps.crc, 2.948750000000E+02)
    assert_equals(gps.omega, 5.418360356115E-01)
    assert_equals(gps.omegaDot, -8.197841473003E-09)

#fourth line
def test_04():
    assert_equals(gps.toeTime, 1.656000000000E+05)
    assert_equals(gps.cic, 9.313225746155E-09)
    assert_equals(gps.omega0, -6.361854098473E-01)
    assert_equals(gps.cis, -5.960464477539E-08)

#third line
def test_03():
    assert_equals(gps.cuc, -3.596767783165E-06)
    assert_equals(gps.eccentricity, 6.229116464965E-03)
    assert_equals(gps.cus, 4.574656486511E-06)
    assert_equals(gps.sqrtA, 5.153692497253E+03)

#second line
def test_02():
    assert_equals(gps.iode, 6.000000000000E+00)
    assert_equals(gps.crs, -7.018750000000E+01)
    assert_equals(gps.deltaN, 4.509830709694E-09)
    assert_equals(gps.m0, -2.275517339128E+00)

#first line
def test_01():
    assert_equals(gps.sat_number, "G01")
    assert_equals(gps.epochYear, "2017")
    assert_equals(gps.epochMonth, "02")
    assert_equals(gps.epochDay, "13")
    assert_equals(gps.epochHour, "22")
    assert_equals(gps.epochMinute, "00")
    assert_equals(gps.epochSecond, "00")
    assert_equals(gps.sv_clock_bias, 4.918128252029E-05)
    assert_equals(gps.sv_clock_drift, 9.094947017729E-13)
    assert_equals(gps.sv_clock_drift_rate, 0.000000000000E+00)
