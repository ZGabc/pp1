def f(arr1,arr2):
    if len(arr1)==len(arr2):
        for i in range(len(arr1)):
            if arr1[i]==arr2[i]:
                pass
            else:
                print("we are not the same")
        print("we are not so diffrent after all")
    else:
        print("we are not the same")

f([5,3,1] , [5,3,1])