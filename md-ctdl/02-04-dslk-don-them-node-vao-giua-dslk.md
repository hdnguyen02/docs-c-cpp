# [DSLK Đơn]. Thêm Node Vào Giữa DSLK

Bài viết này mình sẽ hướng dẫn thao tác thêm node vào giữa danh sách liên kết đơn, mã nguồn được cài đặt bằng cả ngôn ngữ lập trình C và C++ cũng như triển khai nhiều cách cài đặt khác nhau để bạn có thể dễ dàng tiếp cận nhất

**NỘI DUNG :** 

- **Thêm node vào giữa DSLK đơn quản lý bằng node head**
- **Thêm node vào giữa DSLK đơn quản lý bằng node head cách 2**
-  **Thêm node vào giữa DSLK đơn quản lý bằng node head và tail** 
- **Video tutorial** 

---

**1. Thêm node vào giữa DSLK đơn quản lý bằng node head**

Đối với việc chèn node vào giữa DSLK thì mình sẽ cho chèn vào các vị trí hợp lệ, ví dụ DSLK đơn của mình có 5 phần tử thì bạn có thể chèn vào các vị trí 1, 2, 3, 4, 5, 6. Việc chèn vào vị trí 6 tương đương với việc thêm node vào cuối DSLK.

Ngoài các vị trí chèn trên thì mình sẽ thông báo là không hợp lệ về vị trí chèn.

**Các bước để thêm node vào vị trí thứ K DSLK :** 

- Cấp phát động một node mới
- Duyệt tới node thứ K - 1 trong DSLK
- Cho node mới trỏ tới node thứ K
- Cho node K - 1 trỏ vào node mới

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
    newNode->next = NULL;
    return newNode;
}

void themdau(node **head, int x){
    node *newNode = makeNode(x);
    newNode->next = (*head);
    (*head) = newNode;
}

void themgiua(node **head, int x, int k){
    int n = len(*head);
    if(k < 1 || k > n + 1){
        printf("Vi tri chen khong hop le !\n");
        return;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        themdau(head, x); return;
    }
    else{
        node *tmp = *head;
        for(int i = 1; i < k - 1; i++){
            tmp = tmp->next;
        }
        newNode->next = tmp->next;
        tmp->next = newNode;
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(&head, i);
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
    struct node *next;
};

void duyet(node *head){
    while(head != NULL){
        cout << head->data << " ";
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
    node *newNode = new node;
    newNode->data = x;
    newNode->next = NULL;
    return newNode;
}

void themdau(node *&head, int x){
    node *newNode = makeNode(x);
    newNode->next = head;
    head = newNode;
}

void themgiua(node *&head, int x, int k){
    int n = len(head);
    if(k < 1 || k > n + 1){
        cout << "Vi tri chen khong hop le !\n";
        return;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        themdau(head, x); return;
    }
    else{
        node *tmp = head;
        for(int i = 1; i < k - 1; i++){
            tmp = tmp->next;
        }
        newNode->next = tmp->next;
        tmp->next = newNode;
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(head, i);
    }
    themgiua(head, 28, 5);
    themgiua(head, 28, 9);
    duyet(head);
}
```

Output :

```cpp
10 9 8 7 28 6 5 4 28 3 2 1
```

---

**2. Thêm node vào giữa DSLK đơn quản lý bằng node head cách 2**

Cách cài đặt thứ 2 này thì bạn không cần dùng con trỏ tới con trỏ hay tham chiếu tới con trỏ nhưng bạn cần viết hàm trả về con trỏ, để sau khi thay đổi head trong hàm thêm node vào giữa thì trong hàm main khi gọi hàm bạn sẽ gán lại hàm đó cho head.

**Mã nguồn C :** 

```cpp
#include "stdio.h"
#include "string.h"
#include "stdlib.h"

struct node{
    int data;
    struct node *next;
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
    newNode->next = NULL;
    return newNode;
}

node* themdau(node *head, int x){
    node *newNode = makeNode(x);
    newNode->next = head;
    head = newNode;
    return head;
}

node* themgiua(node *head, int x, int k){
    int n = len(head);
    if(k < 1 || k > n + 1){
        printf("Vi tri chen khong hop le !\n");
        return head;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        return themdau(head, x);
    }
    else{
        node *tmp = head;
        for(int i = 1; i < k - 1; i++){
            tmp = tmp->next;
        }
        newNode->next = tmp->next;
        tmp->next = newNode;
        return head;
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        head = themdau(head, i);
    }
    head = themgiua(head, 28, 5);
    head = themgiua(head, 28, 9);
    duyet(head);
}
```

**Mã nguồn C++:**

```cpp
#include "iostream"
using namespace std;

struct node{
    int data;
    struct node *next;
};

void duyet(node *head){
    while(head != NULL){
        cout << head->data << " ";
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
    node *newNode = new node;
    newNode->data = x;
    newNode->next = NULL;
    return newNode;
}

node* themdau(node *head, int x){
    node *newNode = makeNode(x);
    newNode->next = head;
    head = newNode;
    return head;
}

node* themgiua(node *head, int x, int k){
    int n = len(head);
    if(k < 1 || k > n + 1){
        cout << "Vi tri chen khong hop le !\n";
        return head;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        return themdau(head, x);
    }
    else{
        node *tmp = head;
        for(int i = 1; i < k - 1; i++){
            tmp = tmp->next;
        }
        newNode->next = tmp->next;
        tmp->next = newNode;
        return head;
    }
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        head = themdau(head, i);
    }
    head = themgiua(head, 28, 5);
    head = themgiua(head, 28, 9);
    duyet(head);
}
```

Output :

```cpp
10 9 8 7 6 5 4 3 2 1
```

---

**3. Thêm node vào giữa DSLK quản lý bằng node head và tail**

Cách cài đặt thứ 3 này thường xây dựng thêm 1 cấu trúc DSLK có 2 node head(đầu) và tail (cuối) để quản lý DSLK

**Chú ý** : Khi thêm node vào cuối DSLK đơn thì bạn phải cập nhật cho tail.

**Mã nguồn C :**

```cpp
#include "stdio.h"
#include "stdlib.h"

struct node{
    int data;
    struct node *next;
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
    newNode->next = NULL;
    return newNode;
}

void themdau(LIST *l, int x){
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = NULL;
    if(l->head == NULL){
        l->tail = newNode;
    }
    newNode->next = l->head;
    l->head = newNode;
}

void themgiua(LIST *l, int x, int k){
    int n = len(l->head);
    if(k < 1 || k > n + 1){
        printf("Vi tri chen khong hop le !\n");
        return;
    }
    node *newNode = makeNode(x);
    if(k == 1){
        themdau(l, x);
    }
    else{
        node *tmp = l->head;
        for(int i = 1; i < k - 1; i++){
            tmp = tmp->next;
        }
        newNode->next = tmp->next;
        if(tmp->next == NULL){
            l->tail = newNode;
        }
        tmp->next = newNode;
    }
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 1; i <= 10; i++){
        themdau(&l, i);
    }
    themgiua(&l, 28, 5);
    themgiua(&l, 28, 8);
    duyet(l);
}
```

---

**Video Chèn Node Vào Giữa DSLK Đơn**
