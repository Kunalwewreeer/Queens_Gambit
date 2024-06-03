#include <bits/stdc++.h>
using namespace std;
#define black 1
#define white 2
#define blank 0

void print_board(vector<vector<int>> &board, int n)
{
    cout << "\nCurrent Board is" << endl;
    cout << "  ";
    for (int i = 0; i < n; i++)
    {
        cout << i << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        cout << i << " ";
        for (int j = 0; j < n; j++)
        {
            if (board[i][j] == black)
            {
                cout << "B ";
            }
            else if (board[i][j] == white)
            {
                cout << "W ";
            }
            else
            {
                cout << "* ";
            }
        }
        cout << endl;
    }
    cout << endl;
}

vector<pair<pair<int, int>, pair<int, int>>> valid_moves(vector<vector<int>> &board, int turn, int n)
{
    vector<pair<pair<int, int>, pair<int, int>>> ans;
    if (turn == white)
    {
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == white)
                {
                    continue;
                }
                else if (board[i][j] == blank)
                {
                    if (board[i + 1][j] != white)
                    {
                        continue;
                    }
                    else
                    {
                        ans.push_back({{i, j}, {i + 1, j}});
                    }
                }
                else
                {
                    if (j > 0 && board[i + 1][j - 1] == white)
                    {
                        ans.push_back({{i, j}, {i + 1, j - 1}});
                    }
                    if (j < n - 1 && board[i + 1][j + 1] == white)
                    {
                        ans.push_back({{i, j}, {i + 1, j + 1}});
                    }
                }
            }
        }
        return ans;
    }
    else
    {
        for (int i = 1; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == black)
                {
                    continue;
                }
                else if (board[i][j] == blank)
                {
                    if (board[i - 1][j] != black)
                    {
                        continue;
                    }
                    else
                    {
                        ans.push_back({{i, j}, {i - 1, j}});
                    }
                }
                else
                {
                    if (j > 0 && board[i - 1][j - 1] == black)
                    {
                        ans.push_back({{i, j}, {i - 1, j - 1}});
                    }
                    if (j < n - 1 && board[i - 1][j + 1] == black)
                    {
                        ans.push_back({{i, j}, {i - 1, j + 1}});
                    }
                }
            }
        }
        return ans;
    }
}

vector<pair<pair<int, int>, pair<int, int>>> valid_moves1(vector<vector<int>> &board, int turn, int n)
{
    vector<pair<pair<int, int>, pair<int, int>>> ans;
    if (turn == black)
    {
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == black)
                {
                    continue;
                }
                else if (board[i][j] == blank)
                {
                    if (board[i + 1][j] != black)
                    {
                        continue;
                    }
                    else
                    {
                        ans.push_back({{i, j}, {i + 1, j}});
                    }
                }
                else
                {
                    if (j > 0 && board[i + 1][j - 1] == black)
                    {
                        ans.push_back({{i, j}, {i + 1, j - 1}});
                    }
                    if (j < n - 1 && board[i + 1][j + 1] == black)
                    {
                        ans.push_back({{i, j}, {i + 1, j + 1}});
                    }
                }
            }
        }
        return ans;
    }
    else
    {
        for (int i = 1; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == white)
                {
                    continue;
                }
                else if (board[i][j] == white)
                {
                    if (board[i - 1][j] != white)
                    {
                        continue;
                    }
                    else
                    {
                        ans.push_back({{i, j}, {i - 1, j}});
                    }
                }
                else
                {
                    if (j > 0 && board[i - 1][j - 1] == white)
                    {
                        ans.push_back({{i, j}, {i - 1, j - 1}});
                    }
                    if (j < n - 1 && board[i - 1][j + 1] == white)
                    {
                        ans.push_back({{i, j}, {i - 1, j + 1}});
                    }
                }
            }
        }
        return ans;
    }
}

void make_move(vector<vector<int>> &board, pair<pair<int, int>, pair<int, int>> a)
{
    board[a.first.first][a.first.second] = board[a.second.first][a.second.second];
    board[a.second.first][a.second.second] = blank;
}
bool haswon1(vector<vector<int>> &board, int turn, int n)
{
    if (turn == white)
    {
        for (int i = 0; i < n; i++)
        {
            if (board[n - 1][i] == white)
            {
                return true;
            }
        }
        return false;
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            if (board[0][i] == black)
            {
                return true;
            }
        }
        return false;
    }
}

bool haswon(vector<vector<int>> &board, int turn, int n)
{
    if (turn == white)
    {
        for (int i = 0; i < n; i++)
        {
            if (board[0][i] == white)
            {
                return true;
            }
        }
        return false;
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            if (board[n - 1][i] == black)
            {
                return true;
            }
        }
        return false;
    }
}
int main()
{
    int n;
    cout << "Enter the size of the board(<=10)" << endl;
    cin >> n;
    cout << "Do you want to play as White(you get the priveledge to move first)\nReply with Y/N" << endl;
    char a;
    cin >> a;
    if (a == 'Y')
    {
        vector<vector<int>> board(n, vector<int>(n, blank));
        for (int i = 0; i < n; i++)
        {
            board[0][i] = black;
            board[n - 1][i] = white;
        }
        print_board(board, n);
        while (1 == 1)
        {

            vector<pair<pair<int, int>, pair<int, int>>> moves1 = valid_moves(board, white, n);
            if (moves1.size() == 0)
            {
                cout << "the game is a draw" << endl;
                break;
            }
            // To do 1////////////////////////////////////// Implement your function here for the case when you are white /////////////////////////////////
            ///////////////////////////////////////start/////////////////////////////////////////////////////////////

            int flag = 0;
            while (1 == 1)
            {
                cout << "Enter your move as white" << endl;
                pair<pair<int, int>, pair<int, int>> a;
                string s;
                cin >> s;
                a.first.first = s[0] - 48;
                a.first.second = s[1] - 48;
                a.second.first = s[2] - 48;
                a.second.second = s[3] - 48;
                for (int i = 0; i < moves1.size(); i++)
                {
                    if (moves1[i].first.first == a.first.first && moves1[i].first.second == a.first.second && moves1[i].second.first == a.second.first && moves1[i].second.second == a.second.second)
                    {
                        make_move(board, a);
                        print_board(board, n);
                        flag = 1;
                        break;
                    }
                    else
                    {
                        continue;
                    }
                }
                if (flag == 0)
                {
                    cout << "Invalid move,try again" << endl;
                }
                else
                {
                    break;
                }
            }
            ////////////////////////////////////////////////////////////////end////////////////////////////////////////////////////////////////////
            if (haswon(board, white, n) == true)
            {
                cout << "White wins" << endl;
                break;
            }

            vector<pair<pair<int, int>, pair<int, int>>> moves2 = valid_moves(board, black, n);
            if (moves2.size() == 0)
            {
                cout << "The game ends in a draw" << endl;
                break;
            }
            flag = 0;
            while (1 == 1)
            {
                cout << "Enter your move as black" << endl;
                pair<pair<int, int>, pair<int, int>> a;
                string s;
                cin >> s;
                a.first.first = s[0] - 48;
                a.first.second = s[1] - 48;
                a.second.first = s[2] - 48;
                a.second.second = s[3] - 48;
                for (int i = 0; i < moves2.size(); i++)
                {
                    if (moves2[i].first.first == a.first.first && moves2[i].first.second == a.first.second && moves2[i].second.first == a.second.first && moves2[i].second.second == a.second.second)
                    {
                        make_move(board, a);
                        print_board(board, n);
                        flag = 1;
                        break;
                    }
                    else
                    {
                        continue;
                    }
                }
                if (flag == 0)
                {
                    cout << "Invalid move,try again" << endl;
                }
                else
                {
                    break;
                }
            }
            if (haswon(board, black, n) == true)
            {
                cout << "Black wins" << endl;
                break;
            }
        }
    }
    else
    {
        vector<vector<int>> board(n, vector<int>(n, blank));
        for (int i = 0; i < n; i++)
        {
            board[n - 1][i] = black;
            board[0][i] = white;
        }
        print_board(board, n);
        while (1 == 1)
        {
            vector<pair<pair<int, int>, pair<int, int>>> moves1 = valid_moves1(board, white, n);
            if (moves1.size() == 0)
            {
                cout << "the game is a draw" << endl;
                break;
            }

            int flag = 0;
            while (1 == 1)
            {
                cout << "Enter your move as white" << endl;
                pair<pair<int, int>, pair<int, int>> a;
                string s;
                cin >> s;
                a.first.first = s[0] - 48;
                a.first.second = s[1] - 48;
                a.second.first = s[2] - 48;
                a.second.second = s[3] - 48;
                for (int i = 0; i < moves1.size(); i++)
                {
                    if (moves1[i].first.first == a.first.first && moves1[i].first.second == a.first.second && moves1[i].second.first == a.second.first && moves1[i].second.second == a.second.second)
                    {
                        make_move(board, a);
                        print_board(board, n);
                        flag = 1;
                        break;
                    }
                    else
                    {
                        continue;
                    }
                }
                if (flag == 0)
                {
                    cout << "Invalid move,try again" << endl;
                }
                else
                {
                    break;
                }
            }
            if (haswon1(board, white, n) == true)
            {
                cout << "White wins" << endl;
                break;
            }

            vector<pair<pair<int, int>, pair<int, int>>> moves2 = valid_moves1(board, black, n);
            if (moves2.size() == 0)
            {
                cout << "The game ends in a draw" << endl;
                break;
            }
            // To do 2/////////////////////////////////////////Implement your function here for the case when you are black//////////////////////////////////////////
            //////////////////////////////////////////start//////////////////////////////////////////////////////
            flag = 0;
            while (1 == 1)
            {
                cout << "Enter your move as black" << endl;
                pair<pair<int, int>, pair<int, int>> a;
                string s;
                cin >> s;
                a.first.first = s[0] - 48;
                a.first.second = s[1] - 48;
                a.second.first = s[2] - 48;
                a.second.second = s[3] - 48;
                for (int i = 0; i < moves2.size(); i++)
                {
                    if (moves2[i].first.first == a.first.first && moves2[i].first.second == a.first.second && moves2[i].second.first == a.second.first && moves2[i].second.second == a.second.second)
                    {
                        make_move(board, a);
                        print_board(board, n);
                        flag = 1;
                        break;
                    }
                    else
                    {
                        continue;
                    }
                }
                if (flag == 0)
                {
                    cout << "Invalid move,try again" << endl;
                }
                else
                {
                    break;
                }
            }
            ///////////////////////////////////////////////////////////////end/////////////////////////////////////////////////////////////////////////////////
            if (haswon1(board, black, n) == true)
            {
                cout << "Black wins" << endl;
                break;
            }
        }
    }
}
