class Node:
    def __init__(self, data):
        self.data = data   # 表示对应的元素值
        self.next = None   # 表示下一个链接的链点


class Linked_List:
    def __init__(self, head=None):   #链表初始化函数
        self.head = head   # 表示链表的头部元素#

    def append(self, new_element):
        """
        在链表后面增加一个元素
        """
        current = self.head
        if self.head:   # 当头部结点存在时
            # 遍历到链表最后一个元素
            while current.next:
                current = current.next
            current.next = new_element
        else:   # 当头部结点不存在时
            self.head = new_element

    def is_empty(self):
        """
        判断链表是否为空
        """
        return not self.head

    def get_length(self):
        """
        获取链表的长度
        """
        temp = self.head
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        return length

    def insert(self, position, new_element):
        """
        在链表中指定索引处插入元素
        """
        if position < 0 or position > self.get_length():
            raise IndexError('insert插入时，key的值超出了范围')
        temp = self.head
        if position == 0:
            new_element.next, self.head = temp, new_element
            return
        i = 0
        while i < position:
            pre, temp = temp, temp.next
            i += 1
        pre.next, new_element.next = new_element, temp

    def print_list(self):
        """
        遍历链表，并将元素依次打印出来
        """
        print("linked_list: ")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def remove(self, position):
        """
        删除指定索引的链表元素
        """
        if position < 0 or position > self.get_length() - 1:
            raise IndexError('删除元素的位置超出范围')
        i = 0
        temp = self.head
        while temp != None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return
            pre, temp = temp, temp.next
            i += 1
            if i == position:
                pre.next, temp.next = temp.next, None
                return

    def reverse(self):
        """
        链表反转
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def initlist(self, data_list):
        """
        将列表转换为链表
        """
        # 创建头结点
        self.head = Node(data_list[0])
        temp = self.head
        # 逐个为data内的数据创建结点，建立链表
        for i in data_list[1:]:
            node = Node(i)
            temp.next, temp = node, temp.next
