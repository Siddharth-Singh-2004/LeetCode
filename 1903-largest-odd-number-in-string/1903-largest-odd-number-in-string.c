char* largestOddNumber(char* num) {
    int len = strlen (num);
    int oddDigFnd = false;
    /* number is odd, just spitout else cut out even digits from the end */
    if (num[len-1]%2 == 0) {
      /* Now track largest odd from the end */
        for (int i=len - 1; i >= 0 ; i--) {
            if (num[i] % 2 != 0)  {
                oddDigFnd = true;
                num[i+1] = '\0';
                break;
            }
        }
    }
    else
    {
        oddDigFnd = true;
    }

    printf ("%s\n", num);   
    if (oddDigFnd)
       return (num);
    else
        return ("");
    
}