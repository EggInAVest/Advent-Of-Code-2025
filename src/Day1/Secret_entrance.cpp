
#include <iostream>
#include <fstream>

int main()
{
	std::ifstream dataFile("moves.txt");
	if (not dataFile.is_open())
	{
		std::cout << "error\n";
		return (1);
	}
	std::string line;
	char direction;
	int position = 50;
	int answer = 0;
	while (std::getline(dataFile, line))
	{
		direction = line[0];
		std::string numberStr;
		numberStr = line.substr(1, line.size());
		int number = stoi(numberStr);

		if (direction == 'R')
		{
			for (int j = 0; j < number; j++)
			{
				position++;
				if (position > 99)
					position = 0;
				if (position == 0)
					answer++;
			}
		}
		else if (direction == 'L')
		{
			for (int j = 0; j < number; j++)
			{
				position--;
				if (position < 0)
				{
					position = 99;
				}
				if (position == 0)
					answer++;
			}
		}
	}
	std::cout << "The answer is: " << answer << std::endl;
	return (0);
}