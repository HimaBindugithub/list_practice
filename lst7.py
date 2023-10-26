def displaying_items():
    print("========================")
    print("Accessing the list by using For Loop")
    print("========================")
    global stationaryItems
    stationaryItems = ["Pencils", "Papers", "Ball Pens", "Erasers", "Glue Sticks", "Exam Pads"]
    z=0
    for idx in stationaryItems:
        print("In stationaryItems Index",z,":",idx, end = "\n")
        z=z+1
    print(" ")
    print("========================")
    print("Accessing the list by using While Loop")
    print("========================")
    j=0
    while j<len(stationaryItems):
       print("In stationaryItems Index",z,":",idx, end = "\n")
       j=j+1

def access_list():
    print("========================")
    print("Accessing the list by using Indexing")
    print("========================")
    print("In stationaryItems Index0:",stationaryItems[0], end = "\n")
    print("In stationaryItems Index1:",stationaryItems[1],end="\n")
    print("In stationaryItems Index2:",stationaryItems[2],end="\n")
    print("In stationaryItems Index3:",stationaryItems[3],end="\n")
    print("In stationaryItems Index4:",stationaryItems[4],end="\n")
    print("In stationaryItems Index5:",stationaryItems[5],end="\n")

def main():
    #call the create_list()
   displaying_items()
   access_list()


if __name__ == "__main__":
    main()
