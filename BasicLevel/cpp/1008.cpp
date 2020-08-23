#include<iostream>
#include<vector>
using namespace std;

int main()
{
	unsigned int length, num_to_move;
	cin >> length >> num_to_move;

	//cout << length << num_to_move << endl;
	num_to_move %= length;

	vector<int> arr;
	int temp;

	for (size_t i = 0; i < length; i++)
	{
		cin >> temp;
		arr.push_back(temp);
	}


	for (size_t i = 0, j = 0; j < arr.size(); j++)
	{
		if (j < num_to_move)
			i = j - num_to_move + length;
		else
			i = j - num_to_move;
		
		if (j == arr.size() - 1)
			cout << arr[i];
		else
			cout << arr[i] << ' ';
	}

	system("pause");
	return 0;
}