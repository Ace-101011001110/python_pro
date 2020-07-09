#!/cygdrive/c/Anaconda3/python.exe

import sys
appDir="%s/Fairedge_dev/app_MktOMS"%("c:" if sys.platform=="win32" else "")
sys.path.append(appDir)

import os
import subprocess
import re
import glob
import sys, stat
import time
import pytz
import socket
import getpass
import datetime
import hashlib
import toNative

from QpsDirs import *
from QpsSys import *
from QpsVts import *
from QpsDate import *
from QpsDatetime import *
from QpsCondor import *

def BN():
	return "751"

def FeConfigDir():
	return toNative.getNativePath("c:/fe/config")

sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0

def high2low(a,b):
	if a > b:
		return -1
	elif a == b:
		return 0
	else:
		return 1

def sed_replace(pattern, fromFn, toFn, verbose = 0):
	patternNative=pattern
	if sys.platform!="win32":	#unixlike
		patternNative="%ss/^c:\//python \//ig;s/\.bn[0-9][0-9][0-9]\//\//g;s/\.exe/.py/g;s/c:\//\//ig;s/\/FE\//\/fe\//g;s/\/Quanpass\//\/quanpass\//g;"%(patternNative)
	cmd = "%s -e \"%s\" %s > %s"%(toNative.getCmdBin("sed"),patternNative, fromFn.replace('^', '^^'), toFn.replace('^', '^^'))
	#print >> sys.stderr,cmd
	if verbose:
		print(cmd, file=sys.stderr)
	run_cmd(cmd, expandHat=0)

def dir_chain(dir):
	dirElem = dir.split('/')
	dirChain = []
	for i in xrange(2,len(dirElem)):
		dirChain.append('/'.join(dirElem[0:i+1]))
	return dirChain

def msgPrompt(dryrun, other):
	if dryrun:
		return "DRYRUN"
	else:
		return other

def print_help(command, waitFinish=0, debug=0):
	out = []
	for ln in run_command(command, waitFinish=waitFinish):
		ln = ln.strip()
		skip=0
		for skipPhrase in ("ERR",
						   "IFO",
						   "INF",
						   "zonespec database",
						   "getCfgFilePath",
						   "evt_meta_types.txt"):
			if ln.find(skipPhrase)>=0:
				skip=1
				break
		if skip==0:
			print(ln, file=sys.stdout)



def m4gen(outFn, inFnList, dbg):
	with open(outFn, 'w') as output:
		cmd = ["c:/cygwin/bin/m4.exe" if sys.platform=="win32" else "m4"]
		#cmd.append("-P")#--prefix-builtins
		for fn in inFnList:
			if os.path.exists(fn):
				cmd.append(fn)
		#print >> sys.stderr, "gen %s, cmd %s"%(outFn, cmd)
		if(dbg):
			print("gen %s, cmd %s"%(outFn, cmd), file=sys.stderr)

		subprocess.call(cmd, stdout=output)

def cvs_add_dir(pathToAdd):
	cmd = "%s %s --cfg %s %s"%(toNative.getCmdBin("perl"),toNative.getNativePath("c:/fe/scripts/auto_cvs.pl"), toNative.getNativePath("c:/quanpass/config/sid_auto_cvs.txt"), pathToAdd)
	print(cmd, file=sys.stderr)
	os.system(cmd)


def uncommentJS(js):
	list = re.findall('(\"([^\\\"]*(\\.)?)*\")|(\'([^\\\']*(\\.)?)*\')|(\/{2,}.*?(\r|\n))|(\/\*(\n|.)*?\*\/)',js) #remove notes //:6 /**/:8
	for array in list:
		if(array[6]!=None):
			js = js.replace(array[6],'')
		if(array[8]!=None):
			js = js.replace(array[8],'')
	return js


def getAttr(options, attr):
	if not hasattr(options, attr):
		return False
	return getattr(options, attr)


def python_version():
	s = run_command("python.exe --version")
	output = [x for x in s]
	return ''.join(output).strip()

def idxdt2trddt(idxdt, tm, offset=0):
	(prevdate, nextdate) = getPrevNextBusinessDay(str(idxdt))
	tmHour = int(tm.split(":")[0])
	if tmHour > 17:
		return nextdate
	else:
		return idxdt

def trddt2idxdt(trddt, tm, offset=0):
	(prevdate, nextdate) = getPrevNextBusinessDay(str(trddt))
	tmHour = int(tm.split(":")[0])
	if tmHour > 17:
		return prevdate
	else:
		return trddt

def pk2sym(pk):
	return pk.split(":")[2]

def pk2bk(pk):
	return pk.split(":")[1]

def pk2bn(pk):
	return pk.split(":")[0]


if __name__=='__main__':
	""" 		
		#print(getNetworkFileUsingCache("N:/FE/xyft/config/ContMktSym.txt"), file=sys.stdout)
		#copyNetworkFileUsingCache("N:/FE/xyft/config/ContMktSym.txt", "c:/temp")
		print(python_version(), file=sys.stdout)		
		
		print_error("foobar", 3, file=sys.stdout)
		print(getDefaultBn(), file=sys.stdout)
		print_error("foobar2", 4, file=sys.stdout)

		for testListname in ['NXOM', 'NXNM', 'NXP']:
			print("INFO: listname=%s, category=%s"%(testListname, listname2TacticCategory(testListname)), file=sys.stdout)

		getFundCategory2Listnames()

		print("INFO: getDayRangeList('cn', 20170911, 20170912) returns %s"%(','.join([str(x) for x in getDayRangeList("cn", 20170911, 20170912)])), file=sys.stdout)
		print("INFO: getDayRangeList('cn', 20170912, 20170912) returns %s"%(','.join([str(x) for x in getDayRangeList("cn", 20170912, 20170912)])), file=sys.stdout)
		print("INFO: getDayRangeList('cn', 20170912, 20170912, 0, 0) returns %s"%(','.join([str(x) for x in getDayRangeList("cn", 20170912, 20170912, -1, 2)])), file=sys.stdout)
		print("INFO: getDayRangeList('cn', 20150105, 20170912, 0, 0) returns %s"%(','.join([str(x) for x in getDayRangeList("cn", "20150105", "20170912", 0, 0)])), file=sys.stdout)


		print( "Test splitBnListname:  %s"%("=".join(splitBnListname("0NXDP_TC949cd9"))), file=sys.stdout)
		print( "Test splitBnListname:  %s"%("=".join(splitBnListname("10XDP_TC949cd9"))), file=sys.stdout)
		print( "Test splitBnListname:  %s"%("=".join(splitBnListname("XDP_TC949cd9"))), file=sys.stdout)

		dir_chain("h:/FE_dev.v6.DEV/src/cmn/hrt")

		print(getuser(), file=sys.stdout)
		print(getuser(), file=sys.stdout)

		print(is_junction_dir("h:/FE_dev.v6.DEV/src"), file=sys.stdout)
		print(is_junction_dir("h:/FE_dev.v6.DEV/src/cmn"), file=sys.stdout)
		print(is_junction_dir("h:/FE_dev.v6.DEV/src/cmn/hrt"), file=sys.stdout)
		print(gettoday(), file=sys.stdout)

		#print_help("c:/Python27/python.exe c:/Quanpass/programs/python/strategies/scnOpt.py -h")

		get_bn_cfg(verbose=True)

		print(get_bn_cmd(toNative.getPy("/cygdrive/c/quanpass/programs/python/strategies.bn203/doVtsScn.exe")), file=sys.stdout)
		print(get_bn_cmd(toNative.getNativePath("/cygdrive/c/fe/vts.900.rel/bin/vts%s"%(".exe" if sys.platform=="win32" else ""))), file=sys.stdout)

		mkdir([toNative.getNativePath("c:/temp/test_dir")])
		create_junction_dir(toNative.getNativePath("c:/temp/test_dir_junction"), toNative.getNativePath("c:/temp/test_dir"), verbose=1)

		#print "INFO: found_condor_err = %d"%(check_condor_error("c:/fe/simu/lcai/chna/study_cfrev_opntf_w2/AA02/date^20161230.e74a_c58c/20161011.subtask"))

		#print "\n".join(open_readlines("c:/FE/stratfunds/ZS0/fund_tactic_config_NGT.frz.full"))

		testFn = toNative.getNativePath("c:/fe/simu/cli/chna/study_pair_AAxx/AA00/macro_pair8_fsm_freeze.FZ_bn206.SP_L.FC_4e94.REF_cfb6bf8a.tar.gz")
		newFn = remapFreezeFn(testFn, toNative.getNativePath("c:/fe/stratalloc/cn_futr_alloc_candidates/%s~"%("TEST")))
		recoverFn = reverseFreezeFn(newFn, toNative.getNativePath("c:/fe/stratalloc/cn_futr_alloc_candidates/%s~"%("TEST")))
		if (testFn != recoverFn):
			print(recoverFn, file=sys.stdout)

		run_cmd("%s %s %s"%(toNative.getCmdBin("cp"),toNative.getNativePath("c:/temp/test.txt"), toNative.getNativePath("c:/temp/test2.txt")), quiet=1, debug=1)

		print("INFO: getLastLimtPriceDate %s"%(getLastLimtPriceDate()), file=sys.stdout)

		subtaskDir = toNative.getNativePath("c:/fe/simu/lcai/chna/study_nsrev_regtime_speedup2_seg2_delist/AA00/date^20180330.1d42_58b0/20180102.subtask")
		print("INFO: %s isNightSessionTactic %s"%(subtaskDir, isNightSessionTactic(subtaskDir)), file=sys.stdout)
	"""
	try:
		print("INFO:  getexchdate('CN', today='20180221') = %s, prevNextBusinessDay=%s"%(getexchdate('CN', today='20180221'), " ".join(getPrevNextBusinessDay())), file=sys.stdout)
		print("INFO:  getexchdate('US', today='20180221') = %s, prevNextBusinessDay=%s"%(getexchdate('US', today='20180221'), " ".join(getPrevNextBusinessDay(today=getexchdate("US"), region="US", ))), file=sys.stdout)
		print("INFO:  getexchdate('US', today='20180221') = %s, prevNextBusinessDay=%s"%(getexchdate('US'), " ".join(getPrevNextBusinessDay(today=getexchdate("US"), region="US", ))), file=sys.stdout)
		print("INFO:  getexchdate('US', today='20180221') = %s, prevNextBusinessDay=%s"%(getexchdate('CN'), " ".join(getPrevNextBusinessDay(today=getexchdate("CN"), region="CN", ))), file=sys.stdout)

		print(idxdt2trddt('20190115', '00:01:00.000'), file=sys.stdout)
		print(idxdt2trddt('20190115', '09:00:00.000'), file=sys.stdout)
		print(idxdt2trddt('20190115', '15:00:00.000'), file=sys.stdout)
		print(idxdt2trddt('20190115', '21:00:00.000'), file=sys.stdout)

		print(trddt2idxdt('20190115', '00:01:00.000'), file=sys.stdout)
		print(trddt2idxdt('20190115', '9:00:00.000'), file=sys.stdout)
		print(trddt2idxdt('20190115', '15:00:00.000'), file=sys.stdout)
		print(trddt2idxdt('20190115', '21:00:00.000'), file=sys.stdout)
		print(trddt2idxdt(20190118, "16:00:00.000"), file=sys.stdout)
		print("Found dates in str: %s"%(",".join(find_dates_in_str("R:/cloudvts/simu/che/chna/study_trd_cross_day_example03/AA00/date^20190329.ef8d_8cd4/20190115.subtask/20190115.pos"))), file=sys.stdout)

		print("getexchdate('CN')  %s"%(getexchdate('CN')), file=sys.stdout)
		print("getexchdate('US')  %s"%(getexchdate('US')), file=sys.stdout)

		print("asofdate=%s, prevdate=%s, tradedate=%s, nextdate=%s"%(
			getDatesCfg("asofdate"), getDatesCfg("prevdate"), 
			getDatesCfg("tradedate"), getDatesCfg("nextdate")), file=sys.stdout)

#		fn = "C:/Quanpass/programs/python/regtests/EM_missing_iid.PNG"
#		print("file md5 %s %s %s"%(fn, file2md5(fn), getFileMd5(fn)), file=sys.stdout)

		print(user_dir("che"))
	
	except Exception as e:
		print(e)
