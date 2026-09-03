import sys
def total(a, b,c):
    return a+b+c
def avg(a,b,c):
    return a+b+c/3
def result1(a,b,c):
    if(a>=40 and b>=40 and c>=40):
        return "pass"
    else:
        return "Fail"            
if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3=  int(sys.argv[3])
    result = total(num1, num2,num3)
    result1=avg(num1,num2,num3)
    result2=result1(num1,num2,num3)
    print("=================================")
    print("Student details")
    print("=================================")
    print(f"sum          : {result}")
    print(f"avg        : {result1}")
    print(f"result        : {result2}")