class Solution:
    def romanToInt(self, s: str) -> int:
    	'''
    	Converts roman numeral to integer in accordance to 
    	the 'translation' dictionary.
    	
    	'I' can be placed before 'V' (5) and 'X' (10) to make 4 and 9. 
	'X' can be placed before 'L' (50) and 'C' (100) to make 40 and 90. 
	'C' can be placed before 'D' (500) and 'M' (1000) to make 400 and 900.
	
	Make use of the above supplementary information to replace occurances of 
	said strings with the equivalent (although wrong) format so as to calculate the sum fast.
    	
    	'''
        translation = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        s = s.replace('IV', 'IIII').replace('IX', 'VIIII') \
            .replace('XL', 'XXXX').replace('XC', 'LXXXX') \
            .replace('CD', 'CCCC').replace('CM', 'DCCCC')

        return sum(map(translation.get, s))
