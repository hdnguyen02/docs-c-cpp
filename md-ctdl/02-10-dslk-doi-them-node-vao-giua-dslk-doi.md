# [DSLK Đôi]. Thêm Node Vào Giữa DSLK Đôi

Bài viết này mình sẽ hướng dẫn thao tác thêm node vào giữa danh sách liên kết đôi, mã nguồn được cài đặt bằng cả ngôn ngữ lập trình C và C++ cũng như triển khai nhiều cách cài đặt khác nhau để bạn có thể dễ dàng tiếp cận nhất

**NỘI DUNG :** 

- **Thêm node vào giữa DSLK đôi quản lý bằng node head**
-  **Thêm node vào giữa DSLK đôi quản lý bằng node head và tail** 
- **Video tutorial** 

---

**1. Thêm node vào giữa DSLK đôi quản lý bằng node head**

Đối với việc chèn node vào giữa DSLK thì mình sẽ cho chèn vào các vị trí hợp lệ, ví dụ DSLK đơn của mình có 5 phần tử thì bạn có thể chèn vào các vị trí 1, 2, 3, 4, 5, 6. Việc chèn vào vị trí 6 tương đương với việc thêm node vào cuối DSLK.

Ngoài các vị trí chèn trên thì mình sẽ thông báo là không hợp lệ về vị trí chèn.

Đối với danh sách liên kết đôi thì bạn có thể duyệt tới node K vì từ node K có thể quay lại được node K - 1.

**Các bước để thêm node vào vị trí thứ K DSLK :** 

- Cấp phát động một node mới
- Duyệt tới node thứ K trong DSLK
- Cho node mới trỏ tới node thứ K
- Cho node K - 1 trỏ vào node mới
- Cho node mới trỏ ngược lại node K - 1
- Cho node K trỏ ngược lại node mới

**Chú ý** : Vì khi bạn chèn vào vị trí thứ K trong DSLK thì bạn cần phải tới được node thứ K - 1, tuy nhiên nếu K = 1 thì DSLK không có node thứ 0 nên bạn cần xử lý riêng tương tự như là thêm node vào đầu DSLK

**Mã nguồn C :** 

Cài đặt dựa trên con trỏ tới con trỏ có thể áp dụng cho cả ngôn ngữ lập trình C và C++. Trong cách cài đặt này mình có thêm hàm len để đếm số node trong DSLK và hàm makeNode để nhanh chóng tạo node mới khi cần.

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

int len(node *head){
    int dem = 0;
    while(head != NULL){
        ++dem;
        head = head->next; // cho head chuyen sang node ke tiep
    }
    return dem;
}

node *makeNode(int x){
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    return newNode;
}

void themgiua(node **head, int x, int k){
    int n = len(*head);
    if(k < 1 || k > n + 1){
        printf("Vi tri chen khong hop le !\n");
        return;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        newNode->next = *head;
        if(*head != NULL){
            (*head)->prev = newNode;
        }
        *head = newNode;
    }
    else{
        //Duyet toi node k
        node *tmp = *head;
        for(int i = 1; i <= k - 1; i++){
            tmp = tmp->next;
        }
        //newnode => node thu k
        newNode->next = tmp;
        //Node thu k - 1 <=> new node
        tmp->prev->next = newNode;
        newNode->prev = tmp->prev;
        //Node k => newnode
        tmp->prev = newNode;
    }
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
        themgiua(&head, i, 1);
    }
    themgiua(&head, 28, 5);
    themgiua(&head, 28, 9);
    duyet(head);
}
```

**Mã nguồn C ++ :** 

Cài đặt dựa trên tham chiếu trong C++, lưu ý trong C không có tham chiếu nên bạn không được sử dụng nó khi lập trình.

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

node *makeNode(int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    return newNode;
}

int len(node *head){
    int dem = 0;
    while(head != NULL){
        ++dem;
        head = head->next; // cho head chuyen sang node ke tiep
    }
    return dem;
}

void themgiua(node *&head, int x, int k){
    int n = len(head);
    if(k < 1 || k > n + 1){
        cout << "Vi tri chen khong hop le !\n";
        return;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        newNode->next = head;
        if(head != NULL){
            head->prev = newNode;
        }
        head = newNode;
    }
    else{
        node *tmp = head;
        for(int i = 1; i <= k - 1; i++){
            tmp = tmp->next;
        }
        newNode->next = tmp;
        tmp->prev->next = newNode;
        newNode->prev = tmp->prev;
        tmp->prev = newNode;
    }
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
        themgiua(head, i, 1);
    }
    themgiua(head, 28, 5);
    themgiua(head, 28, 9);
    duyet(head);
}
```

Output :

```cpp
1 2 3 4 28 5 6 7 28 8 9 10
```

---

**2. Thêm node vào giữa DSLK quản lý bằng node head và tail**

Cách cài đặt thứ 3 này thường xây dựng thêm 1 cấu trúc DSLK có 2 node head(đầu) và tail (cuối) để quản lý DSLK

**Chú ý** : Khi thêm node vào cuối DSLK đơn thì bạn phải cập nhật cho tail.

**Mã nguồn C :**

```cpp
#include "stdio.h"
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

int len(node *head){
    int dem = 0;
    while(head != NULL){
        ++dem;
        head = head->next; // cho head chuyen sang node ke tiep
    }
    return dem;
}

node *makeNode(int x){
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    return newNode;
}

void themgiua(LIST *l, int x, int k){
    int n = len(l->head);
    if(k < 1 || k > n + 1){
        printf("Vi tri chen khong hop le !\n");
        return;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        if(l->head == NULL){
            l->head = l->tail = newNode;
        }
        else{
            newNode->next = l->head;
            l->head->prev = newNode;
            l->head = newNode;
        }
    }
    else{
        node *tmp = l->head;
        for(int i = 1; i <= k - 1; i++){
            tmp = tmp->next;
        }
        newNode->next = tmp;
        tmp->prev->next = newNode;
        newNode->prev = tmp->prev;
        tmp->prev = newNode;
        if(tmp->next == NULL){
            l->tail = newNode;
        }
    }
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 10; i >= 1; i--){
        themgiua(&l, i, 1);
    }
    themgiua(&l, 28, 5);
    themgiua(&l, 28, 8);
    duyet(l);
}
```

---

**Video Chèn Node Vào Giữa DSLK Đơn**
