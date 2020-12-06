from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()  # Esto arreglaría el problema del foreing key, que se da si usas un db distinto de sqlite, como Mysql
            item = ItemModel('test', 19.99, 1) # ese 1 es un foreing key, porque es el key de la tabla de tiendas

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))


    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')