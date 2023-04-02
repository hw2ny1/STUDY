#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

/*
struct TRIE
{
    // 마지막인지 확인을 하기 위한 bool타입 변수
    bool Finish;
    // 알파벳을 노드를 표현할 포인터 배열
    TRIE* Node[26];
    // 생성자 (init)같은 것.
    TRIE()
    {
        Finish = false;
        for (int i = 0; i < 26; i++) Node[i] = NULL;
    }

    // Str이라는 문자열을 삽입하는 함수
    void Insert(char* Str)
    {
        // 만약 문자를 다 넣었다면 Finish에 true를 저장하여 표시
        if (*Str == NULL)
        {
            Finish = true;
            return;
        }
        // 문자를 정수로 변환
        int Cur = *Str - 'A';
        // 연결된 노드가 없는 경우, 새로운 노드를 생성.
        if (Node[Cur] == NULL) Node[Cur] = new TRIE();
        // 다음 문자로 넘어가는 과정.
        Node[Cur]->Insert(Str + 1);
    }

    bool Find(char* Str)
    {
        // 마지막 문자까지 왔을 경우,
        if (*Str == NULL)
        {
            // Finish를 확인해서 존재 유무 출력
            if (Finish == true) return true;
            return false;
        }
        // 문자를 정수로 변환
        int Cur = *Str - 'A';
        // 만약 연결된 노드가 없으면 false 출력
        if (Node[Cur] == NULL) return false;
        // 연결 되어있다면 
        return Node[Cur]->Find(Str + 1);
    }
    
    void IsSorting(TRIE* N, char Str[], int Idx)
    {
        if (N->Finish == true) cout << Str << endl;
        for (int i = 0; i < 26; i++)
        {
            if (N->Node[i] != NULL)
            {
                char C = i + 'A';
                Str[Idx] = C;
                N->IsSorting(N->Node[i], Str, Idx + 1);
            }
        }
    }
};
*/
const int NUM_ALPHABETS = 26;
int toIndex(char ch) { return ch - 'a'; }

struct TrieNode {
    TrieNode* children[NUM_ALPHABETS];
    // unordered_map<string, TrieNode*> children;
    bool isEnd;

    TrieNode() : children(), isEnd(false) {}

    void Insert(string& key, int index) {
        if (index == key.length() - 1)
            isEnd = true;
        else {
            int next = toIndex(key[index]);
            // nullptr은 포인터 값 중 NULL을 표현하는 값.
            if (children[next] == nullptr)
                children[next] = new TrieNode;
            children[next]->Insert(key, index + 1);
        }
    }

    bool Find_1(string& key, int depth) {   // 접두사로서 검색 되더라도 true 를 리턴하게끔 한 함수
        if (depth == key.length() - 1)
            return true;
        int next = toIndex(key[depth]);
        if (children[next] == nullptr)
            return false;
        return children[next]->Find_1(key, depth + 1);
    }

    bool Find_2(string& key, int depth) {  // 완전히 일치하는 단어 단위로만 찾고 true 를 리턴하게끔 한 함수
        if (depth == key.length() - 1 && isEnd)
            return true;
        if (depth == key.length() - 1 && !isEnd)
            return false;
        int next = toIndex(key[depth]);
        if (children[next] == nullptr)
            return false;
        return children[next]->Find_2(key, depth + 1);
    }
};

int main() {
    vector<string> words = { "what", "when", "yours", "apple", "her", "his", "you" };

    TrieNode root;
    for (string word : words)
        root.Insert(word, 0);

    string search = "wh";

    if (root.Find_1(search, 0)) cout << search << "가 검색 결과에 있습니다." << '\n';
    else cout << search << "가 검색 결과에 없습니다." << '\n';

    if (root.Find_2(search, 0)) cout << search << "가 검색 결과에 있습니다." << '\n';
    else cout << search << "가 검색 결과에 없습니다." << '\n';
}