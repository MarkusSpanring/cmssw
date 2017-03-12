#!/usr/bin/env python

import argparse
import glob
import os
import sys
import shutil
import subprocess

def readInput():
	parser = argparse.ArgumentParser(description="Perform the skimming for all samples in a folder")
	parser.add_argument("path",
	                    help="Input folder.")
	parser.add_argument("-c", "--config",
	                    default="$CMSSW_BASE/src/Validation/RecoTau/Tools/GetRecoTauVFromDQM_MC_cff.py",
	                    #default="$CMSSW_BASE/src/Validation/RecoTau/Tools/GetRecoTauVFromDQM_MC_cff_2.py",
	                    help="CMSSW configuration. [default: %(default)s]")
	parser.add_argument("-o", "--output-dir",
	                    default="$CMSSW_BASE/src/Validation/RecoTau/data/relval_plots",
	                    help="Output directory. [default: %(default)s]")

	args = parser.parse_args()
	args.config = os.path.expandvars(args.config)
	args.output_dir = os.path.expandvars(args.output_dir)
	
	return args


def main():
	args = readInput()

	input_list = glob.glob(os.path.join(args.path, "*.root"))
	campaign = args.path[args.path.rfind("CMSSW"):]

	for input_file in input_list:
		output_file = os.path.join(args.output_dir, campaign, os.path.basename(input_file))
		if not os.path.exists(os.path.dirname(output_file)):
			os.makedirs(os.path.dirname(output_file))

		postfix = ""
		if "ZTT" in input_file or "Zprime" in input_file:
			postfix = "ZTT"
		if "ZMM" in input_file:
			postfix = "ZMM"
		if "ZEE" in input_file:
			postfix = "ZEE"
		if "TTbar" in input_file or "QCD" in input_file:
			postfix = "QCD"

		exe = "python " + args.config + " " + input_file + " " + output_file + " " + postfix
		print exe
		p = subprocess.Popen(exe,
		stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin = subprocess.PIPE)
		(out, err) = p.communicate()
		print out
		print err


if __name__ == "__main__":
	main()
