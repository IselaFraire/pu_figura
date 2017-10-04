Feature: Area de la figura geometrica circulo
    Como usuario de la clase de matematicas
    deseo sacar el area del circulo
    para obtener el area del circulo de la manera mas precisa

    Scenario: Area circulo 10
        Dado que ingreso el radio "10"
        cuando realizo la operacion
        entonces obtengo el area "314.16"

    Scenario: Area circulo 50
        Dado que ingreso el radio "50"
        cuando realizo la operacion
        entonces obtengo el area "7854"

    Scenario: Area circulo 5
        Dado que ingreso el radio "5"
        cuando realizo la operacion
        entonces obtengo el area "78.54"
