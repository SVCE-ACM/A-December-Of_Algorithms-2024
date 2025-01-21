#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};

Node* createLinkedList(vector<int>& values) {
    Node* head = nullptr;
    Node* tail = nullptr;

    for (int value : values) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }
    return head;
}

int findIntersection(Node* head1, Node* head2) {
    while (head1) {
        Node* temp = head2;
        while (temp) {
            if (head1 == temp) return head1->data;
            temp = temp->next;
        }
        head1 = head1->next;
    }
    return -1;
}
