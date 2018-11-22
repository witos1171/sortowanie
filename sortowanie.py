
def BubleSort(list):
    print(list)
    for x in range(len(list),0,-1):
        for y in range(x,len(list)-1):
            if list[y]>list[y+1]:
                list[y],list[y+1]=list[y+1],list[y]
    print(list)
def main():
    dane=input("Podaj dane do sortowania")
    dane=dane.split()
    dane=[int(x) for x in dane]
    BubleSort(dane)
main()