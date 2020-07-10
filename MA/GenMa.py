#!/cygdrive/c/Anaconda3/python.exe
import sys, os
# import asyncio
import datetime
from pathlib import Path
import pymysql
# from NatsComponent import NatsComponent
# import StockQuote_pb2
import Util
from optparse import OptionParser

nats_qt = "nats://192.168.20.185:4222"
qt_subject = "eb.qt.ltqtick.stk.cn.>"

def genMaGetOptions():
    parser = OptionParser(description="GenMa")
    parser.add_option("--asofdate",
                        dest="asofdate",
                        type = "str",
                        help="asofdate (default: %default)",
                        metavar="asofdate",
                        default=datetime.datetime.now().strftime("%Y%m%d"))
    parser.add_option("--step",
                        dest="step",
                        type = "int",
                        help="step (default: %default)",
                        metavar="step",
                        default=5)

    (options, args) = parser.parse_args()
    return (options, args)

class GenMa():
    nats_qt = None
    def __init__(self, options):
        # print(f"asofdate={options.asofdate}, step={options.step}")
        self.conn = pymysql.connect(host='192.168.0.56', port=3306, user='feadmin', passwd='feadmin000', db='sddb_cn')
        self.cur = self.conn.cursor()

        # self.loop = asyncio.get_event_loop()
        # if not .nats_qt:
        #     .nats_qt = NatsComponent(self.loop)
        # self.connect(nats_qt)

        self.asofdate = options.asofdate
        self.step = options.step

        # logDir = f"{os.path.dirname(os.path.abspath(__file__))}/run/{self.asofdate}"
        # if not os.path.exists(logDir):
        #     os.makedirs(logDir)
        # self.logFp = open(f"{logDir}/{os.path.splitext(os.path.basename(sys.argv[0]))[0]}.log", "w")
        # print(f"INFO: log dir: {self.logFp.name}")

        self.symMap = {}
        self.querySym()
        self.preHistClosePri()

        # self.qt = StockQuote_pb2.StockQuote()

    # def connect(self, nats_qt):
    #     self.loop.run_until_complete(.nats_qt.connect([nats_qt]))
    #     print("INFO:connect oms nats success:%s"%(nats_qt))

    # def subscribe(self):
    #     asyncio.run_coroutine_threadsafe(.nats_qt.subscribe(qt_subject, self.sub_handler_qt), loop=self.loop)
    #     self.loop.run_forever()

    # def sub_handler_qt(self, msg):
    #     self.qt.ParseFromString(msg.data[16:])
    #     sym = self.qt.sym
    #     if sym not in self.symMap.keys():
    #         return



    def dbQuery(self, cmd):
        self.cur.execute(cmd)
        return self.cur.fetchall()

    def genQueryCloseCmd(self, permid, date, rawName="*"):
        if not permid or not date:
            print(f"ERROR:permid={permid}, date={date}")

        if rawName == "close":
            rawName = "prccd_r_adj"
        return f"SELECT {rawName} FROM fe_sec_dstat WHERE datadate = {date} AND permid = {permid}"

    def genQuerySymCmd(self):
        return f"SELECT tic, permid FROM fe_security WHERE permid IN (SELECT permid FROM fe_sym_set WHERE SYM_SET_NAME IN ('cn_csi_300','cn_csi_500') AND dead_date = 30000000 ORDER BY alive_date DESC)"
    
    def querySym(self):
        for line in self.dbQuery(self.genQuerySymCmd()):
            sym = line[0]
            if int(sym) >= 600000:
                self.symMap[line[0]] = {'ma5_0':0, 'ma5_1':0, 'ma5_2':0, 'clo_0': 0, 'clo_1': 0, 'clo_2': 0, 'permid':line[1], 'closeArr_0':[], 'closeArr_1':[], 'closeArr_2':[]}
            else:
                self.symMap[line[0]] = {'ma5_0':0, 'ma5_1':0, 'ma5_2':0, 'clo_0': 0, 'clo_1': 0, 'clo_2': 0, 'permid':line[1], 'closeArr_0':[], 'closeArr_1':[], 'closeArr_2':[]}

    def queryClosePri(self, permid, date):
        for line in self.dbQuery(self.genQueryCloseCmd(permid=permid, date=date, rawName="close")):
            return line[0]

    def preHistClosePri(self):
        dateArr = Util.genTrdDateList(self.asofdate, self.step+2) #往前推7天，计算前天的MA昨日的MA和今天的MA
        for sym in self.symMap.keys():
            closeArr = []
            for date in dateArr:
                closeArr.append(self.queryClosePri(self.symMap[sym]['permid'], date))
            try:
                self.symMap[sym]['ma5_0'] = sum(closeArr[:-2])/self.step
                self.symMap[sym]['clo_0'] = closeArr[0]

                self.symMap[sym]['ma5_1'] = sum(closeArr[1:-1])/self.step
                self.symMap[sym]['clo_1'] = closeArr[1]

                self.symMap[sym]['ma5_2'] = sum(closeArr[2:])/self.step
                self.symMap[sym]['clo_2'] = closeArr[2]

                self.symMap[sym]['closeArr_0'] = closeArr[:-2]
                self.symMap[sym]['closeArr_1'] = closeArr[1:-1]
                self.symMap[sym]['closeArr_2'] = closeArr[2:]
            except:
                pass
                # print(sym)


if __name__ == "__main__":
    (options, args) = genMaGetOptions()
    # options.asofdate = "20200709"

    dateArr = Util.genTrdDateList(options.asofdate, 10)
    for date in dateArr:
        options.asofdate = date
        genMa = GenMa(options)
        targetSymArr = {}
        for sym in genMa.symMap.keys():
            symInfo = genMa.symMap[sym]
            if symInfo['ma5_0']<=symInfo['clo_0'] and symInfo['ma5_1']>symInfo['clo_1'] and symInfo['ma5_2']<=symInfo['clo_2'] and symInfo['ma5_2']>symInfo['ma5_1'] and symInfo['ma5_0']>symInfo['ma5_1']:
                targetSymArr[sym]=[symInfo['closeArr_0'], symInfo['closeArr_1'], symInfo['closeArr_2']]
        print(f"{date}:{targetSymArr.keys()}")

    genMa.conn.close()
