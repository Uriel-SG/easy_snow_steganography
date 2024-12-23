import os
import subprocess
import time

def operation():  
    time.sleep(1.2)
    while True:
        time.sleep(1)
        print("\nChoose an option: ")
        time.sleep(0.1)
        print("\n1) Hide;")
        time.sleep(0.1)
        print("2) Retrieve;")
        time.sleep(0.1)
        print("3) Exit;\n")
        choice = input(">> ")
        if choice == "1":
            file1 = open("secret.txt", "w")
            file2 = open("infile.txt", "w")

            content1 = str(input("\nWrite the message you want to hide here:\n>> "))
            file1.write(content1)
            file1.close()

            content2 = str(input("\nWrite the message in which you want to hide your secret:\n>> "))
            file2.write(content2)
            file2.close()

            compression = input("\nDo you want to compress your secret text? (y/n) ")
            if compression == "y" or compression == "Y":
                subprocess.run(snow_name + " -C -f secret.txt infile.txt steg_output.txt", shell=True)
                print("\nDone! Saved as 'steg_output.txt' in your working directory.\n")
                os.remove("secret.txt")
                os.remove("infile.txt")
                input()
            else:
                subprocess.run(snow_name + " -f secret.txt infile.txt steg_output.txt", shell=True)
                print("\nDone! Saved as 'steg_output.txt' in your working directory,\n")
                os.remove("secret.txt")
                os.remove("infile.txt")
                input()
        elif choice == "2":
            input_file = input("Path to your text file: ")
            compressed = input("Is the secret message compressed? (y/n) ")
            if compressed == "y" or compressed == "Y":
                subprocess.run(snow_name + " -C " + input_file, shell=True)
                input()   
            else:
                subprocess.run("stegsnow " + input_file, shell=True)
                input()
        elif choice == "3":
            print("\n#############################################")
            print("\nBye bye!")
            time.sleep(0.7)
            print("\nSee you next time!")
            time.sleep(0.7)
            print("\n     Uriel-SG\n")
            print("#############################################\n")
            exit()

print('''\n############ Welcome to the ############

╔═╗┌─┐┌─┐┬ ┬   ╔═╗┌┐┌┌─┐┬ ┬   ╔═╗┌┬┐┌─┐┌─┐
║╣ ├─┤└─┐└┬┘───╚═╗││││ ││││───╚═╗ │ ├┤ │ ┬
╚═╝┴ ┴└─┘ ┴    ╚═╝┘└┘└─┘└┴┘   ╚═╝ ┴ └─┘└─┘

''')
time.sleep(1)

while True: 
    print("\nChoose your OS:\n>> ")
    time.sleep(0.8)
    print("\n1) Linux;\n2) macOS\n")
    chooseos = str(input())
    print("\nChecking dependencies...\n")
    if chooseos == "1":
        snow_name = "stegsnow"
        subprocess.run("sudo apt install stegsnow", shell=True)
        print("\n###################################################################")
        operation()
    elif chooseos == "2":
        snow_name = "snow"
        subprocess.run("brew install snow", shell=True)
        print("\n###################################################################")
        operation()
    else:
        print("Please, choose '1' or '2'!")



