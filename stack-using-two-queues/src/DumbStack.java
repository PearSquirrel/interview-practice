import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Queue;

public class DumbStack<T> {
    private Queue<T> queue1;
    private Queue<T> queue2;

    public DumbStack() {
        queue1 = new LinkedList<T>();
        queue2 = new LinkedList<T>();
    }

    public void push(T element) {
        queue1.add(element);
    }

    public T pop() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        T cur = queue1.remove();
        while (!queue1.isEmpty()) {
            queue2.add(cur);
            cur = queue1.remove();
        }
        Queue<T> tmp = queue1;
        queue1 = queue2;
        queue2 = tmp;

        return cur;
    }

    public T peek() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        T cur = queue1.peek();
        while (!queue1.isEmpty()) {
            cur = queue1.remove();
            queue2.add(cur);
        }
        Queue<T> tmp = queue1;
        queue1 = queue2;
        queue2 = tmp;

        return cur;
    }

    public boolean isEmpty() {
        return queue1.isEmpty();
    }

    public static void main(String[] args) {
        log("This is a horrible way to make a stack :)");
        DumbStack<String> dumb = new DumbStack<>();
        dumb.push("a");
        dumb.push("b");
        dumb.push("c");
        dumb.push("d");
        log(dumb.pop());
        log(dumb.pop());
        dumb.push("e");
        dumb.push("f");
        log(dumb.peek());
    }

    private static void log(Object o) {
        System.out.println(o.toString());
    }
}