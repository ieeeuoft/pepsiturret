# punch the following stuff into a terminal when you launch your edge impulse script:
# 1. make a FIFO (pipe) using ```mkfifo pepsipipe```
# 2. run the edge impulse script, but redirect the output to the pipe: ```{command to start edge impulse script goes here} > pepsipipe```
# 3. make sure this script is in the same directory as where your edge impulse script is

import os
import serial

fifo_path = "pepsipipe" # path to the pipe

def port_init():
  # initializes the port to the arduino, returns connection object
  try:
    conn = serial.Serial('{COM PORT HERE}', 9600, timeout=30)
  except serial.SerialException:
    print('Cannot initialize serial communication.')
    print('Is the device plugged in? \r\nIs the correct COM port chosen?')
  return conn

def process(data):
  # TODO: process the data from the edge impulse script
  # take the data, process it, and come up with a sequence of U, D, L, R, or S depending on what to do
  # do some processing here
  return 

def main():
  # Check if the FIFO pipe exists
  if not os.path.exists(fifo_path):
      print(f"FIFO pipe '{fifo_path}' does not exist.")
      exit(1)

  try:
      conn = port_init()
      with open(fifo_path, 'r') as fifo:
          while True: # will keep reading until no more data
              data = fifo.readline()
              to_arduino = process(data)
              conn.write(to_arduino.encode()) # writes processed stuff to the arduino
              if not data:
                  break
              print(f"Received: {data}", end="")
  except KeyboardInterrupt:
      print("Reading from FIFO pipe stopped.")
  except Exception as e:
      print(f"An error occurred: {e}")
