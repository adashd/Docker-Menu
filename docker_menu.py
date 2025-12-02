import os

print(
"""

----------------------------------

DOCKER MENU BASED PROGRAM

----------------------------------
1. List images
2. Launch new container
3. Stop the container
4. List containers
5. Start the container
6. Remove the container


"""
)

choice = input("Enter your choice :   ")

if choice == "1":
  os.system(f"sudo docker images")

elif choice == "2":
  name = input ("Enter name of container :  ")
  image = input ("Enter name of image :  ")
  os.system(f"sudo docker run -dit --name={name} {image} ")

elif choice == "3":
  name = input ("Enter name of container :  ")
  os.system(f"sudo docker stop {name} ")

elif choice == "4":
  os.system(f"sudo docker ps -a")

elif choice == "5":
  name = input ("Enter name of container :  ")
  os.system(f"sudo docker start {name} ")

elif choice == "6":
  name = input ("Enter name of container :  ")
  os.system(f"sudo docker rm {name} ")

