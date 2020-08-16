#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main(){
    ofstream file;
    fstream f;
    file.open("settings.txt", ios::trunc);
    file.close();
    string token, messagetobot, messagetouser;
    cout << "Enter token\n";
    cin >> token;
    while (true){
            cout << "Do you want to rewrite the token or to continue? 1/2\n";
        int tokenanswer;
        cin >> tokenanswer;
        if (tokenanswer==1){
            file.open("settings.txt", ios::trunc);
            file.close();
            cout << "Enter token\n";
            cin >> token;
        }
        if (tokenanswer==2){
            f.open("settings.txt", ios::app);
            f << token << "\n";
            f.close();
            break;
        }
    }
    cout << "Enter message to bot\n";
    cin >> messagetobot;
    cout << "Enter message to user\n";
    cin >> messagetouser;
    f.open("settings.txt", ios::app);
    f  << "\n"<< messagetobot << "\n" <<messagetouser << "\n";
    while (true){
        cout << "Do you want to add more messages or save? 1/2\n";
        int answer;
        cin >> answer;
        if (answer==1){
            cout << "Enter message to bot\n";
            cin >> messagetobot;
            cout << "Enter message to user\n";
            cin >> messagetouser;
            f << "\n" << messagetobot << "\n" <<messagetouser << "\n";
        }
        if (answer==2){
            f.close();
            cout << "File is saved, close the window\n";
            break;
        }
    }
    system("pause");
}
// Made by alde-the-coder
// Version 2.0