import unittest
from app.models import load_data, preprocess_data, train_model

class TestModels(unittest.TestCase):

    def test_load_data(self):
        df = load_data('data/sample_data.csv')
        self.assertFalse(df.empty)

    def test_preprocess_data(self):
        df = load_data('data/sample_data.csv')
        X_train, X_test, y_train, y_test = preprocess_data(df)
        self.assertEqual(X_train.shape[0], y_train.shape[0])

    def test_train_model(self):
        df = load_data('data/sample_data.csv')
        X_train, X_test, y_train, y_test = preprocess_data(df)
        model = train_model(X_train, y_train)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
