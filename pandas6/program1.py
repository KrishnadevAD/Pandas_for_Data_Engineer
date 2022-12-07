##practice about the  pandas 
import pandas as pd
 # taking the marks of the 3 subjects to find  series  and the percentage obtained 
student_english={1:90,2:85,3:96,4:80,5:88,6:76,7:99}
student_math={1:98,2:89,3:96,4:80,5:68,6:96,7:59}
student_science={1:97,2:95,3:96,4:90,5:88,6:86,7:49}
total1=pd.Series(student_english)
total2=pd.Series(student_math)
total3=pd.Series(student_science)
data=pd.DataFrame({'English':total1,'maths':total2,'Science':total3})
print(data)
print("*******************************************")
# converting into the percentage and adding with the particular series 
data['percentage']=(data["English"]+data["maths"]+data["Science"])*0.30
print(data)


