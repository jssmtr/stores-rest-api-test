from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest

class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test_store')

        self.assertEqual(store.name, 'test_store', "custom error message")