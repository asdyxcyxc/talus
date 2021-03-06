#!/usr/bin/env python
# encoding: utf-8

import sys
import argparse

import slave

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('amqp_host', type=str, help="Address of AMQP host")
	parser.add_argument('max_vms', type=int, help="Maximum number of VMs to run concurrently")
	parser.add_argument('intf', type=str, help="Network interface")
	parser.add_argument('--plugins', type=str, help="Path to plugins directory")
	
	args = parser.parse_args()
	
	#if len(sys.argv) < 4:
	#	sys.stderr.write("USAGE: {} <AMQP_HOST> <MAX_VMS> <INTF>\n")
	#	exit(1)

	#slave.main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
	slave.main(args.amqp_host, args.max_vms, args.intf, args.plugins)
