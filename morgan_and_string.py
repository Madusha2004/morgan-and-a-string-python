
def morganAndString(a, b):


    a += chr(ord('z') + 1)
    b += chr(ord('z') + 1)



    i, j = 0, 0
    result = []



    while i < len(a) - 1 or j < len(b) - 1: 

        if a[i] < b[j]:

            result.append(a[i])

            i += 1

        elif b[j] < a[i]: 

            result.append(b[j])

            j += 1

        else: 

            if a[i:] < b[j:]:

                result.append(a[i])

                i += 1

            else:

                result.append(b[j])

                j += 1
        

    return ''.join(result)



if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')



    t = int(input().strip())



    for t_itr in range(t):

        a = input().strip()

        b = input().strip()



        result = morganAndString(a, b)



        fptr.write(result + '\n')



    fptr.close()