# [DSLK Đôi]. Xóa Node Cuối Trong DSLK Đôi

Bài viết này mình sẽ hướng dẫn các bạn thao tác xóa node cuối cùng trong DSLK đôi, mã nguồn được cài đặt bằng cả C và C++ cũng như trình bày theo 2 cách để các bạn có thêm cách tiếp cận phù hợp.

**NỘI DUNG :** 

- **Xóa node cuối trong DSLK đôi quản lý bởi node head**
- **Xóa node cuối trong DSLK đôi quản lý bởi node head và tail** 
- **Video tutorial** 

---

**1. Xóa node cuối trong DSLK đôi quản lý bởi node head**

Để xóa node cuối trong danh sách liên kết bạn thực hiện theo các bước sau đây :

- Duyệt đến node thứ 2 từ cuối về
- Lưu lại node cuối trong DSLK
- Cho node thứ 2 trong DSLK trỏ vào NULL
- Giải phóng vùng nhớ node cuối đã lưu ở bước 2

**Chú ý** : Nếu DSLK đơn chỉ có 1 node thì bạn cần xử lý riêng vì nó không có node thứ 2 từ cuối về trong trường hợp này. Để duyệt tới node thứ 2 từ cuối về bạn để điều kiện lặp head->next->next != NULL, nếu DSLK chỉ có 1 node thì câu lệnh này sẽ gây lỗi bộ nhớ nên việc xử lý khi DSLK có 1 node là cần thiết.

**Mã nguồn C :** 

Cài đặt bằng con trỏ cấp 2 (con trỏ tới con trỏ), cách này bạn có thể áp dụng cho cả C++, chỉ cần thay đổi cách giải phóng vùng nhớ của node.

```cpp
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

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

void xoacuoi(node **head){
    if(*head == NULL) return; // DSLK rong
    if((*head)->next == NULL){
        free(*head);
        (*head) = NULL;
    }
    else{
        node *tmp = (*head);
        //Duyet den node thu 2 tu cuoi ve : tmp
        while(tmp->next->next != NULL){
            tmp = tmp->next;
        }
        //Luu lai node cuoi de giai phong
        node *delNode = tmp->next;
        //Cho node tmp => NULL
        tmp->next = NULL;
        //Giai phong node cuoi
        delete delNode;
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(&head, i);
    }
    duyet(head);
    xoacuoi(&head);
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

void xoacuoi(node *&head){
    if(head == NULL) return; // DSLK rong
    if(head->next == NULL){
        delete head;
        head = NULL;
    }
    else{
        node *tmp = head;
        while(tmp->next->next != NULL){
            tmp = tmp->next;
        }
        node *delNode = tmp->next;
        tmp->next = NULL;
        delete delNode;
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(head, i);
    }
    duyet(head);
    xoacuoi(head);
    cout << endl;
    duyet(head);
}
```

Output :

```cpp
10 9 8 7 6 5 4 3 2 1 
10 9 8 7 6 5 4 3 2
```

---

**2. Xóa node cuối trong DSLK đôi quản lý bởi node head và tail**

Tương tự như trong các bài viết trước về DSLK đơn thì các bạn cũng có thể xây dựng thêm cấu trúc để quản lý DSLK thông qua con trỏ head(đầu) và tail (cuối).

**Mã nguồn C :** 

```cpp
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

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

void xoacuoi(LIST *l){
    if(l->head == NULL) return; //DSLK rong
    if(l->head->next == NULL){
        delete l->head;
        l->head = l->tail = NULL;
    }
    else{
        node *tmp = l->head;
        while(tmp->next->next != NULL){
            tmp = tmp->next;
        }
        node *delNode = tmp->next;
        tmp->next = NULL;
        l->tail = tmp;
        free(delNode);
    }
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(&l, i);
    }
    duyet(l);
    xoacuoi(&l);
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

void xoacuoi(LIST &l){
    if(l.head == NULL) return; //DSLK rong
    if(l.head->next == NULL){
        delete l.head;
        l.head = l.tail = NULL;
    }
    else{
        node *tmp = l.head;
        while(tmp->next->next != NULL){
            tmp = tmp->next;
        }
        node *delNode = tmp->next;
        tmp->next = NULL;
        l.tail = tmp;
        delete delNode;
    }
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(l, i);
    }
    duyet(l);
    cout << endl;
    xoacuoi(l);
    duyet(l);
}
```

Output :

```cpp
10 9 8 7 6 5 4 3 2 1 
10 9 8 7 6 5 4 3 2
```

---

**Video Xóa Node Đầu Trong DSLK Đơn**
