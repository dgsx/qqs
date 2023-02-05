stk=[]
top=-1
def isEmpty():
  global stk
  if stk==[]:
    print("Stack is Empty")
  else:
    None
def push():
  global stk
  global top
  n=int(input("Enter value to append:"))
  stk.append(n)
  top=len(stk)-1
  print("Value is Pushed into stack.")
  
def display():
  global stk
  global top
  if top==-1:
    isEmpty()
  else:
    top=len(stk)-1
    print("Top->",stk[top])
    for i in range(top-1,-1,-1):
      print(stk[i])
      
def Pop():
  global stk
  global top
  if top==-1:
    isEmpty()
  else:
    print("Elment Popped:",stk.pop())
    top=top-1
    
def peek():
  global stk
  global top
  top=len(stk)-1
  print("Peeked Element:",stk[top])
def menu():
  while True:
    print('''
          1. Push
          2. Pop
          3. Display
          4. Peek
          5. Exit
  ''')
    ch=int(input("Enter any number:"))
    if ch==1:
      push()
    elif ch==2:
      Pop()
    elif ch==3:
      display()
    elif ch==4:
      peek()
    elif ch==5:
      print("Bye Bye!")
      break
    else:
      print("Invalid choice")
    
menu()
