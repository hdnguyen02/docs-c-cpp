# [DSLK Đôi]. Xóa Node Giữa Trong DSLK Đôi

Bài viết này mình sẽ hướng dẫn các bạn thao tác xóa node giữa trong DSLK đôi, mã nguồn được cài đặt bằng cả C và C++ cũng như trình bày theo 2 cách để các bạn có thêm cách tiếp cận phù hợp.

**NỘI DUNG :** 

- **Xóa node giữa trong DSLK đôi quản lý bởi node head**
- **Xóa node giữa trong DSLK đôi quản lý bởi node head và tail** 
- **Video tutorial** 

---

**1. Xóa node giữa trong DSLK đôi quản lý bởi node head**

Để xóa node giữa tại vị trí thứ K trong danh sách liên kết bạn thực hiện theo các bước sau đây :

- Duyệt đến node k trong DSLK
- Lưu lại địa chỉ node thứ k
- Cho node k - 1 trỏ vào node k + 1
- Cho node k + 1 trỏ ngược lại node k - 1
- Giải phóng vùng nhớ node thứ k đã lưu ở bước 2

**Chú ý** : Nếu DSLK đơn chỉ có 1 node thì bạn cần xử lý riêng vì với việc xóa trong DSLK đơn nếu bạn xóa node thứ k ta cần tới được node thứ k - 1 và tìm cách kết nối node này với node k + 1.

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
    if(*head != NULL){
        (*head)->prev = newNode;
    }
    (*head) = newNode;
}

int len(node *head){
    int dem = 0;
    while(head != NULL){
        ++dem;
        head = head->next; // cho head chuyen sang node ke tiep
    }
    return dem;
}

void xoadau(node **head){
    if(*head == NULL) return; // DSLK rong
    node *deleteNode = *head;
    //Cho node head thanh node thu 2 trong DSLK
    (*head) = (*head)->next; 
    if(*head != NULL){
        (*head)->prev = NULL;
    }
    //Giai phong vung nho
    free(deleteNode);
}

void xoagiua(node **head, int k){
    if(k < 1 || k > len(*head)) return; // vi tri xoa ko hop le
    if(k == 1){
        xoadau(head);
    }
    else{
        node *tmp = (*head);
        //Duyet den node k 
        for(int i = 1; i <= k - 1; i++){
            tmp = tmp->next;
        }
        //Luu lai node thu k
        node *delNode = tmp;
        //Cho k - 1 => tro vao k + 1
        tmp->prev->next = tmp->next;
        //Cho k + 1 => tro nguoc vao k - 1
        if(tmp->next != NULL){
            tmp->next->prev = tmp->prev;
        }
        //Giai phong node thu k
        free(delNode);
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(&head, i);
    }
    duyet(head);
    xoagiua(&head, 3);
    printf("\n");
    duyet(head);
}
```

Cài đặt bằng con trỏ cấp 2 (con trỏ tới con trỏ), cách này bạn có thể áp dụng cho cả C++, chỉ cần thay đổi cách giải phóng vùng nhớ của node.

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
    newNode->next = newNode->prev = newNode;
    newNode->next = head;
    if(head != NULL) head->prev = newNode;
    head = newNode;
}

int len(node *head){
    int dem = 0;
    while(head != NULL){
        ++dem;
        head = head->next; // cho head chuyen sang node ke tiep
    }
    return dem;
}

void xoadau(node *&head){
    if(head == NULL) return; // DSLK rong
    node *deleteNode = head;
    head = head->next;
    if(head != NULL) head->prev = NULL;
    delete deleteNode;
}

void xoagiua(node *&head, int k){
    if(k < 1 || k > len(head)) return; // vi tri xoa ko hop le
    if(k == 1){
        xoadau(head);
    }
    else{
        node *tmp = head;
        //Duyet den node k - 1
        for(int i = 1; i <= k - 1; i++){
            tmp = tmp->next;
        }
        //Luu lai node thu k
        node *delNode = tmp;
        //Cho k - 1 => tro vao k + 1
        tmp->prev->next = tmp->next;
        //Cho k + 1 => tro nguoc k - 1
        if(tmp->next != NULL)
            tmp->next->prev = tmp->prev;
        //Giai phong node thu k
        delete delNode;
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(head, i);
    }
    duyet(head);
    xoagiua(head, 3);
    cout << endl;
    duyet(head);
}
```

Output :

```cpp
10 9 8 7 6 5 4 3 2 1 
10 9 7 6 5 4 3 2 1
```

---

**2. Xóa node giữa trong DSLK đôi quản lý bởi node head và tail**

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

int len(LIST l){
    int dem = 0;
    while(l.head != NULL){
        ++dem;
        l.head = l.head->next;
    }
    return dem;
}

void themdau(LIST *l, int x){
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = NULL;
    if(l->head == NULL){
        l->tail = l->head = newNode; return;
    }
    newNode->next = l->head;
    l->head->prev = newNode; 
    l->head = newNode;
}

void xoadau(LIST *l){
    if(l->head == NULL) return; //DSLK rong
    node *delNode = l->head;
    l->head = l->head->next;
    if(l->head != NULL)
        l->head->prev = NULL;
    else 
        l->tail = NULL;
    free(delNode);
}

void xoagiua(LIST *l, int k){
    if(k < 1 || k > len(*l)) return; // vi tri xoa ko hop le
    if(k == 1){
        xoadau(l);
    }
    else{
        node *tmp = l->head;
        //Duyet den node k 
        for(int i = 1; i <= k - 1; i++){
            tmp = tmp->next;
        }
        //Luu lai node thu k
        node *delNode = tmp;
        //Cho k - 1 => tro vao k + 1
        tmp->prev->next= tmp->next;
        //Cho k + 1 => tro nguoc vao k - 1
        tmp->next->prev = tmp->prev;
        if(tmp->next == NULL)
            l->tail = tmp->prev;
        //Giai phong node thu k
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
    xoagiua(&l, 3);
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
    struct node *next;
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

int len(LIST l){
    int dem = 0;
    while(l.head != NULL){
        ++dem; l.head = l.head->next;
    }
    return dem;
}

void themdau(LIST &l, int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = NULL;
    if(l.head == NULL){
        l.tail = newNode;
    }
    newNode->next = l.head;
    l.head = newNode;
}

void xoadau(LIST &l){
    if(l.head == NULL) return;
    node *delNode = l.head;
    l.head = l.head->next;
    if(l.head == NULL) 
        l.tail = NULL;
    delete delNode;
}

void xoagiua(LIST &l, int k){
    if(k < 1 || k > len(l)) return; // vi tri xoa ko hop le
    if(k == 1){
        xoadau(l);
    }
    else{
        node *tmp = l.head;
        //Duyet den node k - 1
        for(int i = 1; i <= k - 2; i++){
            tmp = tmp->next;
        }
        //Luu lai node thu k
        node *delNode = tmp->next;
        //Cho k - 1 => tro vao k + 1
        tmp->next = delNode->next;
        if(tmp->next == NULL)
            l.tail = tmp;
        //Giai phong node thu k
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
    xoagiua(l, 3);
    duyet(l);
}
```

Output :

```cpp
10 9 8 7 6 5 4 3 2 1 
10 9 7 6 5 4 3 2 1
```

---

**Video Xóa Node Giữa Trong DSLK Đơn**
