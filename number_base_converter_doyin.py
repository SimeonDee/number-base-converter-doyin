####################################################
# Description: Number Base Converter Module
# Author:      Adeyemi Adedoyin Simeon
# Date:        February 3rd, 2019
# Version:     1.0
# Location:    Ibadan, AAH PG Hall, UI
#####################################################
# coding: utf-8

# # Number bases converter

# ### Decimal to other number bases converter function

# In[10]:


def dec_to_other_bases_conv(decimal,base):
    """
    decimal: The decimal number to convert
    base: Number equivalent to the base to convert to
    
    """
    d = decimal
    ans = ""
    while(decimal > 0):
        rem = decimal % base
        #print("{} : {}".format(quotient,rem))
        #ans.insert(0,rem)
        ans = str(rem) + ans
        decimal = decimal // base
    print("\n" + str(d) + " in decimal is equal to " + ans + " in base " + str(base))
    return ans


# ### Function to convert from other number bases to Decimal

# In[11]:


def other_base_to_dec_conv(number,numBase):
    """
    number: The number to convert
    base: Integer Number equivalent to the base of the number entered
    
    """
    decimal = 0
    strNum = str(number)
    position = len(strNum) - 1
    print("")
    header = "{} \t|\t {} \t\t|\t {} \t|\t {} \t|\t{}".format("index","Digit","position","Weight = (base ^ pos)","Sum Weight")
    print(header)
    print("-" * int(1.7 * len(header)))
    for i in range(0,len(strNum)):
        decimal = decimal + (int(strNum[i])* numBase**position)
        print("{} \t|\t {} \t\t|\t {} \t\t|\t {} \t\t\t|\t {}".format(i,strNum[i],position,numBase**position,decimal))
        position -= 1
    print("\n{} in base {} is equal to {} in decimal".format(number,numBase,decimal))
    return decimal


# ### Function to convert from other number base to other number base

# In[13]:


def other_base_to_other_base_conv(number,fromBase,toBase):
    """
    number: The number to convert
    fromBase: Integer Number equivalent to the base of the number entered
    toBase: Integer Number equivalent to the base you want to convert to
    
    """

    decimalEqv = other_base_to_dec_conv(number,fromBase)
    finalAnswer = dec_to_other_bases_conv(decimalEqv,toBase)
    print("\nSolution:")
    print("{} in base {} is equal to {} in base {}".format(number,fromBase,finalAnswer,toBase))
    return finalAnswer

