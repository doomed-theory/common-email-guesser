#! /usr/bin/python
##Common Email Guesser -- guesses a person's email address
##Copyright (C) 2014  Doomed Theory
##
##This program is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License
##along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os, sys
import os.path
print('''
Common Email Guesser  Copyright (C) 2014  Doomed Theory
This program comes with ABSOLUTELY NO WARRANTY; .
This is free software, and you are welcome to redistribute it
under certain conditions. see http://www.gnu.org/copyleft/gpl.html for details.
''')
fname=input("enter first name: ") #first name
mname=input("enter middle name: ") #middle name
sname=input("enter last name: ") #last name
comp=input("enter company: ") #company
punc0="." # a period
punc1="_" # an underscore
punc2="-" #a hyphen
punc3=punc0
punc4="?"
addr=input("please enter the street address: ") # first three letters of street address
yale=input("please enter year of birth: ")
#*** full email addresses with domain names are not currently supported. This is a protype for later. ***#
##prefix="mail." 
##tld1=".com"
##tld2=".org"
##tld3=".net"
##tld4=".biz"
##dom0="gmail"+tld1
##dom1="yahoo"+tld1
##dom2="hotmail"+tld1
##dom3="icloud"+tld1
##dom4="outlook"+tld1
##dom5=comp+tld1
##dom6=comp+tld2
##dom7=comp+tld3
##dom8=comp+tld4
##dom9="aol"+tld1
##dom10=prefix+comp+tld1
##dom11=prefix+comp+tld2
##dom12=prefix+comp+tld3
##dom13=prefix+comp+tld4

if os.path.isfile("./emaillist.txt"):
    delyn=input("file already exists. Would you like to delete the file? type y or n: ")
    while True:
        if delyn.startswith('y'):
            os.remove("./emaillist.txt")
            break
        elif dely.startswith('Y'):
            os.remove("./emaillist.txt")
            break
        elif delyn.startswith('n'):
            sys.exit(0)
        elif delyn.startswith('N'):
            sys.exit(0)
        else:
            print("please enter y or n")
            continue
file=open("./emaillist.txt", 'w')
file.close()
o=open("./emaillist.txt", 'a')
o.write("# generated by common email generator")
o.write(fname+"\n")
o.write(sname+"\n")
o.write(mname+"\n")
o.write(comp+"\n")
o.write(fname+yale+"\n")
o.write(lname+yale+"\n")
o.write(fname+punc0+lname+yale+"\n")
o.write(fname+punc4+"\n")
o.write(sname+punc4+"\n")
o.write(fname+sname+"\n")
o.write(fname+comp+"\n")
o.write(mname+comp+"\n")
o.write(sname+comp+"\n")
o.write(fname+addr+"\n")
o.write(mname+addr+"\n")
o.write(sname+addr+"\n")
o.write(fname+punc0+sname+"\n")
o.write(fname+punc1+sname+"\n")
o.write(fname+punc0+sname+punc4+"\n")
o.write(fname+punc2+sname+"\n")
o.write(fname+mname+sname+"\n")
o.write(fname+punc0+mname+sname+"\n")
o.write(fname+punc1+mname+sname+"\n")
o.write(fname+punc2+mname+sname+"\n")
o.write(fname+mname+punc0+sname+"\n")
o.write(fname+mname+punc1+sname+"\n")
o.write(fname+mname+punc2+sname+"\n")
o.write(fname+punc0+mname+punc0+sname+"\n")
o.write(fname+punc1+mname+punc1+sname+"\n")
o.write(fname+punc2+mname+punc2+sname+"\n")
o.write(fname+sname+comp+"\n")
o.write(fname+punc0+sname+comp+"\n")
o.write(fname+punc1+sname+comp+"\n")
o.write(fname+punc2+sname+comp+"\n")
o.write(fname+mname+sname+comp+"\n")
o.write(fname+punc0+mname+sname+comp+"\n")
o.write(fname+punc1+mname+sname+comp+"\n")
o.write(fname+punc2+mname+sname+comp+"\n")
o.write(fname+mname+punc0+sname+comp+"\n")
o.write(fname+mname+punc1+sname+comp+"\n")
o.write(fname+mname+punc2+sname+comp+"\n")
o.write(fname+punc0+mname+punc0+sname+comp+"\n")
o.write(fname+punc1+mname+punc1+sname+comp+"\n")
o.write(fname+punc2+mname+punc2+sname+comp+"\n")
o.write(fname+sname+addr+"\n")
o.write(fname+punc0+sname+addr+"\n")
o.write(fname+punc1+sname+addr+"\n")
o.write(fname+punc2+sname+addr+"\n")
o.write(fname+mname+sname+addr+"\n")
o.write(fname+punc0+mname+sname+addr+"\n")
o.write(fname+punc1+mname+sname+addr+"\n")
o.write(fname+punc2+mname+sname+addr+"\n")
o.write(fname+mname+punc0+sname+addr+"\n")
o.write(fname+mname+punc1+sname+addr+"\n")
o.write(fname+mname+punc2+sname+addr+"\n")
o.write(fname+punc0+mname+punc0+sname+addr+"\n")
o.write(fname+punc1+mname+punc1+sname+addr+"\n")
o.write(fname+punc2+mname+punc2+sname+addr+"\n")
o.write(fname+sname+comp+addr+"\n")
o.write(fname+punc0+sname+comp+addr+"\n")
o.write(fname+punc1+sname+comp+addr+"\n")
o.write(fname+punc2+sname+comp+addr+"\n")
o.write(fname+mname+sname+comp+addr+"\n")
o.write(fname+punc0+mname+sname+comp+addr+"\n")
o.write(fname+punc1+mname+sname+comp+addr+"\n")
o.write(fname+punc2+mname+sname+comp+addr+"\n")
o.write(fname+mname+punc0+sname+comp+addr+"\n")
o.write(fname+mname+punc1+sname+comp+addr+"\n")
o.write(fname+mname+punc2+sname+comp+addr+"\n")
o.write(fname+punc0+mname+punc0+sname+comp+addr+"\n")
o.write(fname+punc1+mname+punc1+sname+comp+addr+"\n")
o.write(fname+punc2+mname+punc2+sname+comp+addr+"\n")
o.write(fname+"x"+sname+"\n")
o.write(fname+punc0+"x"+sname+"\n")
o.write(fname+punc1+"x"+sname+"\n")
o.write(fname+punc2+"x"+sname+"\n")
o.write(fname+"x"+punc0+sname+"\n")
o.write(fname+"x"+punc1+sname+"\n")
o.write(fname+"x"+punc2+sname+"\n")
o.write(fname+punc0+"x"+punc0+sname+"\n")
o.write(fname+punc1+"x"+punc1+sname+"\n")
o.write(fname+punc2+"x"+punc2+sname+"\n")
o.write(fname+"x"+sname+comp+"\n")
o.write(fname+punc0+"x"+sname+comp+"\n")
o.write(fname+punc1+"x"+sname+comp+"\n")
o.write(fname+punc2+"x"+sname+comp+"\n")
o.write(fname+"x"+punc0+sname+comp+"\n")
o.write(fname+"x"+punc1+sname+comp+"\n")
o.write(fname+"x"+punc2+sname+comp+"\n")
o.write(fname+punc0+"x"+punc0+sname+comp+"\n")
o.write(fname+punc1+"x"+punc1+sname+comp+"\n")
o.write(fname+punc2+"x"+punc2+sname+comp+"\n")
o.write(fname+"x"+sname+addr+"\n")
o.write(fname+punc0+"x"+sname+addr+"\n")
o.write(fname+punc1+"x"+sname+addr+"\n")
o.write(fname+punc2+"x"+sname+addr+"\n")
o.write(fname+"x"+punc0+sname+addr+"\n")
o.write(fname+"x"+punc1+sname+addr+"\n")
o.write(fname+"x"+punc2+sname+addr+"\n")
o.write(fname+"x"+sname+comp+addr+"\n")
o.write(fname+punc0+"x"+sname+comp+addr+"\n")
o.write(fname+punc1+"x"+sname+comp+addr+"\n")
o.write(fname+punc2+"x"+sname+comp+addr+"\n")
o.write(fname+"x"+punc0+sname+comp+addr+"\n")
o.write(fname+"x"+punc1+sname+comp+addr+"\n")
o.write(fname+"x"+punc2+sname+comp+addr+"\n")
o.write(fname+punc0+"x"+punc0+sname+comp+addr+"\n")
o.write(fname+punc1+"x"+punc1+sname+comp+addr+"\n")
o.write(fname+punc2+"x"+punc2+sname+comp+addr+"\n")
o.write(fname+"xx"+sname+"\n")
o.write(fname+punc0+"xx"+sname+"\n")
o.write(fname+punc1+"xx"+sname+"\n")
o.write(fname+punc2+"xx"+sname+"\n")
o.write(fname+"xx"+punc0+sname+"\n")
o.write(fname+"xx"+punc1+sname+"\n")
o.write(fname+"xx"+punc2+sname+"\n")
o.write(fname+punc0+"xx"+punc0+sname+"\n")
o.write(fname+punc1+"xx"+punc1+sname+"\n")
o.write(fname+punc2+"xx"+punc2+sname+"\n")
o.write(fname+"xx"+sname+comp+"\n")
o.write(fname+punc0+"xx"+sname+comp+"\n")
o.write(fname+punc1+"xx"+sname+comp+"\n")
o.write(fname+punc2+"xx"+sname+comp+"\n")
o.write(fname+"xx"+punc0+sname+comp+"\n")
o.write(fname+"xx"+punc1+sname+comp+"\n")
o.write(fname+"xx"+punc2+sname+comp+"\n")
o.write(fname+punc0+"xx"+punc0+sname+comp+"\n")
o.write(fname+punc1+"xx"+punc1+sname+comp+"\n")
o.write(fname+punc2+"xx"+punc2+sname+comp+"\n")
o.write(fname+"xx"+sname+addr+"\n")
o.write(fname+punc0+"xx"+sname+addr+"\n")
o.write(fname+punc1+"xx"+sname+addr+"\n")
o.write(fname+punc2+"xx"+sname+addr+"\n")
o.write(fname+"xx"+punc0+sname+addr+"\n")
o.write(fname+"xx"+punc1+sname+addr+"\n")
o.write(fname+"xx"+punc2+sname+addr+"\n")
o.write(fname+"xx"+sname+comp+addr+"\n")
o.write(fname+punc0+"xx"+sname+comp+addr+"\n")
o.write(fname+punc1+"xx"+sname+comp+addr+"\n")
o.write(fname+punc2+"xx"+sname+comp+addr+"\n")
o.write(fname+"xx"+punc0+sname+comp+addr+"\n")
o.write(fname+"xx"+punc1+sname+comp+addr+"\n")
o.write(fname+"xx"+punc2+sname+comp+addr+"\n")
o.write(fname+punc0+"xx"+punc0+sname+comp+addr+"\n")
o.write(fname+punc1+"xx"+punc1+sname+comp+addr+"\n")
o.write(fname+punc2+"xx"+punc2+sname+comp+addr+"\n")

lfname=list(fname)
lmname=list(mname)
lsname=list(sname)
lcomp=list(comp)
lpunc0=list(punc0)
lpunc1=list(punc1)
lpunc2=list(punc2)
laddr=list(addr)

case1=lfname[0]+lmname[0]+lsname[0]
o.write(case1+"\n")
case1=lfname[0]+lmname[0]+lsname[0]+addr
o.write(case1+"\n")
case1=fname+lsname[0]
o.write(case1+"\n")
case1=fname+lmname[0]+lsname[0]
o.write(case1+"\n")
adds1=lfname[0]+lmname[0]+sname
o.write(adds1+"\n")
adds1=lfname[0]+lmname[0]+punc0+sname
o.write(adds1+"\n")
adds1=lfname[0]+lmname[0]+punc1+sname
o.write(adds1+"\n")
adds1=lfname[0]+lmname[0]+punc2+sname
o.write(adds1+"\n")
adds1=fname+lsname[0]
o.write(adds1+"\n")
adds1=fname+punc0+lsname[0]
o.write(adds1+"\n")
adds1=fname+punc1+lsname[0]
o.write(adds1+"\n")
adds1=fname+punc2+lsname[0]
o.write(adds1+"\n")
case1=fname+lmname[0]+sname
o.write(case1+"\n")
case1=fname+punc0+lmname[0]+sname
o.write(case1+"\n")
case1=fname+punc1+lmname[0]+sname
o.write(case1+"\n")
case1=fname+punc2+lmname[0]+sname
o.write(case1+"\n")
case1=fname+lmname[0]+punc0+sname
o.write(case1+"\n")
case1=fname+lmname[0]+punc1+sname
o.write(case1+"\n")
case1=fname+lmname[0]+punc2+sname
o.write(case1+"\n")
case1=fname+lmname[0]+punc0+sname
o.write(case1+"\n")
case1=fname+lmname[0]+punc1+sname
o.write(case1+"\n")
case1=fname+lmname[0]+punc2+sname
o.write(case1+"\n")
case1=fname+punc0+lmname[0]+punc0+sname
o.write(case1+"\n")
case1=fname+punc1+lmname[0]+punc1+sname
o.write(case1+"\n")
case1=fname+punc2+lmname[0]+punc2+sname
o.write(case1+"\n")
case1=fname+lmname[0]+sname
o.write(case1+"\n")
case1=fname+punc0+lmname[0]+sname+comp
o.write(case1+"\n")
case1=fname+punc1+lmname[0]+sname+comp
o.write(case1+"\n")
case1=fname+punc2+lmname[0]+sname+comp
o.write(case1+"\n")
case1=fname+lmname[0]+punc0+sname+comp
o.write(case1+"\n")
case1=fname+lmname[0]+punc1+sname+comp
o.write(case1+"\n")
case1=fname+lmname[0]+punc2+sname+comp
o.write(case1+"\n")
case1=fname+lmname[0]+punc0+sname+comp
o.write(case1+"\n")
case1=fname+lmname[0]+punc1+sname+comp
o.write(case1+"\n")
case1=fname+lmname[0]+punc2+sname+comp
o.write(case1+"\n")
case1=fname+punc0+lmname[0]+punc0+sname+comp
o.write(case1+"\n")
case1=fname+punc1+lmname[0]+punc1+sname+comp
o.write(case1+"\n")
case1=fname+punc2+lmname[0]+punc2+sname+comp
o.write(case1+"\n")
case2=lfname[0]+sname
o.write(case2+"\n")
case2=lfname[0]+sname+comp
o.write(case2+"\n")
case2=lfname[0]+sname+addr
o.write(case2+"\n")
case2=lfname[0]+punc0+sname
o.write(case2+"\n")
case2=lfname[0]+punc1+sname
o.write(case2+"\n")
case2=lfname[0]+punc2+sname
o.write(case2+"\n")
case2=lfname[0]+punc0+sname+comp
o.write(case2+"\n")
case2=lfname[0]+punc0+sname+addr
o.write(case2+"\n")
case2=lfname[0]+punc1+sname+comp
o.write(case2+"\n")
case2=lfname[0]+punc2+sname+addr
o.write(case2+"\n")
case2=lfname[0]+punc0+sname+punc0+comp
o.write(case2+"\n")
case2=lfname[0]+punc1+sname+punc1+comp
o.write(case2+"\n")
case2=lfname[0]+punc2+sname+punc2+comp
o.write(case2+"\n")
case2=lfname[0]+punc0+sname+punc0+addr
o.write(case2+"\n")
case2=lfname[0]+punc1+sname+punc1+addr
o.write(case2+"\n")
case2=lfname[0]+punc2+sname+punc2+addr
o.write(case2+"\n")
case2=lfname[0]+sname+punc0+comp
o.write(case2+"\n")
case2=lfname[0]+sname+punc1+addr
o.write(case2+"\n")
case2=lfname[0]+sname+punc2+addr
o.write(case2+"\n")


o.close()
