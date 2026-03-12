#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
  int numFemale, numMale, numOthers;
  double percF, percM, percO;

  cout << "Enter the number of students: Male, Female and Others";
  cin >> numMale >> numFemale >> numOthers;
  double total = numMale + numFemale + numOthers;
  percM = (numMale * 100.0) / total;
  percF = (numFemale * 100.0) / total;
  percO = (numOthers * 100.0) / total;

  cout << setprecision(2) << fixed;
  cout << "Percentage of Male: " << percM << endl;
  cout << "Percentage of Female: " << percF << endl;
  cout << "Percentage of Others: " << percO << endl;
}
