// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

// Definition of a Node in the linked list
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Function to create a linked list from an array of values
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

// Function to attach the second list at a specific position in the first list
void attachLists(Node* list1, Node* list2, int position) {
    if (position == 0) return; // No intersection
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
    // Input for the first linked list
    int n;
    cout << "Enter the number of nodes in the first linked list: ";
    cin >> n;
    int arr1[n];
    cout << "Enter the node values: ";
    for (int i = 0; i < n; ++i) {
        cin >> arr1[i];
    }

    // Input for the second linked list
    int m;
    cout << "Enter the number of nodes in the second linked list: ";
    cin >> m;
    int arr2[m];
    cout << "Enter the node values: ";
    for (int i = 0; i < m; ++i) {
        cin >> arr2[i];
    }

    // Input for the intersection position
    int pos;
    cout << "Enter the position of intersection (0 if no intersection): ";
    cin >> pos;

    // Create linked lists
    Node* list1 = createLinkedList(arr1, n);
    Node* list2 = createLinkedList(arr2, m);

    // Attach the second list to the first at the given position
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
