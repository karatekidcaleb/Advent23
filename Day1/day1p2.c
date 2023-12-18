#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 255

char * checkForPhrase(char * line);

int main(int argc, char ** argv)
{
	FILE *filePtr;
	char * fileName = argv[1];
	printf("%s", fileName);
	char numArr[1001][MAX_LENGTH];
	int numArrClean[1001][2];
	
	filePtr = fopen(fileName, "r");

	if(filePtr==NULL)
	{
		printf("file not found");
		return (-1);
	}
	
	int counter = 0;
	int sum = 0;
	while(fgets(numArr[counter], MAX_LENGTH, filePtr))
	{
		//make string workable
		numArr[counter][strlen(numArr[counter]) - 1] = '\0';
		//clean up written digits into real digits
		checkForPhrase(numArr[counter]);
		//find first int
		for(int i=0; i<strlen(numArr[counter]); i++)
		{
			int charAtCount = (int)numArr[counter][i] - (int)'0';
			if (charAtCount >=0 && charAtCount <=9)
			{
				numArrClean[counter][0] = charAtCount;
				break;
			}
		}
		//find last int
		for(int i=strlen(numArr[counter]); i>=0 ; i--)
		{
			int charAtCount = (int)numArr[counter][i] - (int)'0'; //ascii '5' turns into int 5
			if (charAtCount >=0 && charAtCount <=9)
			{
				numArrClean[counter][1] = charAtCount;
				break;
			}
		}
		sum += (numArrClean[counter][0] *10) + numArrClean[counter][1];
		printf("\n%d and %d, total: %d\n", numArrClean[counter][0],  numArrClean[counter][1], sum);
		counter++;
	}
}

char * checkForPhrase(char * line)
{
	char numStrings[9][6] = 
	{"one", "two", "three", "four",
	"five", "six", "seven", "eight",
	"nine"};
	
	for(int i=0; i<9; i++) //for every possible spelled out digit...
	{
		if(strstr(line, numStrings[i]) != NULL) //if the input string actually contains any spelled out digits...
		{
			char charAtCount;
			for(int j=0; j<strlen(line); j++) //starting at the first character in the input string...
			{
				charAtCount = line[j];
				if (charAtCount >= 'a') //if the character is alphabetical...
				{
					if(charAtCount = numStrings[i][0]) { //and matches the first character in the spelled
													  //out digit which we're investigating (i.e. the 
													  //value of i corresponds to "three" and the character
													  //in given string matches 't')...
						short match = 1;
						//start going through each successive character to confirm a full match
						for(int k=0; k<strlen(numStrings[i]); k++)
						{
							if(numStrings[i][k] != line[j+k])
								match = 0;
						}
							if(match == 1)
							{
								line[j+1] = (char)(i + 1 + '0');
								//since our parser ignores non-integer chars, we can just replace somewhere in the matching phrase
								// with the digit and our parser in main will get the message. no need to change the
								// size of our whole array or w/e and spend more clock cycles
							}						
					}
				}
			}
		}			
	}
	return line;
}

