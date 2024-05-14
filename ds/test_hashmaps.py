from unittest import TestCase, main

from hashmaps import HashMap, DynamicHashMap


class HashMapTest(TestCase):
    def setUp(self):
        self.hs = HashMap()
    
    def test_put(self):
        self.hs.put(1, "test")
        self.assertEqual(self.hs.get(1), "test")

    def test_update(self):
        self.hs.put(1, 100)
        self.hs.put(1, 200)
        self.assertEqual(self.hs.get(1), 200)
    
    def test_delete(self):
        self.hs.put(1, 100)

        self.assertEqual(self.hs.delete(1), 100)

        self.assertIsNone(self.hs.get(1))

    def test_delete_not_in_hashmap(self):
        self.assertIsNone(self.hs.get(1))
        self.assertIsNone(self.hs.delete(1))

    def test_size(self):
        self.hs.put(1, 1)
        self.hs.put(2, 1)
        self.hs.put(3, 1)
        self.hs.put(4, 1)

        self.assertEqual(self.hs.size, 4)


class DynamicHashMapTest(TestCase):
    def setUp(self):
        self.hs = DynamicHashMap()
    
    def test_put(self):
        self.hs.put(1, 100)
        self.assertEqual(self.hs.get(1), 100)

    def test_update(self):
        self.hs.put(1, 100)
        self.hs.put(1, 200)
        self.assertEqual(self.hs.get(1), 200)
    
    def test_delete(self):
        self.hs.put(1, 100)

        self.assertEqual(self.hs.delete(1), 100)

        self.assertIsNone(self.hs.get(1))

    def test_delete_not_in_hashmap(self):
        self.assertIsNone(self.hs.get(1))
        self.assertIsNone(self.hs.delete(1))

    def test_size(self):
        self.hs.put(1, 1)
        self.hs.put(2, 1)
        self.hs.put(3, 1)
        self.hs.put(4, 1)

        self.assertEqual(self.hs.size, 4)

    def test_rehash(self):
        self.assertEqual(len(self.hs.array), 10)
        self.hs.put(1, 100)
        self.hs.put(11, 200)

        self.assertEqual(len(self.hs.array), 40)
        self.assertEqual(self.hs.get(1), 100)
        self.assertEqual(self.hs.get(11), 200)

        self.hs.put(2, 100)
        self.hs.put(22, 200)

        self.assertEqual(len(self.hs.array), 40)
        self.assertEqual(self.hs.get(2), 100)
        self.assertEqual(self.hs.get(22), 200)


if __name__ == "__main__":
    main()
