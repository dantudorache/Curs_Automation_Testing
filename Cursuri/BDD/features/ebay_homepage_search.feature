Feature: Test the search functionality of the homepage of ebay

  Background:
    Given Home page: I am on ebay homepage
    # Background = o modalitate prin care putem sa dan un context general testelor noastre
    # functioneaza in pereche cu Given
    # punem in Background orice element de context care este valabil pt toate scenariile din feature file
#############################################################################################################
    # TAGs = daca vrem sa separam testele pe care vrem sa le rulam si sa le executam individual sau grupate
    # un scenariu poate fi identificat prin mai multe taguri
    # behave -f html -o behave-report.html --tags=T1 => va rula primul scenariu
    # behave -f html -o behave-report.html --tags=BDD => va rula ambele scenarii
############################################################################################
    # SCENARIO OUTLINE = o modalitate prin care putem rula acelasi test de mai multe ori, avand input diferit
    # testul se va rula cate o data pentru fiecare input (prezent in Examples)
    # sesiunile de scenario outlines -> examples se pot si ele grupa cu tag


  @T1 @regression @BDD # taguri pt skip
  Scenario Outline: check that the user can make a simple search on the ebay homepage
    When Home page: I search for "<product_name>" from "<category_name>"
    Then Home page: I have at least "<nr_of_results>" results returned

    Examples:
      | product_name | category_name             | nr_of_results |
      | iphone       | Cell Phones & Accessories | 130000        |
      | samsung      | Consumer Electronics      | 120000        |

    Examples:
      | product_name | category_name        | nr_of_results |
      | TV           | Consumer Electronics | 12000         |
      | led          | Consumer Electronics | 3200          |

    Examples:
      | product_name | category_name                 | nr_of_results |
      | dress        | Clothing, Shoes & Accessories | 41000         |
      | sweter       | Clothing, Shoes & Accessories | 10000         |

  @T2 @functional @BDD
  Scenario:  check that the user can make an advanced search for a product
    When Home page: when I click on the advanced link
    When Advanced search page: I type pampers in the keyword textbox
    When Advanced search page: I select exact words, exact order from keyword option
    When Advanced search page: I click search button
    Then Home page: i have at least 1200 results returned
    
