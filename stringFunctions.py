class StringFunctions:
    #takes a string, returns a string of all lowercase charafcters
    #"WHOA" returns "whoa"
    def lowerCase(str):
        return str.lower()

    #takes a string, returns a a string without the . or , at the end
    #"whoa." returns "whoa"
    #"whoa" returns "whoa"
    def noDot(str):
        if str[-1]=='.' or str[-1]==',':
            return str[:-1]
        return str

    #takes a string and if there's no quotes, returns a string with quotes
    #"whoa" returns ""whoa""
    #""whoa"" returns ""whoa""
    def addQuotes(str):
        if str[0:1]!='"':
            str = '"' + str
        if str[-1]!='"':
            str = str + '"'
        return str

    #takes a string, returns the string in reverse
    #"whoa" returns "oahw"
    def reverse(str):
        reverse = ""
        for i in range(len(str)-1,-1,-1):
            reverse = reverse + str[i]
        return reverse

    #takes 2 strings, if they are the same then returns true, false otherwise
    #"okay" "okay" returns true, "okay" "okay." returns false
    def compareStrings(str1, str2):
        if len(str1) != len(str2):
            return False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True

    def makeString(arr):
        alphabet = "abcdefghijklmnopqrustuvwxyz"
        returnString = ""
        for index in arr:
            returnString = returnString + alphabet[index]
        return returnString
                
    
            
