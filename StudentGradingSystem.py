def total_std():
  totalStd=int(input("enter total students:"))
  return totalStd
Total= total_std()
marks_dict={}
let=[]
def std_list():
  for i in range(Total):
    print("enter student details")
    name=input(f"enter name {i+1}: ").strip().title()
    marks=[]
    for i in range(5):
      new=int(input("enter marks out of 10:"))
      marks.append(new)
      avg=sum(marks)/len(marks)
    if avg>=9:
      grade="A+"
    elif avg>=7:
      grade="A"
    elif avg>=5:
      grade="B"
    else:
      grade="C"
    let.append(name)
    let.append(avg)
    let.append(grade)
  print(let)
  
  
    
std_list()

  




