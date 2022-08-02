"""wap ask user to provide his level and  pin distance and let them know which 
club they suppused to use.
1.first of all make the data in such a way that u can rekate the palyer
 level club and pin distance 
2.assign the user level with value like 0 for beginner, 1 for average and 2 for 
advance and make a dictonary named userdict
3.assign the club with tha value as 0 for driver,1 for 2 wood 2 for 3wood ,3 for 
4wood and 4 for 5wood andmake a dictonary namedclubdict.
4. now make a dictonary with level as key and and make another dictonary inside 
as a value, which will have range as a key and club s a value.and name it distdict.
5.ask user to input their level and change to integer value.assign the value to
variable userlevel
6.ask user to input their distance and change it to integer.assign the value 
to the variable user range.
7. now run the loop for key and value in distdict with userlevel as a index
8.use if condition 
   if userrange greater or equal to key[0] and userrange is lesser or equal to 
   key[1]
   then printthe value as  a key for clubdict,ie clubdict[value]
"""



userdict={0:"beginner",1:"average",2:"advanced"}
clubdict={0:"drive",1:"2 wood",2:"3 wood",3:"4 wood",4:"5 wood"}
distdict={
0:{
    (190,194):0,
    (180,189):1,
    (170,179):2,
    (165,169):3,
    (150,164):4
},
1:{
    (220,229):0,
    (215,219):1,
    (210,214):2,
    (205,209):3,
    (195,204):4
},
2:{
    (250,254):0,
    (235,249):1,
    (225,239):2,
    (215,229):3,
    (205,214):4
}
}
userlevel=int(input("please type 0 for beginner,1 for average and 2 for advanced level "))
userrange=int(input("please type the pin distance "))
for key,value in distdict[userlevel].items():
    if userrange>=key[0] and userrange<=key[1]:
        print("the club that you should be using is  ",clubdict[value])
        



 
