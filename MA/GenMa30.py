#!/cygdrive/c/Anaconda3/python.exe
import sys, os
import asyncio
import datetime
from pathlib import Path
import pymysql
from NatsComponent import NatsComponent
import StockQuote_pb2
import Util
from optparse import OptionParser

nats_qt = "nats://192.168.20.185:4222"
qt_subject = "eb.qt.ltqtick.stk.cn.>"

def genMa30GetOptions():
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
                        default=30)

    (options, args) = parser.parse_args()
    return (options, args)

class GenMa30():
    nats_qt = None
    def __init__(self, options):
        self.conn = pymysql.connect(host='192.168.0.56', port=3306, user='feadmin', passwd='feadmin000', db='sddb_cn')
        self.cur = self.conn.cursor()

        self.loop = asyncio.get_event_loop()
        if not GenMa30.nats_qt:
            GenMa30.nats_qt = NatsComponent(self.loop)
        self.connect(nats_qt)

        self.asofdate = options.asofdate
        self.step = options.step

        logDir = f"{os.path.dirname(os.path.abspath(__file__))}/run/{self.asofdate}"
        if not os.path.exists(logDir):
            os.makedirs(logDir)
        self.logFp = open(f"{logDir}/{os.path.splitext(os.path.basename(sys.argv[0]))[0]}.log", "w")
        print(f"INFO: log dir: {self.logFp.name}")

        self.symMap = {}
        self.querySym()
        self.preHistClosePri()

        self.qt = StockQuote_pb2.StockQuote()

    def connect(self, nats_qt):
        self.loop.run_until_complete(GenMa30.nats_qt.connect([nats_qt]))
        print("INFO:connect oms nats success:%s"%(nats_qt))

    def subscribe(self):
        asyncio.run_coroutine_threadsafe(GenMa30.nats_qt.subscribe(qt_subject, self.sub_handler_qt), loop=self.loop)
        self.loop.run_forever()

    def sub_handler_qt(self, msg):
        self.qt.ParseFromString(msg.data[16:])
        sym = self.qt.sym
        if sym not in self.symMap.keys():
            return



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
                self.symMap[line[0]] = {'isMore30':False, 'isLess30':False, 'closeArr':[], 'sum':0, 'permid':line[1]}
            else:
                self.symMap[line[0]] = {'isMore30':False, 'isLess30':False, 'closeArr':[], 'sum':0, 'permid':line[1]}

    def queryClosePri(self, permid, date):
        for line in self.dbQuery(self.genQueryCloseCmd(permid=permid, date=date, rawName="close")):
            return line[0]

    def preHistClosePri(self):
        dateArr = Util.genTrdDateList(self.asofdate, self.step+1) #往前推31天，计算昨日的MA和今天的MA
        for sym in self.symMap.keys():
            closeArr = []
            for date in dateArr:
                closeArr.append(self.queryClosePri(self.symMap[sym]['permid'], date))
            try:
                if (sum(closeArr[1:])/self.step)>closeArr[1]:
                    self.symMap[sym]['isLess30'] = True
                if (sum(closeArr[:-1])/self.step)<=closeArr[0]:
                    self.symMap[sym]['isMore30'] = True
                self.symMap[sym]['closeArr'] = closeArr
                self.symMap[sym]['sum'] = sum(closeArr[:-1])
            except:
                pass
                # print(sym)


if __name__ == "__main__":
    (options, args) = genMa30GetOptions()
    # options.asofdate = ""
    genMa = GenMa30(options)
    targetSymArr = {}
    for sym in genMa.symMap.keys():
        if genMa.symMap[sym]['isLess30'] and genMa.symMap[sym]['isMore30']:
            targetSymArr[sym]=genMa.symMap[sym]['closeArr']
    print(targetSymArr.keys())

    genMa.conn.close()
