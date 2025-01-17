// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;


struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};


Node* createLinkedList(int arr[], int size) {
    if (size == 0) return nullptr;
    Node* head = new Node(arr[0]);
    Node* current = head;
    for (int i = 1; i < size; ++i) {
        current->next = new Node(arr[i]);
        current = current->next;
    }
    return head;
}
void attachLists(Node* list1, Node* list2, int position) {
    if (position == 0) return; 
    Node* current = list1;
    for (int i = 1; i < position && current != nullptr; ++i) {
        current = current->next;
    }
    if (current != nullptr) {
        Node* temp = list2;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = current;
    }
}

int main() {
 
    int n;
    cout << "Enter the number of nodes in the first linked list: ";
    cin >> n;
    int arr1[n];
    cout << "Enter the node values: ";
    for (int i = 0; i < n; ++i) {
        cin >> arr1[i];
    }
    int m;
    cout << "Enter the number of nodes in the second linked list: ";
    cin >> m;
    int arr2[m];
    cout << "Enter the node values: ";
    for (int i = 0; i < m; ++i) {
        cin >> arr2[i];
    }
    int pos;
    cout << "Enter the position of intersection (0 if no intersection): ";
    cin >> pos;

 
    Node* list1 = createLinkedList(arr1, n);
    Node* list2 = createLinkedList(arr2, m);

    attachLists(list1, list2, pos);

    if (pos == 0) {
        cout << "No intersection found." << endl;
    } else {
        Node* current = list1;
        for (int i = 1; i < pos && current != nullptr; ++i) {
            current = current->next;
        }
        if (current) {
            cout << "The intersection point is: " << current->data << endl;
        }
    }

    return 0;
}
