import argparse
import os
import os.path
import subprocess
import sys
import threading
import time
import collections

tests = 3
devnull = open(os.devnull, 'wb')

testFile = "index.html"
testFilePath = "/home/ar1778/chromium2/src/quic-data/www.example.org/" + testFile

# commands for tc netem
netemCommandDelete = "sudo tc qdisc del dev lo root"
netemCommandShow = "sudo tc qdisc show dev lo"
netemCommandRoot = "sudo tc qdisc add dev lo root handle 1: netem "
netemCommandLatencyAddendum = " delay ***ms"
netemCommandPacketLossAddendum = " loss ***%"

quicClientCommand = "./home/ar1778/chromium2/src/out/Default/quic_client --host=127.0.0.1 --disable-certificate-verification --port=6121 www.example.org/index.html > ./tmp/download"

# tcpdump commands
pcapTouch = "touch /tmp/test.pcap"
tcpdumpCapture = ["/usr/bin/sudo", "/usr/sbin/tcpdump", "-i", "lo", "-w", "/tmp/test.pcap"]
tcpdumpCaptureKill = "sudo kill "
tcpdumpAnalyze = "sudo tcpdump -T quic -r /tmp/test.pcap -tttttnnqv > *** 2>/dev/null"

def main():
	parser = argparse.ArgumentParser(
		description="   gQUIC metric evaluator")
	parser.add_argument("-l", "--packetloss", nargs="+", type=float, help="Packet loss", default="0")
	parser.add_argument("-d", "--delay", nargs="+", type=int, help="network delay (in ms)", default="0")
	args = parser.parse_args()

	class params:
		def __init__(self, packetloss, delay):
			self.packetloss = packetloss
			self.delay = delay
	paramsQueue = collections.deque()

	if not isinstance(args.packetloss, collections.Iterable):
		args.packetloss = [args.packetloss]
	if not isinstance(args.delay, collections.Iterable):
		args.delay = [args.delay]

	for packetloss in args.packetloss:
		for delay in args.delay:
				paramsQueue.append(params(packetloss, delay))

	def netemConfig(params):

        if params.delay > 0:
		    netemCommandConfigTmp = netemCommandRoot + netemCommandLatencyAddendum.replace("***", str(params.delay))
		if params.packetloss > 0:
			netemCommandConfigTmp += netemCommandPacketLossAddendum.replace("***", str(params.packetloss))

		os.system(netemCommandDelete)
		os.system(netemCommandConfigTmp)
		return

	def getOutputFilename(testIndex, params):
		ret = str(params.protocol).lower()
		ret += "_" + str(params.packetloss)
		ret += "_" + str(params.delay)
		return ret

	def startTcpdump():
		global captureProcess
		os.system(pcapTouch)
		captureProcess = subprocess.Popen(
			tcpdumpCapture, stdout=devnull, stderr=devnull, shell=False)
		if args.vverbose:
			print("Capture started (" + str(captureProcess.pid) + ")")
		return

	def stopTcpdump(testIndex, params):
		os.system(tcpdumpCaptureKill + str(captureProcess.pid))		

		outputName = getOutputFilename(testIndex, params)

		os.system(tcpdumpAnalyze.replace("***", "./tcpDumpData/"+ str(outputName)))

		return

	while paramsQueue:
		params = paramsQueue.pop()
		netemConfig(params)

		currentTests = tests
		for i in xrange(currentTests):
			startTcpdump()
            os.system(quicClientCommand)
				
			stopTcpdump(i, params)

main()
