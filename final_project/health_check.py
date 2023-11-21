#!/usr/bin/env python3

import os
import psutil
import socket
import emails

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
  subject = False
  if check_cpu(80):
    subject = "Error - CPU usage is over 80%"
  if check_disk(80):
    subject = "Error - Available disk space is less than 20%"
  if check_memory(500):
    subject = "Error - Available memory is less than 500MB"
  if not check_hostname():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"

  if subject:
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body, False)
    emails.send_email(message)

if __name__ == '__main__':
  main()