from django.test import TestCase

# Create your tests here.
{
  allPosts {
    title
    subtitle
    author {
      user {
        username
      }
    }
    tags {
      name
    }
  }
}