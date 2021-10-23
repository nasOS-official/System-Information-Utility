'''


    nasOS, hereby disclaims all copyright interest in the program “System Information Utility” written by  nasOS-official and Electro661.

    signature of nasOS-official 23 October 2021
    nasOS-official, President of nasOS

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''
import re
import os
what = input("""What information do you want to know?
1)All 2)Processor information 3)System information """)
file = open("/proc/cpuinfo" , "r")
os.system("clear")
print("GNU SYSTEM INFORMATION UTILITY")
flag = ["processor", "model name", "flags", "cpu MHz", "cache size", "physical id", "core id,"]

def new_list():
    os.system("clear")
    print("GNU SYSTEM INFORMATION UTILITY")


os.system("clear")
if what == '1':
    new_list()
    
    os.system('last')
    input("Press Enter to go to the next page.")
    new_list()
    os.system('neofetch')
    input("Press Enter to go to the next page.")
    new_list()
    os.system('uname -a')
    input("Press Enter to go to the next page.")
    new_list()
    for line in file:
        for x in range(0, 7):

            if re.search(flag[x], line):

                print(line)



if what == '2':
    new_list()
    for line in file:
        for x in range(0, 7):

            if re.search(flag[x], line):

                print(line)
if what == '3':

    new_list()
    os.system('neofetch')
    input("Press Enter to go to the next page.")
    new_list()
    os.system('last')


file.close()