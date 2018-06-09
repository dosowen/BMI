height = (float (input ('請輸入身高 (公分):')))/ 100
weight = float (input('請輸入體重 (公斤):'))
BMI = (weight/(height*height))
if BMI < 18:
	print ('BMI=',BMI,'過輕')
elif 18 <= BMI < 24:
	print ('BMI=',BMI,'正常')
else :
	print ('BMI=',BMI,'過重')