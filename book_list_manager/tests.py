from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book

class BookListCreateViewTestCase(APITestCase):
    def setUp(self):
        """Set up test prerequisites."""
        self.url = reverse('list-create-books')
        self.book_data = {
            "title": "Introduction to Java",
            "author": "Test Author",  # Ensure it's a string
            "publication_date": "2023-05-05",
            "isbn": "1234567890123"  # Ensure it's 10 or 13 digits
        }

    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expect 200 OK

    def test_create_book(self):
        """Test creating a new book."""
        response = self.client.post(self.url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Expect 201 Created
        self.assertEqual(Book.objects.count(), 1)  # Ensure book was added
        self.assertEqual(Book.objects.first().title, self.book_data["title"])  # Validate title


class RetrieveUpdateDeleteViewTestCase(APITestCase):
    def setUp(self):
        """Set up test prerequisites."""
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="Test Author",
            publication_date="2023-01-01",
            isbn="1234567890"
        )
        self.valid_url = reverse('retrieve-update-delete-books', kwargs={'pk': self.book.pk})
        self.invalid_url = reverse('retrieve-update-delete-books', kwargs={'pk': 9999})
        self.updated_data = {
            "title": "Advanced Django",
            "author": "Updated Author Name",  # Ensure it's a string
            "publication_date": "2023-01-01",
            "isbn": "0987654321"  # Ensure it's 10 or 13 digits
        }

    def test_retrieve_book_valid_pk(self):
        """Test retrieving a book with a valid primary key."""
        response = self.client.get(self.valid_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expect 200 OK
        self.assertEqual(response.data["title"], self.book.title)  # Validate title

    def test_retrieve_book_invalid_pk(self):
        """Test retrieving a book with an invalid primary key."""
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Expect 404 Not Found

    def test_update_book(self):
        """Test updating a book's details."""
        response = self.client.put(self.valid_url, self.updated_data, format="json")
        print(response.status_code)  # 🔍 Debugging output
        print(response.data)  # 🔍 Debugging output

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expect 200 OK
        self.book.refresh_from_db()  # Refresh instance from DB
        self.assertEqual(self.book.title, self.updated_data["title"])  # Validate updated title
        self.assertEqual(self.book.author, self.updated_data["author"])  # Validate updated author

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.valid_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Expect 204 No Content
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())  # Ensure book is deleted
