import sys
def total(a, b,c):
    return a+b+c
def avg(a,b,c):
    return a+b+c/3
def result(a,b,c):
    if(a>=40 and b>=40 and c>=40):
        return "pass"
    else:
        return "Fail"            
if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3=  int(sys.argv[3])
    result1= total(num1, num2,num3)
    result2=avg(num1,num2,num3)
    result3=result(num1,num2,num3)
    print("=================================")
    print("Student details")
    print("=================================")
    print(f"sum          : {result1}")
    print(f"avg        : {result2}")
    print(f"result        : {result3}")