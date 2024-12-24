h = int(input()) 
m = int(input())
s = int(input())

#تبدیل ساعت به ثانبه 
h_convert = h * 60 * 60 
#تبدیل دقیقه به ثانیه
m_convert = m * 60 

result = h_convert + m_convert + s

print (result)