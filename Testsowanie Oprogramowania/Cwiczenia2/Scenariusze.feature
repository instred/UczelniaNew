Feature: Zapisanie się do newslettera

  Scenario: Zapisuję się do newslettera podając poprawny adres e-mail
    When Wprowadzam poprawny mail
    And Klikam przycisk "zapisz mnie"
    Then Pojawia się komunikat, który informuje mnie, ze wysłano do mnie link aktywacyjny

  Scenario Outline: Zapisuje sie do newslettera podajac niepoprawny adres e-mail
    When Wprowadzam niepoprawny mail
    And Klikam Przycisk "zapisz mnie"
    Then Wyświetla się komunikat “Formularz zawiera błędy. Sprawdź poprawność danych”

    Examples:
    | e-mail                   |
    | jan.kowalski@interia.pl  |
    | aaaaa                    |


Scenariusze, które bazują na dodanych przeze mnie funkcjach na stronie:
  - Obsługa błędów: Sprawdzenie czy mail się powtarza w bazie danych
  - Dodatkowe okno: Sprawdzanie lokalizacji - pokazuje się okienko z wyborem języka


Feature: Zapisanie się do newslettera mailem, który już był wcześniej zapisany

  Scenario: Zapisuję się do newslettera, używając adresu, z którego się wcześniej zapisałem
    When Wprowadzam powtarzający się mail
    And Klikam przycisk "zapisz mnie"
    Then Pojawia się komunikat "Mail jest już zapisany"

    Examples:
    | e-mail                   |
    | jan.kowalski@interia.pl  |
    | jan.kowalski@interia.pl  |


Feature: Sprawdzanie lokalizacji użytkownika

  Scenario: Wejście na stronę z innego kraju
    When Wchodzę na stronę z newsletterem, będąc w innym państwie
    And Pojawia się okno z możliwością wyboru języka strony
    And Klikam wybrany język
    Then Język strony zmienia się na wybrany

  Scenario Outline: Wejście na stronę będąc w Polsce
    When Wchodzę na stronę z newsletterem, będąc w Polsce
    Then Nie pojawia się komunikat o zmianie języka, jak i język strony zostaje ten sam