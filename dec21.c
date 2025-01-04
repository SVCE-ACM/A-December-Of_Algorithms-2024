//(21) The Intersection
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* create_list(int n) {
    Node* head = NULL;
    Node* temp = NULL;
    Node* ptr = NULL;
    for (int i = 0; i < n; i++) {
        temp = (Node*)malloc(sizeof(Node));
        scanf("%d", &temp->data);
        temp->next = NULL;
        if (head == NULL) {
            head = temp;
            ptr = head;
        } else {
            ptr->next = temp;
            ptr = ptr->next;
        }
    }
    return head;
}

Node* get_intersection(Node* head1, Node* head2, int pos) {
    if (pos == 0) return NULL;
    Node* temp1 = head1;
    Node* temp2 = head2;
    for (int i = 1; i < pos; i++) {
        temp1 = temp1->next;
    }
    while (temp2->next != NULL) {
        temp2 = temp2->next;
    }
    temp2->next = temp1;
    return temp1;
}

void print_intersection(Node* head1, Node* head2) {
    Node* temp1 = head1;
    Node* temp2 = head2;
    while (temp1 != NULL && temp2 != NULL) {
        if (temp1 == temp2) {
            printf("The intersection point is: %d\n", temp1->data);
            return;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    printf("No intersection found.\n");
}

int main() {
    int n, m, pos;
    Node *head1, *head2;
    
    printf("Enter the number of nodes in the first linked list: ");
    scanf("%d", &n);
    printf("Enter the node values: ");
    head1 = create_list(n);

    printf("Enter the number of nodes in the second linked list: ");
    scanf("%d", &m);
    printf("Enter the node values: ");
    head2 = create_list(m);

    printf("Enter the position of intersection: ");
    scanf("%d", &pos);

    get_intersection(head1, head2, pos);
    print_intersection(head1, head2);

    return 0;
}

