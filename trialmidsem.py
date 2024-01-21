"""
    assert
    control structures
    range (start,end,increment)
    cmd args--
        import sys
        a = int(sys.argv[])
        b = int(sys.argv[])
        print(a+b)
    Strings: --
        are Immutable
        slicing   -- reverse: str[::-1]
        .upper(), .lower(), .capitalize(), .strip(), .lstrip()
        .rfind('s'), .index('s')  # find first occurrence of 's' in string
        membership functions.
        .rstrip() , .replace(), .split()-->returns in form of a list , .partition -> returns ina form of tuple 
        .split() --> divides by delimitter and .partition()-->divides in 2 parts by first occurence of the  delimitter.
        .swapcase(),. find() , .count(), .endswith() , .startswith() ,.title(), .isalpha, .isdigit() 
        .isalnum(), .isprintable(), .issapce() , .istitle() , .join(),  .encode() , .decode() 

        sep() -->print('1' , '2' , '3', sep=" ")
        end () --> by default print ends with new line hence end() appends the new stmt with the previous one in that same line.


        Mutable : List, Set , dictionary
        list [] --
                .append()
                .join("")
                'a' in list() --> returns boolean value
                len(list1)    --> returns length
                .sort()
                sorted(list)
                list.reverse()
                list.extend([4,5,6])
                .remove()
                .insert()
                input from user -- eval (input ( )) -- forms a list of all inputs
                list comprehension : list1 = [ for i in range (0,n) if i%2==0]
**import copy    .copy()--> nested objects ko copy nai kar pata hain
                .deepcopy() --> everything is copied from list1 to list2
                #example -->imp!
                                import copy
                                num1=[1,2,[3,4]]
                                num1_same=num1
                                num1_copy=copy.copy(num1)
                                num1_deepcopy=copy.deepcopy(num1)
                                num1[1]=20
                                num1[2][1]=40
                                print(num1)             [1, 20, [3, 40]]
                                print(num1_same)         [1, 20, [3, 40]]
                                print(num1_copy)         [1, 2, [3, 40]]
                                print(num1_deepcopy)     [1, 2, [3, 4]]
                                

        **      remove --> removes the first occurence of the key element given-->list.remove(3)
                del --> can delete single or multiple values at a time--> del[start:end:inc]
                pop--> return the deleted value and if key not given then removes the last element of the list.--> print(list.pop(3))- returns the deleted value.
                clear --> removes all elements from the list --> print--> None

        set{} -- setcomprehension is same as list comprehension, brackets changed
                -- order not maintained in a set
                .add()--> single elements adding
                .update()--> range of elements adding ex. v1={} v2 ={} v1.update(v2) -- v1 mein sara aa jayega
                type(set) -->set
                min(), max(), sum(), len(), in 
                .discard() -- remove single element
                .pop()
                .clear() --> returns empty set
                .union() --> union of 2 sets karta hain --> v3 = v1.union(v2)
                .intersection() --> v3= v1.intersection(v2) -- common elements
                .difference() --> v3 = v1.difference(v2) -->v1 se v2 ke elements hata denge.
                .issubset() --> check whether s1 is subset of s2 or not -->prints boolen value
                .intersection_update() -> common elements -->v1.intersection.update(v2)--> usi original set se bas remove karta hain  while intersection needs a new set
                .difference_update()--> voi original set mein difference ka kaam karega
                .symmetric_diffrence() -> not simmiliar to both the sets-->v3 = v1.symmetric_difference(v2)
                        ex a={1,2,3,4} b ={3,4,5,6} a-b ={1,2} and b-a ={5,6} v3={1,2,5,6} 
                issubset --> " we use here <= " v1<v2  -- true toh v1 is subset of v2
                issuperset -->" we use here >= " v1>v2 -- true toh v1 is super set of v2

        Immutable : Tuple (   ) --> non scalar data types 
        -- ordered collection of data items
        -- separated by commas
        single value ho toh trailing comma chahiye tabhi tuple hoga
        ie. t1 =(1,) --> print(type(t1))--> <class 'tuple'>
            t2=(1)   --> print(type(t2))--> <class 'int'>

        operations :
                1. multiplication t1*2 --> (1,1)
                2.concatenation t3 = t1 + "wed" -->(1,1,'wed')
                3.length -->len(t1)
                4. indexing --> t1[1]
                5.slicing --> [s:e:inc]
                6.min/max ()
                7. sum()
                8. in :

        Functions:
                1.Zip()--> map karga tuple1 ke ith elem ko tuple2 ke ith elem se and return that map!
                ex - c1 =(1,2,3,4)
                     c2 =(10,20,30,90)
                     c3 = tuple(zip(c1,c2))
                     print(c3)--> ((1,10),(2,20),(3,30),(4,90))
                2. .count()
                3. .index()

        Dictionary: is a unorderd sequenceof key pairs. seperated by commas with curly bracks
        1. Declaration --> Dict = {key1:value1, key2:value2 }
        min, max,  in:, sum only applies to the key
        
                
**      ERROR :
                1. type error 
                2. atrribute error --> jab immutable ko change karne ki koshish ho
                3. Indent error --> out of bound error
                







        Lambda function:

        Map, Reduce, Filter


        Re_ Module



"""
