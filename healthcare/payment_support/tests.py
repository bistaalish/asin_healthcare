from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Product, Order, Purchase

class ProductModelTest(TestCase):
    """Test cases for the Product model."""

    @classmethod
    def setUpTestData(cls):
        """Set up initial data for tests."""
        Product.objects.create(name='Test Product', price=19.99, description='This is a test product')

    def test_product_name_max_length(self):
        """Test maximum length of the product name."""
        print("Testing maximum length of product name...")
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        if max_length == 100:
            print("\033[92mSuccess: Maximum length of product name is correct.\033[0m")  # Green for success
        else:
            print("\033[91mFailed: Maximum length of product name is incorrect.\033[0m")  # Red for failure

    def test_blank_name_raises_error(self):
        """Test that creating a product with a blank name raises a ValidationError."""
        print("Testing creation of product with a blank name...")
        try:
            Product.objects.create(name='', price=19.99, description='Test Description')
            print("\033[91mFailed: Blank name did not raise ValidationError.\033[0m")  # Red for failure
        except ValidationError:
            print("\033[92mSuccess: Blank name raised ValidationError as expected.\033[0m")  # Green for success

    # Add more test cases for the Product model

class OrderModelTest(TestCase):
    """Test cases for the Order model."""

    @classmethod
    def setUpTestData(cls):
        """Set up initial data for tests."""
        user = User.objects.create(username='testuser')
        product = Product.objects.create(name='Test Product', price=19.99, description='This is a test product')
        Order.objects.create(customer=user, product=product)

    def test_order_customer_relationship(self):
        """Test the relationship between an order and a customer."""
        print("Testing the relationship between an order and a customer...")
        order = Order.objects.get(id=1)
        if order.customer.username == 'testuser':
            print("\033[92mSuccess: Order is associated with the correct customer.\033[0m")  # Green for success
        else:
            print("\033[91mFailed: Order is not associated with the correct customer.\033[0m")  # Red for failure

    def test_invalid_order_creation(self):
        """Test that creating an order without necessary fields raises a ValueError."""
        print("Testing creation of an order without necessary fields...")
        try:
            Order.objects.create()  # Trying to create an order without necessary fields
            print("\033[91mFailed: Order created without necessary fields.\033[0m")  # Red for failure
        except ValueError:
            print("\033[92mSuccess: Order creation without necessary fields raised ValueError.\033[0m")  # Green for success

    # Add more test cases for the Order model

class PurchaseModelTest(TestCase):
    """Test cases for the Purchase model."""

    @classmethod
    def setUpTestData(cls):
        """Set up initial data for tests."""
        user = User.objects.create(username='testbuyer')
        Purchase.objects.create(buyer_name='Test Buyer', email='test@example.com', buyer=user, method='single package')

    def test_purchase_method_choices(self):
        """Test the display of payment method choices."""
        print("Testing the display of payment method choices...")
        purchase = Purchase.objects.get(id=1)
        if purchase.get_method_display() == 'buy one':
            print("\033[92mSuccess: Display of payment method choices is correct.\033[0m")  # Green for success
        else:
            print("\033[91mFailed: Display of payment method choices is incorrect.\033[0m")  # Red for failure

    def test_purchase_paid_status(self):
        """Test the payment status of a purchase."""
        print("Testing the payment status of a purchase...")
        purchase = Purchase.objects.get(id=1)
        if not purchase.is_paid():  # Initially, should not be paid
            purchase.stage1 = True
            purchase.stage2 = True
            purchase.stage3 = True
            if purchase.is_paid():
                print("\033[92mSuccess: Purchase is marked as paid.\033[0m")  # Green for success
            else:
                print("\033[91mFailed: Purchase is not marked as paid.\033[0m")  # Red for failure

    def test_invalid_purchase_creation(self):
        """Test that creating a purchase with an invalid method choice raises a ValidationError."""
        print("Testing creation of a purchase with an invalid method choice...")
        try:
            Purchase.objects.create(buyer_name='Test Buyer', email='test@example.com', method='invalid')
            print("\033[91mFailed: Purchase created with an invalid method choice.\033[0m")  # Red for failure
        except ValidationError:
            print("\033[92mSuccess: Purchase creation with an invalid method choice raised ValidationError.\033[0m")  # Green for success

    def test_purchase_diagnosis_field(self):
        """Test the existence and initial value of the diagnosis field."""
        print("Testing the existence and initial value of the diagnosis field...")
        purchase = Purchase.objects.get(id=1)
        if hasattr(purchase, 'diagnosis') and purchase.diagnosis is None:
            print("\033[92mSuccess: Diagnosis field exists and has an initial value of None.\033[0m")  # Green for success
        else:
            print("\033[91mFailed: Diagnosis field does not exist or has an incorrect initial value.\033[0m")  # Red for failure

    # Add more test cases for the Purchase model
