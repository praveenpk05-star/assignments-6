from pip._vendor.distlib.compat import raw_input

ans=True
while ans:
    print ("""
    1.Add task
    2.view all tasks
    0.Exit/Quit
    ===============
    """)
    ans=raw_input("choose option : ")
    if ans=="1":
        with open("file.txt", "a+") as file_object:
            text = str(input('enter the task:'))
            file_object.write(text)
            print('task added')
    elif ans=="2":
        f = open("file.txt", 'r', encoding='utf-8')
        print(f.read())

    elif ans=="0":
      print("\n Goodbye")
      ans = 0