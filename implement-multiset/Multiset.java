import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Multiset<T> {

    Map<T, MutableInteger> internalMap;

    public Multiset() {
        internalMap = new HashMap<>();
    }

    public Multiset add(T element) {
        MutableInteger count = internalMap.get(element);
        if (count == null) {
            internalMap.put(element, new MutableInteger(1));
        } else {
            count.increment();
        }
        return this;
    }

    public int count(T element) {
        MutableInteger count = internalMap.get(element);
        if (count == null) {
            return 0;
        }
        return count.get();
    }

    public Multiset remove(T element) {
        MutableInteger count = internalMap.get(element);
        if (count != null && count.decrement() <= 0) {
            internalMap.remove(element);
        }
        return this;
    }

    public boolean contains(T element) {
        return internalMap.containsKey(element);
    }

    public Set<T> elementSet() {
        return internalMap.keySet();
    }

    public Set<Entry<T>> entrySet() {
        Set<Entry<T>> set = new HashSet<>();
        for (T key : internalMap.keySet()) {
            set.add(new Entry<>(key, internalMap.get(key).get()));
        }
        return set;
    }

    private class MutableInteger {
        private int val;

        public MutableInteger(int val) {
            this.val = val;
        }

        public int increment() {
            return val++;
        }

        public int decrement() {
            return val--;
        }

        public int set(int val) {
            this.val = val;
            return val;
        }

        public int get() {
            return this.val;
        }
    }

    private class Entry<T> {

        T element;
        int count;

        protected Entry(T element, int count) {
            this.element = element;
            this.count = count;
        }

        public int getCount() {
            return count;
        }

        public T getElement() {
            return element;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Entry)) {
                return false;
            }
            Entry<T> that = (Entry<T>) o;
            return element.equals(that.element)
                    && count == that.count;
        }

        @Override
        public int hashCode() {
            return element.hashCode() * 31 + count;
        }
    }

    public static void main(String[] args) {
        Multiset<String> set = new Multiset<>();

        set.add("a").add("a").add("a").add("a").remove("a");
        set.add("b").add("b").add("b");
        set.add("c");
        set.add("d").remove("d");
        log(set.count("a"));
        log(set.count("b"));
        log(set.count("c"));
        log(set.count("d"));
    }

    private static void log(Object o) {
        System.out.println(o.toString());
    }
}
