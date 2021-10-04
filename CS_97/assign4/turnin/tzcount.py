#!/usr/bin/python
# lets the computer know to run this as a python script

#importing libraries
import sys
import string
import array

#main function
def main():
   input = [] #initialize an array called input

   #put all the lines of file into input
   for line in sys.stdin:
      input.append(line.rstrip()) #rstrip() gets rid of newline chars

   #at this point we have put all file into input
   #next step is to only keep the lines with time zones

   #list of for the lines with timezones
   tz = []
   #go through input and get the timezones
   for line in input: #everything is in input currently
      if ('Date:' in line):
         temp = line.split() #split the string
         #temp[6] is the value of the timezones
         tz.append(temp[6]) #append to a list

   #now tz has the collection of time zones
   #want to go through and sort amount of times each time zone pops up

   # make variables for each time zone
   utc0 = []  #utc -1100
   utc1 = []
   utc2 = []
   utc3 = []
   utc4 = []
   utc4 = []
   utc5 = []
   utc6 = []
   utc7 = []
   utc8 = []
   utc9 = []
   utc10 = []
   utc11 = [] #utc 0000
   utc12 = []
   utc13 = []
   utc14 = []
   utc15 = []
   utc16 = []
   utc17 = []
   utc18 = []
   utc19 = []
   utc20 = []
   utc21 = []
   utc22 = []
   utc23 = [] #utc +1200

   a = 1
   for time in tz:
      if (time == '-1100'):
         utc0.append(time)
      elif (time == '-1000'):
         utc1.append(time)
      elif (time == '-0900'):
         utc2.append(time)
      elif (time == '-0800'):
         utc3.append(time)
      elif (time == '-0700'):
         utc4.append(time)
      elif (time == '-0600'):
         utc5.append(time)
      elif (time == '-0500'):
         utc6.append(time)
      elif (time == '-0400'):
         utc7.append(time)
      elif (time == '-0300'):
         utc8.append(time)
      elif (time == '-0200'):
         utc9.append(time)
      elif (time == '-0100'):
         utc10.append(time)
      elif (time == '0000'):
         utc11.append(time)
      elif (time == '+0100'):
         utc12.append(time)
      elif (time == '+0200'):
         utc13.append(time)
      elif (time == '+0300'):
         utc14.append(time)
      elif (time == '+0400'):
         utc15.append(time)
      elif (time == '+0500'):
         utc16.append(time)
      elif (time == '+0600'):
         utc17.append(time)
      elif (time == '+0700'):
         utc18.append(time)
      elif (time == '+0800'):
         utc19.append(time)
      elif (time == '+0900'):
         utc20.append(time)
      elif (time == '+1000'):
         utc21.append(time)
      elif (time == '+1100'):
         utc22.append(time)
      elif (time == '+1200'):
         utc23.append(time)
         

   #printing the time zones and amounts
   print('-1100,' , len(utc0))
   print('-1000,' , len(utc1))
   print('-0900,' , len(utc2))
   print('-0800,' , len(utc3))
   print('-0700,' , len(utc4))
   print('-0600,' , len(utc5))
   print('-0500,' , len(utc6))
   print('-0400,' , len(utc7))
   print('-0300,' , len(utc8))
   print('-0200,' , len(utc9))
   print('-0100,' , len(utc10))
   print(' 0000,' , len(utc11))
   print('+0100,' , len(utc12))
   print('+0200,' , len(utc13))
   print('+0300,' , len(utc14))
   print('+0400,' , len(utc15))
   print('+0500,' , len(utc16))
   print('+0600,' , len(utc17))
   print('+0700,' , len(utc18))
   print('+0800,' , len(utc19))
   print('+0900,' , len(utc20))
   print('+1000,' , len(utc21))
   print('+1100,' , len(utc22))
   print('+1200,' , len(utc23))








#calling to main function
if __name__ == "__main__":
   main()
