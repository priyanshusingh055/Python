def demo():
  try:
    a = int(input("Enter A Number:"))
    print(a)
    return

  except Exception as e:
    print(e) 
    return


  finally:
    print("I am inside finally")       

demo()    