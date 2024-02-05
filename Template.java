import java.io.*;
import java.util.StringTokenizer;

public class Template {

  private static InputReader in;
  private static PrintWriter out;
  private static DoublyLinkedList rooms = new DoublyLinkedList();

  public static void main(String[] args) {
    InputStream inputStream = System.in;
    in = new InputReader(inputStream);
    OutputStream outputStream = System.out;
    out = new PrintWriter(outputStream);

    int N = in.nextInt();

    for (int i = 0; i < N; i++) {
      char command = in.nextChar();
      char direction;

      switch (command) {
        case 'A':
          direction = in.nextChar();
          char type = in.nextChar();
          add(type, direction);
          break;
        case 'D':
          direction = in.nextChar();
          out.println(delete(direction));
          break;
        case 'M':
          direction = in.nextChar();
          out.println(move(direction));
          break;
        case 'J':
          direction = in.nextChar();
          out.println(jump(direction));
          break;
      }
    }

    out.close();
  }

  public static void add(char type, char direction) {
    // Buat ruangan baru dengan ID yang sesuai
    int roomID = rooms.size + 1;
  
    // Tambahkan ruangan baru ke sisi yang ditentukan oleh direction
    if (direction == 'R') {
      rooms.add(roomID, type);
    } else if (direction == 'L') {
      rooms.add(roomID, type);
    } else {
      // Handle kesalahan masukan
      throw new IllegalArgumentException("Direction harus 'R' atau 'L'.");
    }
  }
  
  public static int delete(char direction) {
    Object current;
    // Hapus ruangan di sisi yang ditentukan oleh direction
    if (current == null) {
      return -1; // Daftar kosong
    }
  
    int deletedRoomID = -1;
  
    if (direction == 'R') {
      deletedRoomID = rooms.delete();
    } else if (direction == 'L') {
      deletedRoomID = rooms.delete(true);
    } else {
      // Handle kesalahan masukan
      throw new IllegalArgumentException("Direction harus 'R' atau 'L'.");
    }
  
    return deletedRoomID;
  }
  
  public static int jump(char direction) {
    Object current;
    // Loncat ke ruangan khusus di sebelah kanan (R) atau kiri (L)
    if (current == null) {
      return -1;
    }
  
    int roomID = rooms.jump(direction);
  
    return roomID;
  }
  
  public String traverse() {
    Object first;
    if (first == null) {
      return ""; // Daftar kosong
    }
  
    ListNode traverseNode = (Template.ListNode) first;
    StringBuilder result = new StringBuilder();
    do {
      result.append(traverseNode + ((traverseNode.next != first) ? " | " : ""));
      traverseNode = traverseNode.next;
    } while (traverseNode != first);
  
    return result.toString();
  }
  

class DoublyLinkedList {

  private int nodeIdCounter = 1;
  ListNode first;
  ListNode current;
  ListNode last;
  int size = 0;

  /*
   * Method untuk menambahkan ListNode ke sisi kiri (prev) atau kanan (next) dari {@code current} ListNode
   */
 public ListNode add(int id, char type) {
  ListNode newNode = new ListNode(type, id);

  if (first == null) {
    first = newNode;
    last = newNode;
    newNode.next = newNode;
    newNode.prev = newNode;
  } else {
    if (current == null) {
      newNode.next = first;
      newNode.prev = last;
      first.prev = newNode;
      last.next = newNode;
      last = newNode;
    } else {
      if (current == first && id == 1) {
        newNode.next = first;
        newNode.prev = last;
        first.prev = newNode;
        last.next = newNode;
        first = newNode;
      } else if (current == last && id == size + 1) {
        newNode.next = first;
        newNode.prev = last;
        first.prev = newNode;
        last.next = newNode;
        last = newNode;
      } else {
        if (id <= size / 2) {
          for (int i = 1; i < id; i++) {
            current = current.next;
          }
        } else {
          for (int i = size + 1; i > id; i--) {
            current = current.prev;
          }
        }
        newNode.next = current.next;
        newNode.prev = current;
        current.next.prev = newNode;
        current.next = newNode;
        current = newNode;
      }
    }
  }

  size++;
  return newNode;
}

public int delete() {
  // Hapus ruangan di sebelah kanan current
  if (current == null) {
    return -1;
  }

  int deletedRoomID = current.id;
  if (current == first) {
    if (size == 1) {
      first = null;
      last = null;
      current = null;
    } else {
      first = current.next;
      last.next = first;
      first.prev = last;
      current = first;
    }
  } else if (current == last) {
    last = current.prev;
    last.next = first;
    first.prev = last;
    current = first;
  } else {
    current.prev.next = current.next;
    current.next.prev = current.prev;
    current = current.next;
  }

  size--;
  return deletedRoomID;
}

public int delete(boolean left) {
  // Hapus ruangan di sebelah kiri current
  if (current == null) {
    return -1;
  }

  int deletedRoomID = current.id;
  if (current == first) {
    if (size == 1) {
      first = null;
      last = null;
      current = null;
    } else {
      last.next = first.next;
      first.next.prev = last;
      first = first.next;
      current = first;
    }
  } else if (current == last) {
    current.prev.next = first;
    first.prev = current.prev;
    last = current.prev;
    current = first;
  } else {
    current.prev.next = current.next;
    current.next.prev = current.prev;
    current = current.prev;
  }

  size--;
  return deletedRoomID;
}

public int move() {
  // Pindah ke ruangan di sebelah kanan current
  if (current == null || current == last) {
    return -1;
  }
  current = current.next;
  return current.id;
}

public int move(boolean left) {
  // Pindah ke ruangan di sebelah kiri current
  if (current == null || current == first) {
    return -1;
  }
  current = current.prev;
  return current.id;
}

public int jump(char direction) {
  // Loncat ke ruangan khusus di sebelah kanan (R) atau kiri (L)
  if (current == null) {
    return -1;
  }

  ListNode jumpNode = (direction == 'R') ? current.next : current.prev;
  if (jumpNode != null && jumpNode.element.equals('S')) {
    current = jumpNode;
    return current.id;
  }

  return -1;
}


  /**
   * Method untuk mengunjungi setiap ListNode pada DoublyLinkedList
   */
  public String traverse() {
    ListNode traverseNode = first;
    StringBuilder result = new StringBuilder();
    do {
      result.append(traverseNode + ((traverseNode.next != first) ? " | " : ""));
      traverseNode = traverseNode.next;
    } while (traverseNode != first);

    return result.toString();
  }
}

class ListNode {

  Object element;
  ListNode next;
  ListNode prev;
  int id;

  ListNode(Object element, int id) {
    this.element = element;
    this.id = id;
  }

  public String toString() {
    return String.format("(ID:%d Elem:%s)", id, element);
  }
}
}