Feature: Display the books in a Table with the correct information
  The user can edit number of rows displayed and sort books by column,
  but the info we need displayed is:
  1. Image
  2. Title
  3. Author
  4. Publisher

  Background:
    Given a catalog with these books:
      | Image | Title             | Author                | Publisher       |
      | 0.jpg | Git Pocket Guide  | Richard E. Silverman  | O'Reilly Media  |

  Scenario: Books have an Image, Title, Author and Publisher
    When I open the catalog
    Then I should see 8 books
    And each book should have a value for Image, Title, Author and Publisher

    Scenario Outline: User can change the number of rows to see a single page
      When I open the catalog
      And change the number of rows to <amount> rows
      Then I should see <amount> rows

      Examples:
      | amount  |
      | 5       |
      | 20      |
      | 25      |
      | 50      |
      | 100     |