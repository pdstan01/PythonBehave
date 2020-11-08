Feature: Testing redshelf

Scenario: Visit RedShelf web site and check it loads
When we visit "https://redshelf.com/"
Then it should have a title "RedShelf"

Scenario: Search for "Moby Dick" and check that it is found
Given we are on the home page
When we search for "Moby Dick"
Then "Herman Melville" should be displayed

Scenario: Search for "ABCDEFGH" and check that it is found
Given we are on the home page
When we search for "ABCDEFGH"
Then "Oh No! Looks like we don't have the eBook you're searching for." should be displayed
