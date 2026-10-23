# [DSLK Đôi]. Xóa Node Đầu Trong DSLK Đôi

Bài viết này mình sẽ hướng dẫn các bạn thao tác xóa node đầu tiên trong DSLK đôi, mã nguồn được cài đặt bằng cả C và C++ cũng như trình bày theo 2 cách để các bạn có thêm cách tiếp cận phù hợp.

**NỘI DUNG :** 

- **Xóa node đầu trong DSLK đôi quản lý bởi node head**
- **Xóa node đầu trong DSLK đôi quản lý bởi node head và tail** 
- **Video tutorial** 

---

**1. Xóa node đầu trong DSLK đôi quản lý bởi node head**

Để xóa node đầu trong danh sách liên kết bạn thực hiện theo các bước sau đây :

- Lưu lại node đầu trong DSLK để giải phóng
- Cho node head trỏ sang node thứ 2 trong DSLK
- Cho node thứ 2 trong DSLK trỏ ngược lại NULL
- Giải phóng vùng nhớ node đầu trong DSLK đã lưu ở bước 1

Các bạn cần chú ý kiểm tra DSLK không rỗng thì hãy cho phép xóa node đầu.

**Mã nguồn C :** 

Cài đặt bằng con trỏ cấp 2 (con trỏ tới con trỏ), cách này bạn có thể áp dụng cho cả C++, chỉ cần thay đổi cách giải phóng vùng nhớ của node.

```cpp
#include "stdio.h"
#include "string.h"
#include "stdlib.h"

struct node{
    int data;
    struct node *next;
    struct node *prev;
};
typedef struct node node;

void duyet(node *head){
    while(head != NULL){
        printf("%d ", head->data);
        head = head->next; // cho head chuyen sang node ke tiep
    }
}

void themdau(node **head, int x){
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    newNode->next = (*head);
    (*head) = newNode;
}

void xoadau(node **head){
    if(*head == NULL) return; // DSLK rong
    node *deleteNode = *head;
    //Cho node head thanh node thu 2 trong DSLK
    (*head) = (*head)->next; 
    //Neu head != NULL thi tro ngược lại vào NULL
    if(*head != NULL){
        (*head)->prev = NULL;
    }
    //Giai phong vung nho
    free(deleteNode);
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(&head, i);
    }
    duyet(head);
    xoadau(&head);
    printf("\n");
    duyet(head);
}
```

**Mã nguồn C++ :** 

```cpp
#include "iostream"
using namespace std;

struct node{
    int data;
    node *next;
    node *prev;
};

void duyet(node *head){
    while(head != NULL){
        cout << head->data << " ";
        head = head->next; // cho head chuyen sang node ke tiep
    }
}

void themdau(node *&head, int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    newNode->next = head;
    head = newNode;
}

void xoadau(node *&head){
    if(head == NULL) return; // DSLK rong
    node *deleteNode = head;
    head = head->next;
    if(head != NULL){
        head->prev = NULL;
    }
    delete deleteNode;
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(head, i);
    }
    duyet(head);
    xoadau(head);
    cout << endl;
    duyet(head);
}
```

Output :

```cpp
1 2 3 4 5 6 7 8 9 10 
2 3 4 5 6 7 8 9 10
```

---

**2. Xóa node đầu trong DSLK đôi quản lý bởi node head và tail**

Tương tự như trong các bài viết trước về DSLK đơn thì các bạn cũng có thể xây dựng thêm cấu trúc để quản lý DSLK thông qua con trỏ head(đầu) và tail (cuối).

**Mã nguồn C :** 

```cpp
#include "stdio.h"
#include "string.h"
#include "stdlib.h"

struct node{
    int data;
    struct node *next;
    struct node *prev;
};
typedef struct node node;

struct LIST{
    node *head;
    node *tail;
};
typedef struct LIST LIST;

void duyet(LIST l){
    if(l.head == NULL){
        printf("DSLK rong !\n");
    }
    else{
        node *tmp = l.head;
        while(tmp != NULL){
            printf("%d ", tmp->data);
            tmp = tmp->next;
        }
    }
}

void themdau(LIST *l, int x){
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;

    if(l->head == NULL){
        l->tail = l->head = newNode;
    }
    else{
        newNode->next = l->head;
        l->head->prev = newNode;
        l->head = newNode;
    }
}

void xoadau(LIST *l){
    if(l->head == NULL) return; //DSLK rong
    node *delNode = l->head;
    l->head = l->head->next;
    if(l->head == NULL) 
        l->tail = NULL;
    else
        l->head->prev = NULL;
    free(delNode);
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(&l, i);
    }
    duyet(l);
    xoadau(&l);
    printf("\n");
    duyet(l);
}
```

**Mã nguồn C++ :** 

```cpp
#include "iostream"

using namespace std;

struct node{
    int data;
    node *next;
    node *prev;
};

struct LIST{
    node *head;
    node *tail;
};

void duyet(LIST l){
    if(l.head == NULL){
        cout << "DSLK rong !\n";
    }
    else{
        node *tmp = l.head;
        while(tmp != NULL){
            cout << tmp->data << ' ';
            tmp = tmp->next;
        }
    }
}

void themdau(LIST &l, int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    if(l.head == NULL){
        l.tail = l.head = newNode;
    }
    else{
        newNode->next = l.head;
        l.head->prev = newNode;
        l.head = newNode;
    }
}

void xoadau(LIST &l){
    if(l.head == NULL) return;
    node *delNode = l.head;
    l.head = l.head->next;
    if(l.head == NULL) 
        l.tail = NULL;
    else
        l.head->prev = NULL;
    delete delNode;
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(l, i);
    }
    duyet(l);
    cout << endl;
    xoadau(l);
    duyet(l);
}
```

Output :

```cpp
1 2 3 4 5 6 7 8 9 10 
2 3 4 5 6 7 8 9 10
```

---

**Video Xóa Node Đầu Trong DSLK Đơn**
