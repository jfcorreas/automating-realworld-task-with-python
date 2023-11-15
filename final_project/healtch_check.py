#!/usr/bin/env python

import psutil
import socket

def check_cpu(threshold):
  cpu_usage = psutil.cpu_percent(interval=1)
  return cpu_usage > threshold

def check_disk(threshold):
  disk_usage = psutil.disk_usage('/').percent
  return disk_usage > threshold

def check_memory(threshold):
  free_memory_mb = psutil.virtual_memory().available / 1024 / 1024
  return free_memory_mb < threshold

def check_hostname():
  try:
    localhost_ip = socket.gethostbyname('localhost')
    return localhost_ip == '127.0.0.1'
  except socket.error:
    return False

def main():

  if check_cpu(80):
    print('Error - CPU usage is over 80%')
  if check_disk(80):
    print('Error - Available disk space is less than 20%')
  if check_memory(500):
    print('Error - Available memory is less than 500MB')
  if not check_hostname():
    print('Error - localhost cannot be resolved to 127.0.0.1')

if __name__ == '__main__':
  main()