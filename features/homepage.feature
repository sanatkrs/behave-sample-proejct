Feature: Verifying the homepage content on Amazon.co.uk

  Scenario Outline: Verify that the homepage is showing the header menu
     Given user input wrong email id "<login_id>" and password "<password>"
      When check the homepage
      Then check the homepage title
      Then header menu items should be present
    Examples:
      | login_id | password |
      | Admin | admin123       |
      | Sanat | sanat123       |


