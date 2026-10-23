# [DSLK Đôi]. Thêm Node Vào Đầu DSLK Đôi

Bài viết này mình sẽ hướng dẫn thao tác thêm node vào đầu danh sách liên kết đôi, mã nguồn được cài đặt bằng cả ngôn ngữ lập trình C và C++ cũng như triển khai nhiều cách cài đặt khác nhau để bạn có thể dễ dàng tiếp cận nhất

**NỘI DUNG :** 

- **Thêm node vào đầu DSLK đôi quản lý bằng node head**
- **Thêm node vào đầu DSLK đôi quản lý bằng node head cách 2**
-  **Thêm node vào đầu DSLK đôi quản lý bằng node head và tail** 
- **Video tutorial** 

---

**1. Thêm node vào đầu DSLK đôi quản lý bằng node head**

Danh sách liên kết đôi có thêm một liên kết tới node trước trong danh sách liên kết. Các thao tác của danh sách liên kết đôi cũng nhiều hơn so với danh sách liên kết đơn, đổi lại việc duyệt xóa và chèn trong DSLK đôi có phần dễ dàng hơn.

Cách cài đặt này mình sẽ chỉ sử dụng duy nhất một node đầu tiên trong DSLK, cách này cũng là cách được triển khai phổ biến trong các tài liệu về CTDL và Giải thuật cũng như các website nổi tiếng như : Geeksforgeeks, Leetcode..

Để cài đặt bằng cách này, bạn cần sử dụng con trỏ tới con trỏ hoặc tham chiếu trong C++

Tất nhiên là trong C++ bạn cũng có thể cài đặt bằng con trỏ tới con trỏ như trong C, tuy nhiên khi dùng tham chiếu sẽ dễ cài đặt hơn. Bạn có thể dựa vào mã nguồn C để triển khai cách đó cho C++

**Các bước để thêm node vào đầu DSLK :** 

- Cấp phát động một node mới
- Cho node mới lưu địa chỉ của node head (trỏ tới head)
- Cho node head trỏ ngược lại node mới (lưu địa chỉ node mới)
- Cập nhật head thành node mới tạo

**Mã nguồn C :** 

Cài đặt dựa trên con trỏ tới con trỏ, hàm duyệt DSLK không thay đổi con trỏ head của nó nên không cần con trỏ tới con trỏ hay tham chiếu, ngược lại hàm thêm đầu thay đổi node head nên cần con trỏ tới con trỏ.

```cpp
#include "stdio.h"
#include "string.h"
#include "stdlib.h"

struct node{
    int data;
    struct node *next; // dia chi node sau
    struct node *prev; // dia chi node truoc
};

typedef struct node node;

void duyet(node *head){
    while(head != NULL){
        printf("%d ", head->data);
        head = head->next; // cho head chuyen sang node ke tiep
    }
}

void themdau(node **head, int x){
    //1. Cap phat dong node moi
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    //2. Cho newNode tro vao head
    newNode->next = (*head);
    //3. Cho head tro nguoc lai node moi
    if(*head != NULL){
        (*head)->prev = newNode;
    }
    //4. Cap nhat head => newnode
    (*head) = newNode;
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(&head, i);
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

void themdau(node *&head, int x){
    //1. Cap phat dong node moi
    node *newNode = new node;
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    //2. Cho newNode tro vao head
    newNode->next = head;
    //3. Cho head tro nguoc lai node moi
    if(head != NULL){
        head->prev = newNode;
    }
    //4. Cap nhat head => newnode
    head = newNode;
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(head, i);
    }
    duyet(head);
}
```

Output :

```cpp
1 2 3 4 5 6 7 8 9 10
```

**Chú ý** : Khi cho node head trỏ ngược lại node mới thêm bạn cần kiểm tra head không phải con trỏ NULL, nếu head là con trỏ NULL bạn không cần phải trỏ ngược nếu không sẽ gây lỗi khi truy cập vào phần prev của node head.

---

**2. Thêm node vào đầu DSLK đôi quản lý bằng node head cách 2**

Cách cài đặt thứ 2 này thì bạn không cần dùng con trỏ tới con trỏ hay tham chiếu tới con trỏ nhưng bạn cần viết hàm trả về con trỏ, để sau khi thay đổi head trong hàm thêm node vào đầu thì trong hàm main khi gọi hàm bạn sẽ gán lại hàm đó cho head.

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

node* themdau(node *head, int x){
    //1. Cap phat dong node moi
    node *newNode = (node*)malloc(sizeof(node));
    newNode->data = x;
    newNode->next = newNode->prev = NULL;
    //2. Cho newNode tro vao head
    newNode->next = head;
    //3. Cho head tro nguoc lai newNode
    if(head != NULL){
        head->prev = newNode;
    }
    //4. Cap nhat head => newnode
    head = newNode;
    return head;
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
       head = themdau(head, i);
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

    newNode->next = head;
    if(head != NULL){
        head->prev = newNode;
    }
    head = newNode;
    return head;
}

int main(){
    node *head = NULL;
    for(int i = 10; i >= 1; i--){
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

**3. Thêm node vào đầu DSLK quản lý bằng node head và tail**

Cách cài đặt thứ 3 này mình thấy khá phổ biến tại các tutorial cũng như sách giáo trình tại Việt Nam, tuy nhiên cách cài đặt này theo mình đã làm cho các bạn quên đi mất bản chất của DSLK mỗi node đều là con trỏ. Hầu như mình chưa thấy tài liệu tiếng Anh nào cài đặt theo cách này, nó làm việc cài đặt có phần dễ tiếp cận hơn nên nếu bạn có thể cài đặt theo cách này thì có thể tham khảo.

Nếu đi phỏng vấn, tham gia cuộc thi mà họ không cho phép cài đặt như cách 3 này thì bạn cũng đã biết cách 1 và cách 2.

Cách cài đặt thứ 3 này thường xây dựng thêm 1 cấu trúc DSLK có 2 node head(đầu) và tail (cuối) để quản lý DSLK

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

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(&l, i);
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

void themdau(LIST &l, int x){
    node *newNode = new node;
    newNode->data = x;
    newNode->next = NULL;
    if(l.head == NULL){
        l.tail = l.head = newNode;
    }
    else{
        newNode->next = l.head;
        l.head->prev = newNode;
        l.head = newNode;
    }
}

int main(){
    LIST l;
    l.head = NULL; l.tail = NULL;
    for(int i = 10; i >= 1; i--){
        themdau(l, i);
    }
    duyet(l);
}
```

Output :

```cpp
1 2 3 4 5 6 7 8 9 10
```

---

**Video Thêm Node Vào Đầu DSLK Đôi**
