int prefixCount(char** words, int wordsSize, char* pref) {
    int prefFoundCount = 0;
    int prefLen = strlen (pref);
    
    for (int i = 0; i < wordsSize; i++ ) {
        for (int j = 0; j < prefLen ; j++) {
            if (words[i][j] != pref[j]) {
                break;
            }
            
            if (j == prefLen-1) {
                prefFoundCount++;
                break;
            }
        }
    }
    
    return prefFoundCount;
    
}