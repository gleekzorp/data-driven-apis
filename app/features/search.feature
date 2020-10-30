Feature: User can filter the list of books with a Search

  Background:
    Given a catalog with these books:
      | Image | Title             | Author                | Publisher       |
      | 0.jpg | Git Pocket Guide  | Richard E. Silverman  | O'Reilly Media  |

  Scenario Outline: User enters an exact search
    When I search <query>
    Then I should see <result> book(s)

      Examples:
        | query               | result  |
        | "Git Pocket Guide"  | 1       |
        | "eric elliot"       | 1       |
        | "O'Reilly Media"    | 6       |
        | "Carlos Kidman"     | 0       |

  Scenario Outline:
    When I search <query>
    Then I should see <result> book(s)

      Examples:
        | query       | result  |
        | javascript  | 4       |
        | a           | 8       |
        | as          | 6       |
        | asf         | 0       |