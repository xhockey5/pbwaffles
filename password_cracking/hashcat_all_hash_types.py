import subprocess as sp
import time

hashtypes = ['0', '10', '20', '30', '40', '50', '60', '100', '110', '120', '130', '140', '150',
             '160', '200', '300', '400', '500', '900', '1000', '1100', '1400', '1410', '1420',
             '1430', '1431', '1440', '1450', '1460', '1600', '1700', '1710', '1720', '1730',
             '1740', '1750', '1760', '1800', '2400', '2410', '2500', '2600', '3200', '3300',
             '3500', '3610', '3710', '3720', '3800', '3910', '4010', '4110', '4210', '4300',
             '4400', '4500', '4600', '4700', '4800', '4900', '5000', '5100', '5300',
             '5400', '5500', '5600', '5700', '5800', '6300', '6400', '6500', '6700', '6900',
             '7000', '7100', '7200', '7300', '7400', '7900', '8400', '8900', '9200', '9300',
             '10000', '10200', '10300', '11000', '11100', '11200', '11400', '99999',
             '11', '12', '21', '23', '101', '111', '112', '121', '122', '123', '124', '131',
             '132', '133', '141', '1421', '1441', '1711', '1722', '1731', '2611', '2612', '2711',
             '2811', '3711', '3721', '7600']

for hashtype in hashtypes:
    args = ['hashcat', '-m', hashtype, '/root/NCL/passtocrack.txt', '/root/NCL/sortedpokemon.txt', '--outfile=crackedpasswords.txt', '--outfile-format=3']
    print args
    try:
        sp.check_call(args)
    except sp.CalledProcessError:
        print 'wrong hash type...'
