"""
2^31-1 = 2,147,483,647

e.g. 12,345,678
secList = [678, 345, 12]


"""

class Solution:
    def chTensDigitToWords(self, chTensDigit):
        
        if len(chTensDigit) != 2:
            return -1
        
        tenToNineteenMap = [ 'Ten', 'Eleven', 'Twelve', 'Thirteen', \
                            'Fourteen', 'Fifteen', 'Sixteen', \
                            'Seventeen', 'Eighteen', 'Nineteen' ]
        
        twentyToNinetyMap = [ 'Twenty', 'Thirty', 'Forty', 'Fifty', \
                            'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        if chTensDigit[0] == '1':
            return tenToNineteenMap[int(chTensDigit[1])]
        
        if chTensDigit[1] != '0':
            return twentyToNinetyMap[int(chTensDigit[0])-2] + ' ' + self.chDigitToWords(chTensDigit[1])
        else:
            return twentyToNinetyMap[int(chTensDigit[0])-2]
        
    
    def chDigitToWords(self, chDigit):
        if len(chDigit) != 1:
            return -1

        if chDigit == '0':
            return ''        

        oneToNineMap = ['One', 'Two', 'Three', 'Four', 'Five', \
                       'Six', 'Seven', 'Eight', 'Nine']
        
        return oneToNineMap[int(chDigit)-1]
        
    
    def threeDigitsNumToWords(self, num):
        
        """
        1. Convert num to string
        2. Pad '0' in front of numbers less than 3 digits
        """
        strNum = str(num)
        if len(strNum) <= 0:
            return -1

        words = ""

        while len(strNum) < 3:
            strNum = '0' + strNum

        # Deal with the hundreds' digit
        if strNum[0] != '0':
            words = self.chDigitToWords(strNum[0]) + " Hundred "
            if strNum[1] == '0' and strNum[2] == '0':
                # Trailing the last space
                words = words[:-1]
        # Deal with the tens' digit
        # If it is not 0, deal the tens and the unit digit in the same time
        if strNum[1] != '0':
            words += self.chTensDigitToWords(strNum[1:3])
        else:
            words += self.chDigitToWords(strNum[2])

        return words
        
    def numberToWords(self, num: int) -> str:
        
        if num < 0:
            return -1
        
        if num == 0:
            return 'Zero'
        
        words = ""
        secList = []
        quo = num
        while quo:
            quo, rem = divmod(quo, 1000)
            secList.append(rem)

        thousandToBillion = ['', 'Thousand', 'Million', 'Billion']
        
        # Reverse the list so that we can deal the number from the most significant
        # section, e.g. 'Billion'
        secList = secList[::-1]
        for sec, secNum in enumerate(secList):
            if secNum != 0:
                words = words + self.threeDigitsNumToWords(secNum) + " "
                # No need to add section name to the last section
                if len(secList)-sec > 1:
                    words = words + thousandToBillion[len(secList)-sec-1] + " "
            
        # Trailing the last white space
        words = words[:-1]
        return words
