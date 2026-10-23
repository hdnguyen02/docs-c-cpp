# [DSLK Đôi]. Thêm Node Vào Cuối DSLK Đôi

Bài viết này mình sẽ hướng dẫn thao tác thêm node vào cuối danh sách liên kết đôi, mã nguồn được cài đặt bằng cả ngôn ngữ lập trình C và C++ cũng như triển khai nhiều cách cài đặt khác nhau để bạn có thể dễ dàng tiếp cận nhất

**NỘI DUNG :** 

- **Thêm node vào cuối DSLK đơn quản lý bằng node head**
-  **Thêm node vào cuối DSLK đơn quản lý bằng node head và tail** 
- **Video tutorial** 

---

**1. Thêm node vào cuối DSLK đôi quản lý bằng node head**

Tương tự như bài học trước thì cách cài đặt này sẽ sử dụng con trỏ tới con trỏ hay tham chiếu để sửa đổi node head trong DSLK đôi.

**Các bước để thêm node vào cuối DSLK :** 

- Cấp phát động một node mới
- Duyệt tới node cuối trong DSLK
- Cho node cuối trỏ tới node mới (lưu địa chỉ của node mới)
- Cho node mới trỏ ngược lại node cuối

**Chú ý** : Nếu DSLK đôi đang rỗng tức là node head trong DSLK là con trỏ NULL bạn cần xử lý riêng, vì khi đó ta không có node cuối trong DSLK để trỏ vào node mới.

**Mã nguồn C :** 

Cài đặt dựa trên con trỏ tới con trỏ, cách này dùng được cho cả C và C++. Bạn tự cài đặt cho C++ bằng cách thay đổi cách cấp phát động và câu lệnh cout.

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

void themcuoi(node **head, int x){
    //1. Cap phat dong node moi
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    //Neu DSLK rong => xu ly rieng
    if(*head == NULL){
        *head = newNode; return;
    }
    //2. Duyet node cuoi trong DSLK
    node *tmp = *head;
    while(tmp->next != NULL){
        tmp = tmp->next;
    }
    //3. Cho node cuoi tro vao node moi
    tmp->next = newNode;
    //4. Cho node moi tro nguoc lai node cuoi
    newNode->prev = tmp;
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themcuoi(&head, i);
    }
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

void themcuoi(node *&head, int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    if(head == NULL){
        head = newNode; return;
    }
    node *tmp = head;
    while(tmp->next != NULL){
        tmp = tmp->next;
    }
    tmp->next = newNode;
    newNode->prev = tmp;
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        themcuoi(head, i);
    }
    duyet(head);
}
```

Output :

```cpp
1 2 3 4 5 6 7 8 9 10
```

---

**2. Thêm node vào cuối DSLK đôi quản lý bằng node head cách 2**

Cách cài đặt thứ 2 này thì bạn không cần dùng con trỏ tới con trỏ hay tham chiếu tới con trỏ nhưng bạn cần viết hàm trả về con trỏ, để sau khi thay đổi head trong hàm thêm node vào cuối thì trong hàm main khi gọi hàm bạn sẽ gán lại hàm đó cho head.

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

void duyet(node *head){
    while(head != NULL){
        printf("%d ", head->data);
        head = head->next; // cho head chuyen sang node ke tiep
    }
}

node* themcuoi(node *head, int x){
    //1. Cap phat dong node moi
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    //Neu DSLK rong thi tra ve luon node moi
    if(head == NULL){
        return newNode;
    }
    node *tmp = head;
    while(tmp->next != NULL){
        tmp = tmp->next;
    }
    tmp->next = newNode;
    newNode->prev = tmp;
    return head;
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
       head = themcuoi(head, i);
    }
    duyet(head);
}
```

**Mã nguồn C++:**

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

node* themdau(node *head, int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    if(head == NULL){
        return newNode;
    }
    node *tmp = head;
    while(tmp->next != NULL){
        tmp = tmp->next;
    }
    tmp->next = newNode;
    newNode->prev = tmp;
    return head;
}

int main(){
    node *head = NULL;
    for(int i = 1; i <= 10; i++){
        head = themdau(head, i);
    }
    duyet(head);
}
```

Output :

```cpp
1 2 3 4 5 6 7 8 9 10
```

---

**3. Thêm node vào đầu DSLK đôi quản lý bằng node head và tail**

Cách cài đặt thứ 3 này thường xây dựng thêm 1 cấu trúc DSLK có 2 node head(đầu) và tail (cuối) để quản lý DSLK

Do ta quản lý DSLK bằng con trỏ head và tail nên khi thêm vào cuối bạn chỉ cần kiểm tra DSLK rỗng thì sẽ để cả head và tail đều là node mới. Ngược lại bạn cho con trỏ tail lưu địa chỉ của node mới và cập nhật tail.

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

void themcuoi(LIST *l, int x){
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    if(l->head == NULL){
        l->head = newNode;
        l->tail = newNode;
    }
    else{
        l->tail->next = newNode;
        newNode->prev = l->tail;
        l->tail = newNode;
    }
}

int main(){
    //Khoi tao list
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 1; i <= 10; i++){
        themcuoi(&l, i);
    }
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

void themcuoi(LIST &l, int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    if(l.head == NULL){
        l.head = newNode;
        l.tail = newNode;
    }
    else{
        l.tail->next = newNode;
        newNode->prev = l.tail;
        l.tail = newNode;
    }
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 1; i <= 10; i++){
        themcuoi(l, i);
    }
    duyet(l);
}
```

Output :

```cpp
1 2 3 4 5 6 7 8 9 10
```

---

**Video Thêm Node Vào Cuối DSLK Đôi**
