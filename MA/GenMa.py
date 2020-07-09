#!/cygdrive/c/Anaconda3/python.exe
import sys, os
import asyncio
from pathlib import Path
import pymysql
from NatsComponent import NatsComponent
import Util

nats_qt = "nats://192.168.20.185:4222"
qt_subject = "eb.qt.ltqtick.stk.cn.>"

class GenMa():
    nats_qt = None
    def __init__(self, asofdate):
        self.conn = pymysql.connect(host='192.168.0.56', port=3306, user='feadmin', passwd='feadmin000', db='sddb_cn')
        self.cur = self.conn.cursor()

        self.loop = asyncio.get_event_loop()
        if not GenMa.nats_qt:
            GenMa.nats_qt = NatsComponent(self.loop)
        self.connect(nats_qt)

        self.asofdate = asofdate
        self.step = 30

        logDir = f"{os.path.dirname(os.path.abspath(__file__))}/run/{self.asofdate}"
        if not os.path.exists(logDir):
            os.makedirs(logDir)
        self.logFp = open(f"{logDir}/{os.path.splitext(os.path.basename(sys.argv[0]))[0]}.log", "w")
        print(f"INFO: log dir: {self.logFp.name}")

        self.symMap = {}
        self.querySym()
        self.preHistClosePri()

    def connect(self, nats_qt):
        self.loop.run_until_complete(GenMa.nats_qt.connect([nats_qt]))
        print("INFO:connect oms nats success:%s"%(nats_qt))

    def subscribe(self):
        asyncio.run_coroutine_threadsafe(GenMa.nats_qt.subscribe(qt_subject, self.sub_handler_qt), loop=self.loop)
        self.loop.run_forever()

    def sub_handler_qt(self):
        pass

    def dbQuery(self, cmd):
        self.cur.execute(cmd)
        return self.cur.fetchall()

    def genQueryCloseCmd(self, ticker, date, rawName="*"):
        if not ticker or not date:
            print(f"ERROR:ticker={ticker}, date={date}")
        return f"SELECT {rawName} FROM sliu_ycz_dprc WHERE datadate={date} AND symbol = '{ticker}'"

    def genQuerySymCmd(self):
        return f"SELECT tic FROM fe_security WHERE permid IN (SELECT permid FROM fe_sym_set WHERE SYM_SET_NAME IN ('cn_csi_300','cn_csi_500') AND dead_date = 30000000 ORDER BY alive_date DESC)"
    
    def querySym(self):
        for line in self.dbQuery(self.genQuerySymCmd()):
            sym = line[0]
            if int(sym) >= 600000:
                self.symMap[f"sh{line[0]}"] = {'isLess30':False, 'closeArr':[], 'sum':0}
            else:
                self.symMap[f"sz{line[0]}"] = {'isLess30':False, 'closeArr':[], 'sum':0}

    def queryClosePri(self, ticker, date):
        for line in self.dbQuery(self.genQueryCloseCmd(ticker=ticker, date=date, rawName="close")):
            return line[0]

    def preHistClosePri(self):
        dateArr = Util.genTrdDateList(self.asofdate, self.step+1) #往前推31天，计算昨日的MA和今天的MA
        print(dateArr, len(dateArr))
        for sym in self.symMap.keys():
            closeArr = []
            for date in dateArr:
                closeArr.append(self.queryClosePri(sym, date))
            try:
                if (sum(closeArr[1:])/self.step)>closeArr[1]:
                    self.symMap[sym]['isLess30'] = True
                self.symMap[sym]['closeArr'] = closeArr[1:]
                self.symMap[sym]['sum'] = sum(closeArr[:-1])
            except:
                print(sym)


if __name__ == "__main__":
    genMa = GenMa("20200709")
    # print(genMa.symMap, len(genMa.symMap.keys()))
    targetSymArr = {}
    for sym in genMa.symMap.keys():
        if genMa.symMap[sym]['isLess30']:
            targetSymArr[sym]=genMa.symMap[sym]['closeArr']
    print(targetSymArr)

    genMa.conn.close()
